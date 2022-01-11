import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from modules.db_client import _BaseClient, ClientFactory

sns.set()

class BeerMatcher:
    _db: _BaseClient

    def __init__(self, db_path, **kwargs):
        self._db = ClientFactory(db_path)

    def load(self):
        self._db.load()

    def run(self):
        beer_props = self._user_interact_stage()
        selected_positions = self._select_stage(beer_props)

        return selected_positions

    @staticmethod
    def _user_interact_stage():
        beer_props = dict()

        def beer_props_update(prop):
            _in = input()
            if len(_in) == 0:
                pass
            elif len(_in) < 3:
                beer_props[prop] = float(int(_in) / 100)
            else:
                beer_props[prop] = (_in)
            return beer_props

        print('Введите крепость пива')
        beer_props_update('Алкоголь:')

        print('Введите плотность пива')
        beer_props_update('Плотность:')

        print('Введите цвет пива (светлое, тёмное, полутёмное)')
        beer_props_update('Цвет:')

        print('Выберите фильтрацию (фильтрованное, нефильтрованное)')
        beer_props_update('Фильтрация:')

        print('Введите страну изготовления')
        beer_props_update('Страна:')

        return beer_props

    def _select_stage(self, beer_props: dict) -> pd.DataFrame:
        return self._db.select(beer_props)
