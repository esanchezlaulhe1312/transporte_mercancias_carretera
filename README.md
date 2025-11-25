# Análisis del Transporte de Mercancías por Carretera en España (2017–2024)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Power BI](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Microsoft](https://img.shields.io/badge/Microsoft-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Executive Summary

- Sector analizado: transporte de mercancías por carretera en España (2017–2024)
- Stack: Python (ETL, KPIs) + Power BI (BI) + informes en Word/PPT.
- Resultado clave: se detecta un "margin squeeze" del -3,79% por crecimiento desigual de costes vs. precios, y zonas de alta saturación logística (Extremadura > 250 Ton/m²).
- Rol: diseño de KPIs, modelado de datos, visualización, interpretación de negocio y documentación completa.

---

## Vista Previa del Dashboard

<p align="center">
  <img src="images/dashboard/00.portada/00.portada.png" alt="Portada" width="800"/>
</p>
<p align="center">
  <img src="images/dashboard/01.panorama_general/01.Panorama_General.png" alt="Panorama General" width="700"/>
</p>
<p align="center">
  <img src="images/dashboard/02.analisis_economico/02.Analisis_Economico.png" alt="Análisis Económico" width="700"/>
</p>
<p align="center">
  <img src="images/dashboard/03.eficiencia_e_infraestructura/03.Eficiencia_e_Infraestructura.png" alt="Eficiencia e Infraestructura" width="700"/>
</p>
<p align="center">
  <img src="images/dashboard/04.competitividad_internacional/04.Competitividad_Internacional.png" alt="Competitividad Internacional" width="700"/>
</p>

> Dashboard interactivo desarrollado en Power BI para analizar **8 años de datos oficiales** (2017-2024) del Observatorio del Transporte y la Logística en España (MITMS). Incluye análisis de demanda, costes operativos, saturación de infraestructura logística y competitividad internacional.

**[Ver presentación completa del proyecto](reports/transporte_mercancias_carretera.pptx)**  
**[Leer informe técnico completo](reports/informe_final.pdf)**

---

## Descripción General

Este proyecto transforma microdatos administrativos del **Ministerio de Transportes y Movilidad Sostenible (MITMS)** en un ecosistema de **Inteligencia de Negocio (BI)** que permite responder preguntas estratégicas sobre el sector logístico español:

### Preguntas de Negocio Resueltas

- **Red y Flujos:** ¿Quién mueve qué y hacia dónde? (Matrices Origen-Destino entre comunidades autónomas)
- **Economía:** ¿Cómo evolucionan los márgenes del sector? ¿Existe presión inflacionaria en costes?
- **Infraestructura Logística:** ¿Dónde existen oportunidades de inversión en almacenes? (Ratio $Ton/m^2$)
- **Competitividad:** ¿Cómo se posiciona España frente a Europa en desempeño logístico?

