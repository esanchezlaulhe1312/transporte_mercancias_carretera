# 🚛 Análisis del Transporte de Mercancías por Carretera en España (2017-2024)

## 🧭 Descripción general
Este proyecto analiza los datos abiertos del **Ministerio de Transportes y Movilidad Sostenible (MITMA)**, a través del **Observatorio del Transporte y la Logística en España (OTLE)**.  
Los datasets proceden del portal oficial de datos abiertos del MITMA:  
🔗 [https://otle.transportes.gob.es/](https://otle.transportes.gob.es/)

El objetivo es realizar una **exploración, limpieza y análisis visual** de los principales conjuntos de datos del transporte de mercancías por carretera en España, con el fin de identificar:

- Tendencias temporales (2017–2024)  
- Distribución territorial por comunidad autónoma  
- Eficiencia operativa (viajes vacíos vs cargados)  
- Costes, precios e infraestructura logística  

---

## 📁 Datasets utilizados

Los ficheros seleccionados para el análisis provienen del OTLE y abarcan distintas dimensiones del transporte de mercancías por carretera:

CO280_Trafico_Total_Merc_Veh_Espanyoles_Carr__CCAA_TipoMercancia_TipoDesplaz_Anyo.csv
CO282_CO281_Flujos_Nac_Merc_Veh_Espanyoles_Carr_entre_CCAAs_Anyo.csv
CO285_OperVacio_Veh_Espanyoles_Carr__CCAA_TipoDesplaz_Anyo.csv
CO497_indice_precios_TRM_Carr__tramosDistancias.csv
CO516_Superficie_Instalacs_Logistica_Carr__TipoInstalac_CCAA_Provincia.csv
CO519_Trafico_Total_Merc__ModoTransporte_TipoTrafico_Anyo.csv
CO597_CO598_TRM_int_CAR_Tn_TnKm_Merc_RecibExped_ESP__paises_OrigenDestino.csv
CO614_Coste_TRM_Carr__tipo_veh.csv

---

## 🧩 Estructura y resumen de los datasets

| Archivo | Filas | Columnas | Variables principales | Año / Variable temporal |
|----------|-------|-----------|------------------------|--------------------------|
| CO280 | 15 200 | 10 | year2, comunidad2, tipo_transporte3, tipo_desplazamiento, tipo_mercancia2, valor2 | year2 |
| CO282 | 3 600 | 5 | year, ComunidadOrigen, ComunidadDestino, Unidad, Valor | year |
| CO285 | 2 128 | 13 | comunidad, Estado_Operacion, year, Tipo_transporte, Valor | year |
| CO497 | 96 | 4 | year, tramo_distancia, concepto_precio, valor | year |
| CO516 | 10 402 | 17 | year, comunidad, provincia, tipo_instalacion, superficie | year |
| CO519 | 66 | 7 | year, TipoTrafico, ModoTransporte, valor | year |
| CO597 | 992 | 9 | Pais, tipo_desplazamiento, valor_toneladas, valor_toneladas_km | year |
| CO614 | 4 162 | 12 | vehiculo, tipo_coste_anual, super_tipo_costes, valor | year |

---

## ⚙️ Metodología

1. **Carga de datos:**  
   Lectura de los archivos CSV originales (UTF-8) descargados del OTLE.

2. **Auditoría inicial:**  
   Revisión de estructura, tipos de variables, valores nulos y duplicados.

3. **Limpieza y normalización:**  
   - Estandarización de nombres de columnas.  
   - Conversión de texto a minúsculas y eliminación de espacios.  
   - Transformación de unidades a **toneladas físicas**.  
   - Eliminación de filas agregadas (“total 2024”, “total 2023”…).  

4. **EDA (Exploratory Data Analysis):**  
   - Evolución del volumen total transportado (2017–2024).  
   - Ranking de comunidades autónomas.  
   - Distribución por tipo de mercancía, transporte y desplazamiento.  

5. **Exportación final:**  
   Dataset limpio: `CO280_trafico_toneladas_clean.csv`  
   Codificación: **UTF-8-SIG**

---

## 📊 Resultados clave

- **Periodo analizado:** 2017–2024  
- **Unidad principal:** Toneladas transportadas  
- **CCAA con mayor volumen:** Andalucía, Cataluña, Comunidad Valenciana  
- **Tendencia general:** Descenso temporal en 2020 (efecto COVID-19), con recuperación posterior.  
- **Predominio:** Transporte intrarregional y desplazamientos intermunicipales dentro de cada CCAA.  

---

## 📂 Estructura del proyecto

```
08_Transporte_Carretera_MITMA/
│
├─ data/
│ ├─ raw/ → Archivos CSV originales del MITMA
│ └─ processed/ → Dataset final limpio (CO280_trafico_toneladas_clean.csv)
│   ├─ CO280_trafico_toneladas_clean.csv
│   ├─ CO280_trafico_ton_km_clean.csv
│   ├─ CO282_flujos_ccaa_toneladas_clean.csv
│   ├─ CO282_flujos_ccaa_ton_km_clean.csv
│   ├─ CO285_operaciones_vacio_clean.csv
│   ├─ CO497_indice_precios_clean.csv
│   ├─ CO614_costes_estructura_anual_clean.csv
|   └─ CO614_costes_estructura_unitaria_clean.csv
│
├─ notebooks/
|   ├─ 01_exploracion_CO280.ipynb
|   ├─ 02_limpieza_parte_I.ipynb
|   └─ 02_limpieza_parte_II.ipynb
│
├─ reports/
│ ├─ Informe_CO280_Exploracion_Limpieza.pdf
│ └─ PPT.ppbx
|
├─ dashboards/
│ └─ dashboards.pibx
|
├─ requirements.txt
│
└─ README.md
```

---

## 🔮 Próximos pasos

- Integrar **CO285 (operaciones en vacío)** → análisis de eficiencia.  
- Incorporar **CO497** y **CO614** → análisis de costes e índices de precios.  
- Añadir **CO516** → infraestructura logística y superficie.  
- Unificar todos los ficheros en un modelo analítico completo del transporte por carretera.  
- Desarrollar dashboards interactivos en **Tableau** .

---

## 👩‍💻 Autor

**Elena Sánchez-Laulhé Dégano**  
📍 Madrid, España  
📚 Licencia: Uso educativo y de investigación.

---