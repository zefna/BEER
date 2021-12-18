from modules.matcher import BeerMatcher

TEST_SETTINGS = {
    "db_path": "../data/beer.csv"
}


def test_class_init():
    test_class = BeerMatcher(**TEST_SETTINGS)
    test_class.load()


if __name__ == "__main__":
    test_class_init()
