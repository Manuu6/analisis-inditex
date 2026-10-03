# Análisis y valoración de Inditex (ITX.MC)

> ⚠️ Ejercicio académico con fines formativos. **No es una recomendación de inversión.**

**Autor:** Manuel Pimentel · CUNEF Universidad
**Fecha del análisis:** *[dd/mm/aaaa]*
**Precio de referencia:** *[X,XX €]* · **Precio objetivo:** *[X,XX €]* · **Recomendación:** *[Comprar / Mantener / Vender]*

---

## 1. Resumen ejecutivo

*[3-5 líneas con tu tesis: qué opinas de la empresa y por qué. Escríbelo al final, cuando hayas terminado todo el análisis.]*

## 2. La empresa en 1 minuto

- **Qué hace:** diseña, produce, distribuye y vende moda a través de tiendas físicas y canal online.
- **Marcas:** Zara, Pull&Bear, Massimo Dutti, Bershka, Stradivarius, Oysho, Zara Home y Lefties.
- **Plantilla:** más de 163.000 personas, unas 50.000 en España.
- **Cómo gana dinero:** vendiendo moda que sigue las tendencias de forma muy rápida, apoyándose en una fuerte y continuada inversión en tecnología y logística.

**Ventajas competitivas**

1. **Producción de proximidad:** fabrica buena parte cerca de España, lo que le permite reaccionar rápido a la demanda.
2. **Gestión del inventario en pequeñas tandas:** menos rebajas forzadas y un margen bruto muy alto (58,3%).
3. **Balance sólido:** más caja que deuda financiera y elevada generación de caja.

**Principales riesgos**

1. **Geopolítica y logística:** como depende tanto del transporte global, tensiones como las del estrecho de Ormuz pueden encarecer el petróleo y los fletes.
2. **Divisas:** vende en muchas monedas; en 2025 el tipo de cambio restó unos 4 puntos al crecimiento (+7% constante vs. +3% en euros).
3. **Competencia y tecnología:** su ventaja es la rapidez. Competidores digitales como Shein o Temu presionan en precio y velocidad, lo que obliga a seguir invirtiendo fuerte en tecnología.

*Otros a vigilar: costes laborales y reputación en la cadena de suministro, ciberseguridad.*

**Cifras clave del ejercicio 2025 (feb. 2025 – ene. 2026)**

| Métrica | Valor | Variación |
|---|---|---|
| Ventas | 39.864 M€ | +3% (+7% a tipo de cambio constante) |
| Margen bruto | 58,3% s/ ventas | |
| Costes operativos | | +2,8% |
| EBITDA / EBIT / BAI | | +5% a +6% |
| Beneficio neto (consolidado) | 6.220 M€ | +6% |
| Dividendo por acción | 1,75 € (1,20 ordinario + 0,55 extraordinario) | |
| Dividendo total | 5.454 M€ | |
| Pay-out (dividendo / beneficio consolidado) | ≈ 88% | |

**Lectura:** los costes operativos crecen menos que las ventas (apalancamiento operativo), así que los beneficios crecen el doble que las ventas. El alto pay-out muestra que la empresa genera más caja de la que necesita para invertir.

**Nota:** la propuesta de reparto parte del beneficio de la sociedad matriz (6.360 M€: 906 M€ a reservas y 5.454 M€ a dividendos), no del consolidado del grupo (6.220 M€).

## 3. Análisis financiero

Datos: Yahoo Finance vía yfinance (notebook `02_ratios_financieros`). Ejercicio fiscal de febrero a enero. Ratios completos en [`data/processed/ratios.csv`](data/processed/ratios.csv).

| Métrica | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|
| Ventas (M€) | 32.569 | 35.947 | 38.632 | 39.864 |
| Crecimiento ventas | – | +10,4% | +7,5% | +3,2% |
| Margen bruto | 57,0% | 57,8% | 57,8% | 58,3% |
| Margen EBITDA | 25,4% | 27,9% | 28,3% | 29,0% |
| Margen EBIT | 18,1% | 19,2% | 19,9% | 20,2% |
| Margen neto | 12,7% | 15,0% | 15,2% | 15,6% |
| ROE | 24,3% | 28,9% | 29,8% | 30,5% |
| ROA | 13,8% | 16,4% | 16,9% | 17,5% |
| FCF (M€)\* | 5.259 | 6.795 | 6.616 | 6.520 |

\* FCF = flujo de caja operativo − capex. No descuenta los pagos por arrendamientos (NIIF 16), por lo que sobrestima la caja disponible.

**Conclusiones**

1. **El crecimiento se frena** (+10% → +3%), en parte por el efecto divisa (+7% a tipo constante en 2025).
2. **Los márgenes mejoran año tras año**: el margen EBIT sube del 18% al 20% gracias al apalancamiento operativo.
3. **Rentabilidad excelente**: ROE del 30% con muy poca deuda financiera.
4. **Generación de caja estable** en torno a 6.500 M€, suficiente para cubrir un dividendo de ~5.450 M€.

**Posición financiera neta** (caja − deuda financiera, sin arrendamientos): **10.958 M€** a 31/01/2026 (11.495 M€ un año antes). Inditex no tiene deuda neta: la "deuda total" de Yahoo (~6.000 M€) son casi todo arrendamientos de tiendas (NIIF 16). La ligera bajada se explica por el elevado dividendo (~5.450 M€).

**Pregunta clave para la valoración:** ¿puede Inditex seguir ampliando márgenes con un crecimiento de ventas cada vez menor?

## 4. Valoración

- **DCF:** *[valor por acción y supuestos principales: crecimiento, márgenes, WACC, g]*
- **Múltiplos comparables:** *[EV/EBITDA y P/E frente a H&M, Fast Retailing, AB Foods...]*
- **Sensibilidad:** *[tabla WACC vs. crecimiento terminal]*

## 5. Conclusión

*[Tu recomendación y qué te haría cambiar de opinión.]*

---

## Estructura del repositorio

```
analisis-inditex/
├── README.md              ← este resumen
├── requirements.txt       ← librerías de Python necesarias
├── data/
│   ├── raw/               ← datos descargados sin tocar
│   └── processed/         ← datos limpios / ratios calculados
├── notebooks/
│   ├── 01_descarga_datos.ipynb
│   └── 02_ratios_financieros.ipynb
├── src/                   ← funciones reutilizables
│   ├── datos.py
│   └── ratios.py
├── modelo/                ← modelo DCF en Excel
├── informe/               ← informe completo (plantilla + PDF final)
├── img/                   ← gráficos exportados
└── docs/                  ← guías y notas de trabajo
```

## Cómo reproducir el análisis

```bash
pip install -r requirements.txt
jupyter notebook
```

Ejecuta los notebooks en orden (01 → 02).

## Fuentes

- Inditex, Informes Anuales y presentaciones de resultados: <https://www.inditex.com/itxcomweb/es/es/accionistas-e-inversores>
- CNMV: <https://www.cnmv.es>
- Yahoo Finance (vía yfinance)
- Damodaran Online (primas de riesgo, betas sectoriales): <https://pages.stern.nyu.edu/~adamodar/>
