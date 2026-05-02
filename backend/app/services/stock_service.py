import pandas as pd
from app.repositories.stock_repository import StockRepository


class StockService:
    def __init__(self) -> None:
        self.repo = StockRepository()

    def _load(self) -> pd.DataFrame:
        return self.repo.load_prices()

    def get_kpi(self, date_from: str | None = None, date_to: str | None = None) -> dict:
        df = self._load()
        if date_from:
            df = df[df['date'] >= date_from]
        if date_to:
            df = df[df['date'] <= date_to]
        return {
            'rows': int(len(df)),
            'symbols': int(df['symbol'].nunique()),
            'avg_close': float(df['close'].mean()),
            'avg_volume': float(df['volume'].mean())
        }

    def get_timeseries(self, symbols: list[str], date_from: str | None = None, date_to: str | None = None) -> dict:
        df = self._load()
        if symbols:
            df = df[df['symbol'].isin(symbols)]
        if date_from:
            df = df[df['date'] >= date_from]
        if date_to:
            df = df[df['date'] <= date_to]
        g = df.groupby('date', as_index=False)['close'].mean()
        return {'items': g.to_dict(orient='records')}

    def get_category_stats(self) -> dict:
        df = self._load()
        summary = df.groupby(['sector', 'industry'])['close'].agg(['count', 'mean', 'std', 'min', 'max']).reset_index()
        return {'items': summary.fillna(0).to_dict(orient='records')}

    def get_rows(self, limit: int, symbols: list[str]) -> dict:
        df = self._load()
        if symbols:
            df = df[df['symbol'].isin(symbols)]
        return {'items': df.head(limit).to_dict(orient='records')}

    def rule_demo(self, vol_threshold: float) -> dict:
        df = self._load().copy()
        grouped = df.groupby('symbol')['close']
        vol = grouped.pct_change().groupby(df['symbol']).std().fillna(0)
        high_vol_symbols = vol[vol >= vol_threshold].index.tolist()
        return {'vol_threshold': vol_threshold, 'high_vol_symbols': high_vol_symbols, 'count': len(high_vol_symbols)}
