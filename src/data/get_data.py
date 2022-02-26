import logging
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"

    
def get_mall_customers(data_dir: Path) -> None:
    url = "https://www.kaggle.com/shwetabh123/mall-customers/download"
    df = pd.read_csv(url)

    df.to_feather(data_dir / "external" / "mall_customers.feather")


def get_titanic(data_dir: Path) -> None:
    url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    df = pd.read_csv(url)

    df.to_feather(data_dir / "external" / "titanic.feather")


def main():

    logger = logging.getLogger(__name__)
    logger.info("Downloading data from external websites and storing them in ./data/external/")
    
    logger.info("Downloading mall customers data")
    get_mall_customers(data_dir=DATA_DIR)
    logger.info("Mall customers data successfully downloaded")
    
    logger.info("Downloading titanic data")
    get_titanic(data_dir=DATA_DIR)
    logger.info("Titanic data successfully downloaded")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    main()
