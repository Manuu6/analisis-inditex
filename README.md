# Análisis y valoración de Inditex (ITX.MC)

> ⚠️ Ejercicio académico con fines formativos. **No es una recomendación de inversión.**

**Autor:** Manuel Pimentel · CUNEF Universidad
**Fecha del análisis:** _[dd/mm/aaaa]_
**Precio de referencia:** _[X,XX €]_ · **Precio objetivo:** _[X,XX €]_ · **Recomendación:** _[Comprar / Mantener / Vender]_

---

## 1. Resumen ejecutivo
_[3-5 líneas con tu tesis: qué opinas de la empresa y por qué. Escríbelo al final, cuando hayas terminado todo el análisis.]_

## 2. La empresa en 1 minuto
- **Qué hace:** _[diseño, fabricación, distribución y venta de moda]_
- **Marcas:** Zara, Pull&Bear, Massimo Dutti, Bershka, Stradivarius, Oysho, Zara Home, Lefties
- **Cómo gana dinero:** _[modelo de negocio, integración vertical, proximidad de la producción...]_
- **Ventajas competitivas:** _[...]_
- **Principales riesgos:** _[competencia de Shein/Temu, consumo, divisas, ...]_

## 3. Análisis financiero
_[Pega aquí los gráficos clave de `img/` y comenta en 2-3 frases cada uno.]_

| Métrica | Año 1 | Año 2 | Año 3 | Año 4 |
|---|---|---|---|---|
| Ventas (M€) | | | | |
| Margen bruto | | | | |
| Margen EBIT | | | | |
| ROE | | | | |
| Caja neta (M€) | | | | |

## 4. Valoración
- **DCF:** _[valor por acción y supuestos principales: crecimiento, márgenes, WACC, g]_
- **Múltiplos comparables:** _[EV/EBITDA y P/E frente a H&M, Fast Retailing, AB Foods...]_
- **Sensibilidad:** _[tabla WACC vs. crecimiento terminal]_

## 5. Conclusión
_[Tu recomendación y qué te haría cambiar de opinión.]_

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
- Inditex, Informes Anuales y presentaciones de resultados: https://www.inditex.com/itxcomweb/es/es/accionistas-e-inversores
- CNMV: https://www.cnmv.es
- Yahoo Finance (vía `yfinance`)
- Damodaran Online (primas de riesgo, betas sectoriales): https://pages.stern.nyu.edu/~adamodar/
