from modules.matcher import BeerMatcher

SETTINGS = {
    "db_path": "./data/beer.csv"
}

if __name__ == "__main__":
    _entrypoint = BeerMatcher(**SETTINGS)
    _entrypoint.load()
    result = _entrypoint.run()

    print(result)
