# 🚛 Análisis del Transporte de Mercancías por Carretera en España (2017–2024)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-data--analysis-brightgreen?logo=pandas)
![Tableau](https://img.shields.io/badge/Tableau‑Dashboard-orange?logo=tableau)

---

## 🧭 Descripción general

Este proyecto analiza los datos públicos del **Ministerio de Transportes, Movilidad y Agenda Urbana (MITMA)** a través del **Observatorio del Transporte y la Logística en España (OTLE)**.  
El objetivo es desarrollar una base de datos limpia, estructurada y coherente que permita **analizar el transporte de mercancías por carretera en España entre 2017 y 2024**, comprendiendo:

- Tendencias anuales y regionales del tráfico de mercancías.  
- Flujos entre comunidades autónomas.  
- Operaciones vacías y eficiencia del transporte.  
- Costes estructurales e índices de precios.  
- Superficie y capacidad logística disponible.

🔗 Fuente oficial de datos: [Portal OTLE / MITMA](https://otle.transportes.gob.es/)

---

## 📌 Alcance y limitaciones

### Alcance actual  
✔️ Limpieza y normalización de nueve datasets oficiales (2017–2024) del OTLE.  
✔️ Homogeneización de columnas, tipos y unidades (toneladas, toneladas‑kilómetro).  
✔️ Imputación controlada de nulos (`dimension_coste → indirectos`).  
✔️ Eliminación de registros inconsistentes o con valores clave vacíos.  
✔️ Preparación para análisis exploratorio (EDA) y visualización interactiva.

### Limitaciones  
⚠️ Esta versión no incluye aún el análisis visual completo, modelos predictivos ni correlaciones entre costes y eficiencia.  
⚠️ Las transformaciones se han limitado a limpieza y consistencia estructural; no se han empleado imputaciones estadísticas invasivas.  
⚠️ No se ha integrado todavía la comparación profunda entre modos de transporte (carretera vs. ferrocarril vs. marítimo).  
⚠️ Depende de las actualizaciones de origen: si el portal OTLE modifica o amplía datos en el futuro, podrían requerirse nuevas limpiezas.

Las siguientes fases del proyecto incorporarán la **unificación analítica** y los **dashboards de indicadores logísticos nacionales**.

---

## 📁 Datasets procesados

| Código | Descripción | Estado |
|--------|-------------|--------|
| CO280  | Tráfico total de mercancías (por tipo y desplazamiento) | ✅ Limpio |
| CO282  | Flujos nacionales entre comunidades autónomas | ✅ Limpio |
| CO285  | Operaciones en vacío (eficiencia) | ✅ Limpio |
| CO497  | Índice de precios del transporte | ✅ Limpio |
| CO516  | Superficie de instalaciones logísticas | ✅ Limpio |
| CO519  | Tráfico total por modo de transporte y tipo de tráfico | ✅ Limpio |
| CO597  | Transporte internacional (tn / tn·km) | ✅ Limpio |
| CO614  | Costes estructurales por tipo de vehículo | ✅ Limpio |
| IDL    | Índice de desempeño logístico | ✅ Limpio |

---

## ⚙️ Metodología de limpieza

1. **Carga y auditoría inicial**  
   - Lectura de archivos CSV (UTF‑8‑SIG).  
   - Revisión de estructura, tipos, nulos y duplicados.  

2. **Normalización de columnas**  
   - Nombres en minúsculas, sin espacios, consistentes entre datasets.  
   - Etiquetas uniformes (por ejemplo `recibido`, `expedido`).  

3. **Tratamiento de valores nulos**  
   - Eliminación de filas con `NaN` en variables fundamentales (pais, comunidad, tipo_transporte).  
   - Sustitución documentada (`dimension_coste → indirectos`).  

4. **Conversión y estandarización**  
   - Unificación de unidades en toneladas (tn) o toneladas‑kilómetro (tn·km).  
   - Conversión de la columna de año a tipo numérico.  

5. **Validación**  
   - Rango temporal detectado: _2017‑2024_.  
   - Comprobación de duplicados residuales.  
   - Verificación de imputaciones específicas.  

6. **Exportación final**  
   - Archivos codificados en **UTF‑8‑SIG**.  
   - Guardados en `data/processed/`.

---

## 📂 Estructura de proyecto

```
08_Transporte_Carretera_MITMA/
│
├─ data/
│ ├─ raw/ → Archivos CSV originales del MITMA
│ └─ processed/ → Dataset final limpio (CO280_trafico_toneladas_clean.csv)
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
|   └─ 05_analisis_parte_II.ipynb
│
├─ reports/
│ ├─ analisis_transporte_mercancias_carretera.pdf
│ └─ transporte_mercancias_carretera.ppbx
|
├─ dashboards/
│ └─ dashboard_tte_mercancias_carretera.pibx
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

## ▶️ Reproducibilidad

1. **Entorno** (ejemplo):
   ```bash
   python -m venv .venv
   source .venv/bin/activate       # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Ejecución de notebooks en orden**:
   - `01_exploracion_CO280.ipynb`
   - `02_limpieza_parte_I.ipynb`
   - `03_limpieza_parte_II.ipynb`
   - `04_analisis_parte_I.ipynb`
   - `05_analisis_parte_II.ipynb`

3. **Salida**:  
   Los archivos limpiados estarán disponibles en `data/processed/`, listos para importar en Tableau, Power BI u otra herramienta de visualización.

---

## 📊 Próxima fase analítica

- Serie temporal de toneladas y toneladas‑kilómetro (2017‑2024).  
- Comparativa entre comunidades autónomas y modos de transporte.  
- Cálculo del ratio **vacío / cargado** (CO285 vs CO280).  
- Análisis de relación: **índice de precios (CO497)** vs **costes estructurales (CO614)**.  
- Mapa nacional de infraestructura logística (CO516).  
- Generación de indicadores agregados por **IDL (Índice de Desempeño Logístico)**.

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
