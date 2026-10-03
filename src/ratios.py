"""Cálculo de ratios financieros a partir de los estados de yfinance.

Los estados vienen con las partidas en filas y los años en columnas.
"""
import pandas as pd


def fila(df: pd.DataFrame, *nombres: str) -> pd.Series:
    """Devuelve la primera partida que exista (los nombres cambian entre empresas)."""
    for n in nombres:
        if n in df.index:
            return df.loc[n].astype(float)
    print(f"Aviso: no encontrada ninguna de {nombres}")
    return pd.Series(float("nan"), index=df.columns)


def calcular_ratios(res: pd.DataFrame, bal: pd.DataFrame, flu: pd.DataFrame) -> pd.DataFrame:
    ventas = fila(res, "Total Revenue", "Operating Revenue")
    bruto = fila(res, "Gross Profit")
    ebit = fila(res, "Operating Income", "EBIT")
    ebitda = fila(res, "EBITDA", "Normalized EBITDA")
    neto = fila(res, "Net Income", "Net Income Common Stockholders")

    activo = fila(bal, "Total Assets")
    patrimonio = fila(bal, "Stockholders Equity", "Common Stock Equity")
    deuda = fila(bal, "Total Debt")  # incluye arrendamientos (NIIF 16)
    caja = fila(bal, "Cash And Cash Equivalents",
                "Cash Cash Equivalents And Short Term Investments")

    fco = fila(flu, "Operating Cash Flow")
    capex = fila(flu, "Capital Expenditure")

    r = pd.DataFrame({
        "Ventas (M€)": ventas / 1e6,
        "Crecimiento ventas": ventas.sort_index().pct_change(),
        "Margen bruto": bruto / ventas,
        "Margen EBITDA": ebitda / ventas,
        "Margen EBIT": ebit / ventas,
        "Margen neto": neto / ventas,
        "ROE": neto / patrimonio,
        "ROA": neto / activo,
        "Deuda total (M€)": deuda / 1e6,
        "Caja (M€)": caja / 1e6,
        "Deuda neta (M€)": (deuda - caja) / 1e6,
        "FCF (M€)": (fco + capex) / 1e6,  # capex viene en negativo
    })
    r.index = pd.to_datetime(r.index).year
    r.index.name = "Cierre ejercicio"
    return r.sort_index()
