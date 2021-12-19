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

        print('Введите крепость пива')
        beer_props['Алкоголь:'] = float(int(input()) / 100)

        return beer_props

    def _select_stage(self, beer_props: dict) -> pd.DataFrame:
        return self._db.select(beer_props)
