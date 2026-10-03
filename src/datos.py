"""Funciones para descargar y guardar datos de mercado y estados financieros."""
from pathlib import Path

import pandas as pd
import yfinance as yf

TICKER = "ITX.MC"  # Inditex en la Bolsa de Madrid
RAW = Path(__file__).resolve().parents[1] / "data" / "raw"


def descargar_precios(ticker: str = TICKER, inicio: str = "2015-01-01") -> pd.DataFrame:
    """Precios diarios ajustados desde `inicio`."""
    df = yf.download(ticker, start=inicio, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex):  # yfinance devuelve columnas multinivel
        df.columns = df.columns.get_level_values(0)
    return df


def descargar_estados(ticker: str = TICKER) -> dict[str, pd.DataFrame]:
    """Cuenta de resultados, balance y flujos de caja anuales.

    Ojo: Yahoo solo ofrece ~4 años. Para series más largas usa los
    informes anuales de Inditex. Recuerda que su ejercicio fiscal
    termina el 31 de enero.
    """
    t = yf.Ticker(ticker)
    return {
        "resultados": t.financials,
        "balance": t.balance_sheet,
        "flujos": t.cashflow,
    }


def guardar(df: pd.DataFrame, nombre: str) -> Path:
    RAW.mkdir(parents=True, exist_ok=True)
    ruta = RAW / f"{nombre}.csv"
    df.to_csv(ruta)
    return ruta
