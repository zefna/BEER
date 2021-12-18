from abc import ABC, abstractmethod

import pandas as pd


class _BaseClient(ABC):
    DB_PATH: str

    def __init__(self, db_path: str):
        self.DB_PATH = db_path

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def select(self, props: dict):
        pass


class _ClientCSV(_BaseClient):
    _DATAFRAME: pd.DataFrame

    def load(self):
        self._DATAFRAME = pd.read_csv(self.DB_PATH, sep='|')
        self._configure_column_types()

    @abstractmethod
    def select(self, props: dict):
        selection = sum([self._DATAFRAME[prop] >= value for prop, value in props.items()]) > 0
        return self._DATAFRAME[selection]

    def _configure_column_types(self):
        self._DATAFRAME['Алкоголь:'] = self._convert_column_percents(self._DATAFRAME['Алкоголь:'])
        self._DATAFRAME['Плотность:'] = self._convert_column_percents(self._DATAFRAME['Плотность:'])

    @staticmethod
    def _convert_column_percents(column: pd.Series) -> pd.Series:
        column = column.str.rstrip('%')
        column = column.str.replace(',', '.').astype('float') / 100.0
        return column


class ClientFactory:
    _DB_INTERFACES = {
        'csv': _ClientCSV,
    }

    def __new__(cls, db_path: str, *args, **kwargs):
        selected_class = cls.interface_selection(db_path)
        return selected_class(db_path, *args, **kwargs)

    @classmethod
    def interface_selection(cls, db_path: str):
        _db_ext = db_path.rsplit(".", 1)[-1].lower()

        if _db_ext in cls._DB_INTERFACES:
            return cls._DB_INTERFACES[_db_ext]

        else:
            raise Exception("Unknown database type")
