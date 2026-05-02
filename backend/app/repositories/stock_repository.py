from pathlib import Path
import pandas as pd


class StockRepository:
    def __init__(self) -> None:
        self.file_path = Path(__file__).resolve().parents[3] / 'sample_data' / 'us_stocks_sample.csv'

    def load_prices(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)
        return df
