# 🚛 Análisis del Transporte de Mercancías por Carretera en España (2017–2024)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-data--analysis-brightgreen?logo=pandas)
![Power BI](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Ready_for_Production-success)

---

## 🧭 Descripción general

Este proyecto analiza los datos públicos del **Ministerio de Transportes, Movilidad y Agenda Urbana (MITMA)** a través del **Observatorio del Transporte y la Logística en España (OTLE)**.

El objetivo principal es transformar microdatos administrativos dispersos y no estructurados en un ecosistema de **Inteligencia de Negocio (BI)** que permita responder preguntas estratégicas sobre:

* **Red y Flujos:** ¿Quién mueve qué y hacia dónde? (Matrices Origen-Destino).
* **Economía:** Análisis de márgenes, inflación de costes y elasticidad de precios.
* **Infraestructura (Real Estate):** Detección de zonas saturadas vs. oportunidades de inversión logística ($Ton/m^2$).
* **Competitividad:** Benchmarking internacional y balanza comercial.

🔗 Fuente oficial de datos: [Portal OTLE / MITMA](https://otle.transportes.gob.es/)

---

## 🎯 Alcance y Limitaciones

Para garantizar una interpretación correcta de los datos, se definen las siguientes fronteras del análisis:

### ✅ Alcance (Lo que SÍ incluye)
1.  **Ventana Temporal:** Serie histórica completa **2017-2024**, permitiendo análisis pre y post-pandemia.
2.  **Modo de Transporte:** Foco principal en **Transporte por Carretera** (el 95% del movimiento interior en España), con comparativas modales leves.
3.  **Granularidad Geográfica:**
    * *Flujos (Demanda):* Nivel Comunidad Autónoma (CCAA).
    * *Infraestructura (Oferta):* Nivel Provincia.
4.  **Dimensión Económica:** Estructura de costes desglosada por tipo de vehículo (Articulados, Rígidos, Frigoríficos) y evolución de precios de mercado.

### ⚠️ Limitaciones (Lo que NO incluye)
1.  **Ceguera de "Última Milla":** Los datos oficiales no trazan la distribución capilar urbana (e-commerce B2C dentro de ciudades). El análisis se centra en *Middle Mile* y *Long Haul*.
2.  **Asimetría Geo-Espacial:** No es posible calcular el "Centro de Gravedad" exacto de un almacén dentro de una provincia, ya que los flujos de carga solo se detallan a nivel regional (CCAA).
3.  **Anonimato de Operadores:** Los costes analizados son medias sectoriales del observatorio. No se dispone de datos financieros de empresas específicas (P&L privado).
4.  **Efecto 2020:** El año 2020 presenta anomalías estadísticas severas por el COVID-19; debe tratarse como un *outlier* en los modelos predictivos.

---

## 📁 Datasets procesados

| Código | Descripción |
|--------|-------------|
| CO280  | Tráfico total de mercancías (por tipo y desplazamiento) |
| CO282  | Flujos nacionales entre comunidades autónomas |
| CO285  | Operaciones en vacío (eficiencia) |
| CO497  | Índice de precios del transporte |
| CO516  | Superficie de instalaciones logísticas |
| CO519  | Tráfico total por modo de transporte y tipo de tráfico |
| CO597  | Transporte internacional (tn / tn·km) |
| CO614  | Costes estructurales por tipo de vehículo |
| KPI1   | KPI Costes vs Precios|
| KPI2   | KPI Cuota de Mercado |
| KPI3   | KPI Saturación Logística |
| KPI4   | KPI Costes Vehículos |
| KPI5   | KPI Precios Mercado |
| KPI6   | KPI Balanza Comercial |
| KPI7   | KPI Benchmarking LPI |
| IDL    | Índice de desempeño logístico |

---

## 🎯 Activos Generados (Datasets para Power BI)

Como resultado de la ejecución del pipeline, se han generado los siguientes archivos CSV en /data/processed/, listos para modelado en herramientas de visualización:

### ✅ Alcance (Lo que SÍ incluye)
1.  **KPI Cuota Mercado CCAA** Volumen total movido por región.
2.  **KPI_Costes_Historico_Vehiculos** Desglose detallado de costes opertivos por tipo de camión.
3.  **KPI_Precios_Mercado_Historico** Índice de referencia de precios de mercado (Base 100 = 2017).
4.  **KPI_Saturacion_Logistica_Historica** El KPI estratégico. Relación Ton/m2 histórica por comunidad.
5.  **KPI_Balanza_Comercial* Flujos de exportación vs importación
6.  **KPI_Benchmarking_LPI** Comparativa de desempeño logístico vs Europa.
7.  **KPI_Socios_Internacionales** Ranking de países con mayor intercambio comercial.

---

## ⚙️ Metodología: De Notebooks a Insights

| Fase | Notebook | Descripción Técnica | Insight de Negocio |
|------|-------------|--------|-------------|
| ETL  | 01_exploracion | Mapeo de columnas y auditoría de nulos.  | Validación de la integridad de los datos (2017-2024)|
| ETL  | 02_limpieza_I | Pivoteo de métricas (Ton vs Ton-Km) y limpieza de flujos O-D.  | Creación de la red logística nacional |
| ETL  | 03_limpieza_II | Desagregación de superficies (m2) y estandarización geográfica.  | Inventario de suelo logístico por provincia |
| KPI  | 04_analisis_I| Análisis de Demanda: Cálculo de cuotas de mercado por CCAA.  | "Identificación del ""Triángulo de Oro"" logístico." |
| KPI  | 05_analisis_II | Análisis Financiero: Comparativa Costes vs. Precios.  | "Detección del ""Margin Squeeze"" (Pérdida de rentabilidad 2022-24)." |
| KPI  | 06_analisis_III| Real Estate: Matriz de Saturación (Demanda / Oferta)  | Mapa de calor de oportunidades de inversión en almacenes. |
| KPI  | 07_analisis_IV | Internacional: Balanza comercial y LPI Benchmarking.  | Competitividad de España frente a Europa |

---

## 📂 Estructura de proyecto

```default []
08_Transporte_Carretera_MITMA/
│
├─ data/
│ ├─ raw/ → Archivos CSV originales del MITMA
│ └─ processed/
│   ├─ CO280_trafico_total_ccaa_tipo_desplaz_y_mercancia_clean.csv
│   ├─ CO282_flujos_ccaa_origen_destino_clean.csv
│   ├─ CO282_flujos_ccaa_ton_km_clean.csv
│   ├─ CO285_operaciones_vacio_clean.csv
│   ├─ CO497_indice_precios_clean.csv
│   ├─ CO516_superficies_logisticas_clean.csv
│   ├─ CO519_transporte_mercancias_por_modo_y_ambito.csv
│   ├─ CO597_transporte_mercancias_internacional.csv
│   ├─ CO614_costes_estructura_clean.csv
|   └─ indice_desempeno_logistico_clean
│
├─ notebooks/
|   ├─ 01_exploracion_CO280.ipynb
|   ├─ 02_limpieza_parte_I.ipynb
|   ├─ 03_limpieza_parte_II.ipynb
|   ├─ 04_analisis_parte_I.ipynb
|   ├─ 05_analisis_parte_II.ipynb
|   ├─ 06_analisis_parte_III.ipynb
|   └─ 07_analisis_parte_IV.ipynb
|
├─ src/
│ └─ limpieza.py
│
├─ reports/
│ ├─ analisis_transporte_mercancias_carretera.pdf
│ └─ transporte_mercancias_carretera.pptx
|
├─ dashboards/
│ └─ dashboard_tte_mercancias_carretera.pbix
|
├─ images/
│ ├─ portada.png
│ ├─ imagen1.png
│ ├─ imagen2.png
│ └─ imagen3.png
|
├─ requirements.txt
│
└─ README.md
```

---

## 🧾 Licencia de los datos

Los datos utilizados proceden del **Ministerio de Transportes, Movilidad y Agenda Urbana (MITMA)** – **Observatorio del Transporte y la Logística en España (OTLE)**,  
y se reutilizan conforme a su **Licencia de datos abiertos (LDA)**:  
👉 [https://www.transportes.gob.es/el-ministerio/buen-gobierno/licencia_datos](https://www.transportes.gob.es/el-ministerio/buen-gobierno/licencia_datos)

---

## 👩‍💻 Autora

**Elena Sánchez‑Laulhé Dégano**  
📍 Madrid, España  
🎓 Data Analytics Supply Chain & Logística  
📚 Proyecto educativo y de investigación