**Fuente oficial de datos:** [Portal OTLE / MITMS](https://otle.transportes.gob.es/)

---

### El icono del mundo como guía narrativa del dashboard

Este proyecto utiliza un pequeño icono del mundo como **conductor visual** de la historia.  
Lo verás en los paneles donde se presentan insights clave o cambios de perspectiva dentro del análisis.

El objetivo no es decorativo: el icono actúa como un **narrador** que acompaña al usuario a lo largo del dashboard, reforzando el hilo conductor del proyecto y ayudando a identificar momentos importantes del análisis.

<div align="center">
  <img src="images/iconos/mundo_insight/insight_3.3.png" alt="Narrador del dashboard" width="180"/>
</div>

---

## Principales Insights

### 1️⃣ "Margin Squeeze" - Crisis de Rentabilidad del Sector

<p align="center">
  <img src="images/dashboard/02.analisis_economico/02.Analisis_Economico_Insight01.png" alt="Margin Squeeze" width="700"/>
</p>

<p align="center">
  <img src="images/dashboard/02.analisis_economico/02.Analisis_Economico_Insight02.png" alt="Margin Squeeze" width="700"/>
</p>

**Descubrimiento crítico:** Los costes operativos crecieron un **24,65%** desde 2017, mientras que los precios de mercado solo aumentaron un **23,27%**, generando un margen económico negativo del **-3,79%**.

**Drivers de coste identificados:**

- **Combustible:** 27,64% del coste total
- **Salarios:** 23,23% del coste total
- **Combinado:** 50,9% del coste operativo total

**Riesgo sistémico:** Este margen negativo es insostenible y previsiblemente conducirá a concentración empresarial y reducción de inversión en renovación de flotas.

---

### 2️⃣ Saturación Logística Desigual - Oportunidades de Inversión

<p align="center">
  <img src="images/dashboard/03.eficiencia_e_infraestructura/03.Eficiencia_e_Infraestructura_Insight01.png" alt="Mapa Saturación" width="700"/>
</p>

**Disparidad territorial extrema:**

- **Extremadura:** 253 Ton/m² (ratio crítico - infraestructura insuficiente)
- **Madrid:** 33 Ton/m² (sobrecapacidad instalada)
- **País Vasco/Cornisa Cantábrica:** >100 Ton/m² (demanda industrial alta + orografía limitante)

<p align="center">
  <img src="images/dashboard/03.eficiencia_e_infraestructura/03.Eficiencia_e_Infraestructura_Insight02.png" alt="Top 10 Saturación" width="700"/>
</p>

**Oportunidad estratégica:** Existe potencial de arbitraje logístico deslocalizando almacenaje desde zonas saturadas hacia zonas con capacidad disponible y buena conectividad (Castilla-La Mancha, Aragón).

**Insight adicional:** Las operaciones en vacío representan el **39,4%** del total nacional, evidenciando ineficiencias en la planificación de retornos con impacto directo en costes y emisiones.

<p align="center">
  <img src="images/dashboard/03.eficiencia_e_infraestructura/tooltip/03.Tooltip.png" alt="Tooltip Saturación" width="500"/>
</p>

---

### 3️⃣ Concentración Geográfica - El "Triángulo de Oro"

<p align="center">
  <img src="images/dashboard/01.panorama_general/01.Panorama_General_Insight02.png" alt="Concentración Geográfica" width="700"/>
</p>

**Tres comunidades concentran el 43,5% del volumen total:**

- Cataluña: 15,28%
- Andalucía: 14,11%
- Comunitat Valenciana: 14,11%

Esta concentración define un **"Triángulo de Oro"** logístico en el arco mediterráneo correlacionado con:

- Puertos de alta capacidad (Barcelona, Valencia, Algeciras)
- Densidad industrial (cinturón industrial catalán, polo químico Tarragona)
- Producción agroindustrial (Almería, Murcia, Valencia)

<p align="center">
  <img src="images/dashboard/01.panorama_general/01.Panorama_General_Insight03.png" alt="Panorama General" width="700"/>
</p>

---

### 4️⃣ Dependencia Modal - 98,86% Carretera

<p align="center">
  <img src="images/dashboard/01.panorama_general/01.Panorama_General_Insight01.png" alt="Distribución Modal" width="700"/>
</p>

**Hallazgo:** Solo el **1,38%** del tráfico se realiza por ferrocarril.

---

### 5️⃣ España: Líder en Puntualidad, Rezagada en Facilitación Aduanera

<p align="center">
  <img src="images/dashboard/04.competitividad_internacional/04.Competitividad_Internacional_Insight01.png" alt="LPI España" width="700"/>
</p>

**Francia concentra el 41% del volumen total de comercio exterior:**

- 29.000 toneladas expedidas (desde España)
- 23.000 toneladas recibidas (hacia España)

**Comparativa con otros socios:**

- Portugal: 24.000 toneladas (19%)
- Alemania: 13.000 toneladas (11%)
- Italia: 10.000 toneladas (8%)

**Riesgo sistémico:** Hiperconcentración genera vulnerabilidad ante cambios regulatorios franceses o conflictos laborales en infraestructuras de paso.

<p align="center">
  <img src="images/dashboard/04.competitividad_internacional/04.Competitividad_Internacional_Insight02.png" alt="Benchmarking LPI" width="700"/>
</p>

**Oportunidad de mejora:** Si España redujera los tiempos de despacho aduanero al nivel alemán, podría ganar 0,6 puntos en el LPI global, alcanzando potencialmente la 1ª posición europea.

---

### 6️⃣ Dependencia Comercial de Francia - Riesgo de Concentración

<p align="center">
  <img src="images/dashboard/04.competitividad_internacional/04.Competitividad_Internacional_Insight03.png" alt="Flujos Internacionales" width="700"/>
</p>

**Posicionamiento:** España ocupa la **posición 2 en el ranking global LPI** (Logistics Performance Index del Banco Mundial), pero con un perfil heterogéneo:

**Fortalezas:**

- **Puntualidad:** 4,10/5,00 - Supera a Francia (3,80) e Italia (3,40)
- **Trazabilidad:** 4,00/5,00 - En línea con estándares UE

**Debilidades:**

- **Aduanas:** 3,70/5,00 - Rezago respecto a Alemania (4,30) y Francia (4,10)
- **Transporte Internacional:** 3,70/5,00 - Penalizado por conectividad ferroviaria limitada

---

## Alcance y Limitaciones

### Alcance (Lo que SÍ incluye)

1. **Ventana Temporal:** Serie histórica completa **2017-2024**, permitiendo análisis pre y post-pandemia
2. **Modo de Transporte:** Foco principal en **Transporte por Carretera** (98% del movimiento interior)
3. **Granularidad Geográfica:**
    - *Flujos (Demanda):* Nivel Comunidad Autónoma (CCAA)
    - *Infraestructura (Oferta):* Nivel Provincia
4. **Dimensión Económica:** Estructura de costes desglosada por tipo de vehículo

### Limitaciones

1. **Análisis de emisiones**
2. **Efecto 2020** Año con anomalías estadísticas por COVID-19 (debe tratarse como outlier)

---

## 📊 Datasets Procesados

| Código | Descripción | Registros | Período |
|--------|-------------|-----------|---------|
| CO280  | Tráfico total de mercancías (por tipo y desplazamiento) | 15.200 | 2017-2024 |
| CO282  | Flujos nacionales entre comunidades autónomas | 8.800 | 2017-2024 |
| CO285  | Operaciones en vacío (eficiencia) | 1.728 | 2017-2024 |
| CO497  | Índice de precios del transporte | 480 | 2017-2024 |
| CO516  | Superficie de instalaciones logísticas | 3.816 | 2017 |
| CO519  | Tráfico total por modo de transporte | 240 | 2017-2024 |
| CO597  | Transporte internacional (tn / tn·km) | 1.920 | 2017-2024 |
| CO614  | Costes estructurales por tipo de vehículo | 3.360 | 2017-2024 |
| LPI    | Índice de desempeño logístico (Banco Mundial) | 32 | 2023 |

---

## KPIs Estratégicos Generados

Como resultado del pipeline ETL, se crearon **7 datasets maestros** listos para visualización en Power BI:

| KPI | Descripción | Insight de Negocio |
|-----|-------------|-------------------|
| **KPI_Cuota_Mercado_CCAA** | Volumen total movido por región | Identificación del "Triángulo de Oro" logístico |
| **KPI_Costes_Historico_Vehiculos** | Desglose de costes operativos por tipo de camión | Análisis de rentabilidad por segmento de flota |
| **KPI_Precios_Mercado_Historico** | Índice de precios (Base 100 = 2017) | Detección del fenómeno "Margin Squeeze" |
| **KPI_Saturacion_Logistica_Historico** | Relación Ton/m² por comunidad | Mapa de oportunidades de inversión inmobiliaria |
| **KPI_Balanza_Comercial** | Flujos exportación vs. importación | Dependencia de socios comerciales (Francia 41%) |
| **KPI_Benchmarking_LPI** | Desempeño logístico España vs. Europa | Fortalezas (puntualidad) y debilidades (aduanas) |
| **KPI_Socios_Internacionales** | Ranking de países por volumen comercial | Estrategia de diversificación geográfica |

---

## Metodología: De Notebooks a Insights

| Fase | Notebook | Descripción Técnica | Output Generado |
|------|----------|-------------------|-----------------|
| **ETL** | `01_exploracion` | Mapeo de columnas y auditoría de nulos | Validación integridad datos (2017-2024) |
| **ETL** | `02_limpieza_I` | Pivoteo de métricas (Ton vs Ton-Km) | Red logística nacional (CO280, CO282) |
| **ETL** | `03_limpieza_II` | Desagregación de superficies y estandarización geográfica | Inventario suelo logístico (CO516) |
| **KPI** | `04_analisis_I` | Cálculo cuotas de mercado por CCAA | KPI_Cuota_Mercado_CCAA.csv |
| **KPI** | `05_analisis_II` | Comparativa Costes vs. Precios | KPI_Costes_Historico + KPI_Precios_Mercado |
| **KPI** | `06_analisis_III` | Matriz Saturación (Demanda / Oferta) | KPI_Saturacion_Logistica_Historico.csv |
| **KPI** | `07_analisis_IV` | Balanza comercial y LPI Benchmarking | KPI_Balanza_Comercial + KPI_Benchmarking_LPI |

---

## Desafíos Técnicos Superados

### Error de Interpretación Conceptual - Tráfico Internacional

**El problema:** Durante el desarrollo, asumí que el dataset CO597 "Tráfico Internacional" se refería a **vehículos operando rutas transfronterizas** (ej: Madrid-París). Esta interpretación errónea llevó a diseñar visualizaciones que mezclaban conceptos de "comercio exterior" con "operaciones de vehículos".

**La realidad:** CO597 registra **flujos de mercancías** (toneladas expedidas y recibidas) entre España y Europa, NO clasifica vehículos por ámbito operativo.

**Impacto:** Afectó a dos páginas del dashboard:

**Panorama General:** Métrica "% Transporte Internacional" computaba incorrectamente (doble contabilidad)
**Competitividad Internacional:** Confusión entre balanza comercial y operaciones de vehículos

**Solución implementada:**

1. Rediseñé la página "Panorama General" eliminando la métrica errónea
2. Reestructuré "Competitividad Internacional" para enfocarse exclusivamente en comercio exterior (expediciones vs. importaciones)

**Lección aprendida:** En proyectos con datos administrativos complejos, la **validación semántica de las definiciones** es tan crítica como la limpieza técnica. Documentar asunciones conceptuales en fases tempranas previene rediseños costosos.

---

## Estructura del Proyecto

```
08_Transporte_Carretera_MITMS/
│
├── data/
│   ├── raw/                    # CSVs originales MITMS (no versionados)
│   └── processed/              # Datasets limpios para Power BI
│       ├── CO280_trafico_total_ccaa_clean.csv
│       ├── CO282_flujos_ccaa_origen_destino_clean.csv
│       ├── CO285_operaciones_vacio_clean.csv
│       ├── CO497_indice_precios_clean.csv
│       ├── CO516_superficies_logisticas_clean.csv
│       ├── CO519_transporte_por_modo_clean.csv
│       ├── CO597_transporte_internacional_clean.csv
│       ├── CO614_costes_estructura_clean.csv
│       ├── KPI_Cuota_Mercado_CCAA.csv
│       ├── KPI_Costes_Historico_Vehiculos.csv
│       ├── KPI_Precios_Mercado_Historico.csv
│       ├── KPI_Saturacion_Logistica_Historico.csv
│       ├── KPI_Balanza_Comercial.csv
│       ├── KPI_Benchmarking_LPI.csv
│       └── indice_desempeno_logistico_clean.csv
│
├── notebooks/
│   ├── 01_exploracion_CO280.ipynb
│   ├── 02_limpieza_parte_I.ipynb
│   ├── 03_limpieza_parte_II.ipynb
│   ├── 04_analisis_parte_I.ipynb
│   ├── 05_analisis_parte_II.ipynb
│   ├── 06_analisis_parte_III.ipynb
│   └── 07_analisis_parte_IV.ipynb
│
├── src/
│   └── limpieza.py              # Funciones reutilizables ETL
│
├── reports/
│   ├── analisis_transporte_mercancias_carretera.pdf
│   └── transporte_mercancias_carretera.pptx
│
├── dashboards/
│   ├── transporte_mercancias_carretera.pbix     # Power BI Workbook
│   └── QR_code_dashboard.jpg                     # QR para acceso rápido
│
├── images/
│   └── dashboard/
│       ├── 00.portada/
│       ├── 01.panorama_general/
│       ├── 02.analisis_economico/
│       ├── 03.eficiencia_e_infraestructura/
│       └── 04.competitividad_internacional/
│
├── requirements.txt
└── README.md
```

---

## Cómo Replicar este Proyecto

### Clonar el Repositorio

```bash
git clone https://github.com/esanchezlaulhe1312/transporte_mercancias_carretera.git
cd transporte_mercancias_carretera
```

### Crear Entorno Virtual (Python 3.10–3.12 recomendado)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
```

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Descargar Datos MITMS

Visita [Portal OTLE](https://otle.transportes.gob.es/) y descarga los CSVs correspondientes a los códigos CO280, CO282, CO285, CO497, CO516, CO519, CO597 y CO614 para el período 2017-2024. Colócalos en la carpeta `data/raw/`.

### Ejecutar Notebooks Secuencialmente

Abre Jupyter y ejecuta los notebooks en orden:

1. `01_exploracion_CO280.ipynb`
2. `02_limpieza_parte_I.ipynb`
3. `03_limpieza_parte_II.ipynb`
4. `04_analisis_parte_I.ipynb`
5. `05_analisis_parte_II.ipynb`
6. `06_analisis_parte_III.ipynb`
7. `07_analisis_parte_IV.ipynb`

### Abrir Dashboard en Power BI

Abre el archivo `dashboards/transporte_mercancias_carretera.pbix` con Power BI Desktop y conecta a los CSVs de la carpeta `data/processed/`.

### Cómo navegar el dashboard

- **01. Panorama General**  
  - Filtros: Año, CCAA, Ámbito, Tipo de Envío, Tipo de Mercancía.  
  - Úsalo para: ver la evolución del volumen total y detectar el "Triángulo de Oro" logístico.

- **02. Análisis Económico**  
  - Filtros: Año, Tipo de Vehículo, Categoría/Subcategoría/Tipo Coste, Índice de Precios según distancia(km).
  - Úsalo para: analizar la evolución de costes vs. precios y medir el "margin squeeze", determinar donde están los mayores costes y qué vehículos están asociados a un mayor coste por km

- **03. Eficiencia e Infraestructura**  
  - Filtros: Año, CCAA, Ámbito, Tipo de Infraestructura, Función de la Infraestructura
  - Úsalo para: mostrar % de operaciones en vacío, determinar cuáles son las zonas de mayor saturación logística (Ton/m²) e identificar oportunidades potenciales de inversión.

- **04. Competitividad Internacional**  
  - Filtros: Área, País, Tipo de Ennvío, Indicador  
  - Úsalo para: Distinguir en qué países España tiene mayor volúmen de exportaciones/importaciones y revisar en qué indicadores España es fuerte y en cuáles debe mejorar respecto a la media europea

---

## Tecnologías Utilizadas

- **Python 3.10–3.12 recomendado** Limpieza y procesamiento de datos

  - pandas >= 2.1,<3.0 (manipulación de datos)
  - numpy >= 1.26, < 2.0(cálculos numéricos)
  - matplotlib >= 3.8,< 4.0 (visualizaciones exploratorias)
  - seaborn >= 0.13, < 0.14 (visualizaciones estadísticas)

- **Power BI Desktop:** Visualización interactiva y storytelling

- **Git/GitHub:** Control de versiones

- **VS Code:** Entorno de desarrollo con extensiones Jupyter, Python

- **Microsoft PowerPoint:** Presentación ejecutiva del proyecto

- **Microsoft Word:** Informe técnico completo

---

## Contacto

**Elena Sánchez-Laulhé Dégano**  
Madrid, España  
[LinkedIn](https://www.linkedin.com/in/elena-sanchez-laulhe/)  
[GitHub](https://github.com/esanchezlaulhe1312)

---

### Cómo citar

Si deseas referenciar este trabajo, puedes citarlo como:

> Sánchez-Laulhé Dégano, E. (2025). *Análisis del Transporte de Mercancías por Carretera en España (2017–2024)*. Repositorio GitHub. URL: https://github.com/esanchezlaulhe1312/transporte_mercancias_carretera

---

## Licencia de los Datos

Los datos utilizados proceden del **Ministerio de Transportes y Movilidad Sostenible (MITMS)** – Observatorio del Transporte y la Logística en España (OTLE), y se reutilizan conforme a su **Licencia de Datos Abiertos (LDA)** *(actualización oficial 2024)*:

https://www.transportes.gob.es/el-ministerio/buen-gobierno/licencia_datos

---

## 🧾 Licencia del código

El código de este repositorio se distribuye bajo la **Licencia MIT**, una licencia permisiva que permite usar, modificar y redistribuir el software con muy pocas restricciones.

© 2025 Elena Sánchez-Laulhé – Licencia MIT

Puedes consultar el texto completo en el archivo [`LICENSE`](./LICENSE).

---

## Reconocimientos

Agradecimientos especiales al equipo del OTLE por mantener datasets de calidad y acceso público.

---

<p align="center">
  <strong>📚 Proyecto educativo y de investigación | 2025</strong>
</p>
