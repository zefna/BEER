from modules.matcher import BeerMatcher

TEST_SETTINGS = {
    "db_path": "../data/beer.csv"
}

SELECT_PROPS = {
    'Алкоголь:': 0.1,
}


def test_class_select():
    test_class = BeerMatcher(**TEST_SETTINGS)
    test_class.load()

    result = test_class._select_stage(SELECT_PROPS)

    assert result is not None
    assert len(result) > 0


if __name__ == "__main__":
    test_class_select()
