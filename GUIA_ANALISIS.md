# 📊 GUÍA PASO A PASO: ANÁLISIS DE DATOS DE TRANSPORTE DE MERCANCÍAS

## 🎯 Objetivo

Esta guía proporciona un enfoque sistemático para extraer **la máxima información** de los 9 datasets limpios del proyecto de Transporte de Mercancías por Carretera en España (2017-2024).

---

## 📁 Datasets Disponibles

| Dataset | Descripción | Filas | Columnas Clave |
|---------|-------------|-------|----------------|
| **CO280** | Tráfico total por CCAA, tipo desplazamiento y mercancía | ~15,000 | año, ccaa, toneladas, tipo_mercancia |
| **CO282** | Flujos origen-destino entre comunidades | ~2,000 | año, ccaa_origen, ccaa_destino, toneladas |
| **CO285** | Operaciones en vacío (eficiencia) | ~2,000 | año, tipo_operacion, viajes |
| **CO497** | Índice de precios del transporte | ~30 | año, indice, valor |
| **CO516** | Superficie instalaciones logísticas | ~3,800 | año, ccaa, tipo_instalacion, superficie |
| **CO519** | Transporte por modo y ámbito | ~60 | año, modo_transporte, tipo_trafico, toneladas |
| **CO597** | Transporte internacional | ~400 | año, pais, toneladas, ton-km |
| **CO614** | Costes estructurales por vehículo | ~6,000 | año, tipo_vehiculo, dimension_coste, valor |
| **IDL** | Índice desempeño logístico | ~220 | año, pais, indicador, puntuacion |

---

## 📈 PASO 1: ANÁLISIS TEMPORAL (SERIES DE TIEMPO)

### 1.1 Evolución del Volumen Total

**Objetivos:**
- Identificar tendencias de crecimiento/decrecimiento
- Detectar estacionalidad y patrones cíclicos
- Identificar puntos de inflexión (ej: COVID-19)

**Análisis a realizar:**

```python
# Tráfico total por año
trafico_anual = df_co280.groupby('año')['toneladas'].sum()

# Calcular variación interanual
variacion = trafico_anual.pct_change() * 100

# Identificar año con mayor/menor tráfico
año_max = trafico_anual.idxmax()
año_min = trafico_anual.idxmin()

# Tasa de crecimiento compuesta anual (CAGR)
cagr = ((trafico_anual.iloc[-1] / trafico_anual.iloc[0]) ** (1/len(años)) - 1) * 100
```

**Visualizaciones recomendadas:**
- Gráfico de línea con tendencia
- Barras de variación interanual
- Análisis de decomposición de series temporales

### 1.2 Evolución por Modo de Transporte (CO519)

**Objetivos:**
- Analizar la cuota de mercado de cada modo
- Identificar cambios en preferencias modales
- Evaluar la competitividad del transporte por carretera

**KPIs a calcular:**
- Cuota de mercado por modo (%)
- Variación de cuota año a año
- Toneladas-kilómetro por modo (intensidad)

### 1.3 Evolución de Precios y Costes

**Objetivos:**
- Analizar inflación del sector transporte
- Relacionar precios con volumen (elasticidad)
- Identificar presión sobre márgenes

**Análisis:**
```python
# Inflación acumulada del transporte
inflacion = ((df_co497['valor'].iloc[-1] / df_co497['valor'].iloc[0]) - 1) * 100

# Elasticidad precio-demanda
elasticidad = variacion_volumen / variacion_precio
```

---

## 🗺️ PASO 2: ANÁLISIS GEOGRÁFICO

### 2.1 Tráfico por Comunidad Autónoma (CO280)

**Objetivos:**
- Identificar principales polos logísticos
- Calcular concentración geográfica
- Analizar especialización regional

**Métricas clave:**
```python
# Top CCAA por volumen
top_ccaa = df_co280.groupby('ccaa')['toneladas'].sum().sort_values(ascending=False)

# Índice de concentración (HHI - Herfindahl-Hirschman Index)
cuotas = top_ccaa / top_ccaa.sum()
hhi = (cuotas ** 2).sum() * 10000

# Curva de Lorenz / Coeficiente de Gini
from scipy import stats
gini = 1 - 2 * np.trapz(cuotas.cumsum(), dx=1/len(cuotas))
```

**Análisis adicionales:**
- Tráfico per cápita por CCAA (requiere datos de población)
- Tráfico por km² de territorio
- Especialización por tipo de mercancía

### 2.2 Matriz Origen-Destino (CO282)

**Objetivos:**
- Identificar principales corredores comerciales
- Calcular autosuficiencia regional
- Detectar dependencias logísticas

**Análisis clave:**

```python
# Crear matriz OD
matriz_od = df_co282.pivot_table(
    values='toneladas',
    index='ccaa_origen',
    columns='ccaa_destino'
)

# Tráfico interno vs externo por CCAA
trafico_interno = matriz_od.diagonal().sum()
trafico_total = matriz_od.sum().sum()
ratio_interno = (trafico_interno / trafico_total) * 100

# Top 10 rutas comerciales
top_rutas = df_co282.groupby(['ccaa_origen', 'ccaa_destino'])['toneladas'].sum().sort_values(ascending=False).head(10)

# Análisis de red (requiere NetworkX)
import networkx as nx
G = nx.from_pandas_edgelist(
    df_co282,
    source='ccaa_origen',
    target='ccaa_destino',
    edge_attr='toneladas'
)
centralidad = nx.degree_centrality(G)
```

### 2.3 Infraestructura Logística (CO516)

**Objetivos:**
- Mapear capacidad logística por región
- Identificar gaps de infraestructura
- Relacionar infraestructura con tráfico

**Métricas:**
```python
# Superficie total por CCAA y tipo
superficie_ccaa = df_co516.groupby(['CCAA', 'Tipo Instalación'])['Superficie(m2)'].sum()

# Densidad logística (m² por millón de toneladas)
# Combinar CO280 y CO516
densidad = superficie_total / trafico_total

# Identificar CCAA con déficit/superávit de infraestructura
ratio_esperado = superficie_total.mean() / trafico_total.mean()
gap = superficie_ccaa / trafico_ccaa - ratio_esperado
```

---

## 📦 PASO 3: ANÁLISIS SECTORIAL (MERCANCÍAS)

### 3.1 Distribución por Tipo de Mercancía (CO280)

**Objetivos:**
- Identificar sectores dominantes
- Analizar diversificación del tráfico
- Detectar tendencias sectoriales

**Análisis:**
```python
# Distribución por tipo de mercancía
dist_mercancia = df_co280.groupby('tipo_mercancia')['toneladas'].sum()

# Índice de concentración sectorial
# Evolución temporal por sector
evolucion_sectorial = df_co280.groupby(['año', 'tipo_mercancia'])['toneladas'].sum().unstack()

# Identificar sectores en crecimiento/declive
tasas_crecimiento = evolucion_sectorial.pct_change().mean()
```

### 3.2 Análisis por Tipo de Desplazamiento

**Categorías:**
- Tráfico interior (dentro de España)
- Tráfico de importación
- Tráfico de exportación
- Tráfico de tránsito

**KPIs:**
- Ratio importación/exportación
- Grado de apertura comercial
- Autosuficiencia por tipo de mercancía

---

## ⚡ PASO 4: ANÁLISIS DE EFICIENCIA

### 4.1 Operaciones en Vacío (CO285)

**Objetivo:** Medir la eficiencia operativa del transporte

**Métricas clave:**
```python
# Porcentaje de viajes en vacío
if 'tipo_operacion' in df_co285.columns:
    total_viajes = df_co285['viajes'].sum()
    viajes_vacio = df_co285[df_co285['tipo_operacion'] == 'Vacío']['viajes'].sum()
    pct_vacio = (viajes_vacio / total_viajes) * 100

# Evolución del ratio vacío/cargado
ratio_vacio = df_co285.groupby('año').apply(
    lambda x: x[x['tipo_operacion']=='Vacío']['viajes'].sum() /
              x[x['tipo_operacion']=='Cargado']['viajes'].sum()
)
```

**Impacto:**
- Costes adicionales por ineficiencia
- Emisiones de CO2 evitables
- Potencial de optimización

### 4.2 Eficiencia Logística por CCAA

**Índice compuesto:**
```python
# Eficiencia = Tráfico / Superficie logística
eficiencia_ccaa = (trafico_por_ccaa / superficie_por_ccaa) * 1000

# Normalizar a escala 0-100
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 100))
indice_eficiencia = scaler.fit_transform(eficiencia_ccaa.values.reshape(-1, 1))
```

---

## 🌍 PASO 5: ANÁLISIS INTERNACIONAL

### 5.1 Comercio Exterior (CO597)

**Objetivos:**
- Identificar principales socios comerciales
- Analizar balanza comercial de transporte
- Evaluar integración europea

**Análisis:**
```python
# Top 10 países por volumen
top_paises = df_co597.groupby('pais')['toneladas(miles)'].sum().sort_values(ascending=False).head(10)

# Balanza comercial por país
balanza = df_co597.pivot_table(
    values='toneladas(miles)',
    index='pais',
    columns='desplazamiento',
    aggfunc='sum'
)
balanza['saldo'] = balanza['Expedido'] - balanza['Recibido']

# Intensidad del comercio (ton·km / toneladas)
df_co597['intensidad'] = df_co597['ton-km(millones)'] / df_co597['toneladas(miles)']
# Valores altos indican mayor distancia media
```

### 5.2 Comparación con Índice LPI (IDL)

**Objetivos:**
- Benchmarking internacional
- Identificar fortalezas/debilidades de España
- Priorizar áreas de mejora

**Análisis:**
```python
# Posición relativa de España
ranking_lpi = df_lpi[df_lpi['Indicador'] == 'Índice global de desempeño logístico (LPI)']
ranking = ranking_lpi.groupby('País')['Puntuación'].mean().sort_values(ascending=False)

# Análisis por dimensiones
dimensiones_españa = df_lpi[df_lpi['País'] == 'España'].groupby('Indicador')['Puntuación'].mean()

# Gap vs mejor país por dimensión
mejor_por_dimension = df_lpi.groupby('Indicador')['Puntuación'].max()
gap_españa = mejor_por_dimension - dimensiones_españa
```

---

## 🔗 PASO 6: ANÁLISIS MULTIVARIADO Y CORRELACIONES

### 6.1 Matriz de Correlación

**Variables a correlacionar:**
- Tráfico vs Infraestructura logística
- Precios vs Volumen (elasticidad)
- Costes vs Eficiencia operativa
- LPI vs Volumen de comercio exterior

**Implementación:**
```python
import seaborn as sns

# Crear dataset consolidado
df_consolidado = pd.merge(trafico_por_ccaa, superficie_por_ccaa, on='ccaa')
df_consolidado = pd.merge(df_consolidado, eficiencia_por_ccaa, on='ccaa')

# Matriz de correlación
corr_matrix = df_consolidado.corr()

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
```

### 6.2 Análisis de Regresión

**Modelos sugeridos:**

```python
from sklearn.linear_model import LinearRegression
from scipy import stats

# Modelo 1: Tráfico ~ Infraestructura + Población + PIB
# Modelo 2: Precios ~ Volumen + Costes_combustible
# Modelo 3: Eficiencia ~ Inversión_infraestructura + Tecnología

# Ejemplo: Relación tráfico-infraestructura
X = superficie_ccaa.values.reshape(-1, 1)
y = trafico_ccaa.values

model = LinearRegression()
model.fit(X, y)

r2 = model.score(X, y)
print(f"R² = {r2:.3f}")
print(f"Ecuación: Tráfico = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Superficie")
```

---

## 📊 PASO 7: ANÁLISIS DE COSTES

### 7.1 Estructura de Costes (CO614)

**Dimensiones del coste:**
- Costes fijos vs variables
- Costes por tipo de vehículo
- Evolución temporal de componentes

**Análisis:**
```python
# Distribución de costes por dimensión
if 'dimension_coste' in df_co614.columns:
    dist_costes = df_co614.groupby('dimension_coste')['valor'].sum()
    dist_costes_pct = (dist_costes / dist_costes.sum()) * 100

# Evolución del coste total
coste_total_anual = df_co614.groupby('año')['valor'].sum()

# Coste por tonelada transportada
# Combinar CO614 con CO280
coste_por_tonelada = coste_total_anual / trafico_anual
```

### 7.2 Relación Precios-Costes

**Objetivo:** Analizar márgenes y presión competitiva

```python
# Normalizar series a base 100
precios_norm = (df_co497.groupby('año')['valor'].mean() / df_co497['valor'].iloc[0]) * 100
costes_norm = (coste_total_anual / coste_total_anual.iloc[0]) * 100

# Calcular gap precios-costes
gap = precios_norm - costes_norm
# Gap positivo = mejora de márgenes
# Gap negativo = presión sobre márgenes
```

---

## 🎯 PASO 8: ANÁLISIS PREDICTIVO (OPCIONAL)

### 8.1 Forecasting de Tráfico

**Técnicas sugeridas:**

1. **ARIMA / SARIMA**
```python
from statsmodels.tsa.arima.model import ARIMA

# Ajustar modelo ARIMA
model = ARIMA(trafico_anual, order=(1,1,1))
results = model.fit()

# Predicción 2025-2027
forecast = results.forecast(steps=3)
```

2. **Prophet (Facebook)**
```python
from prophet import Prophet

df_prophet = pd.DataFrame({
    'ds': pd.to_datetime(trafico_anual.index, format='%Y'),
    'y': trafico_anual.values
})

model = Prophet()
model.fit(df_prophet)
future = model.make_future_dataframe(periods=3, freq='Y')
forecast = model.predict(future)
```

3. **Regresión con variables exógenas**
```python
# Incluir predictores: PIB, precio combustible, índice industrial
from sklearn.ensemble import RandomForestRegressor

X = df_predictores[['pib', 'precio_combustible', 'ind_industrial']]
y = trafico_anual

model = RandomForestRegressor()
model.fit(X, y)
```

### 8.2 Clustering de CCAA

**Objetivo:** Segmentar regiones por perfil logístico

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Variables para clustering
features = df_consolidado[['trafico_total', 'superficie_logistica',
                          'ratio_interno', 'eficiencia']]

# Normalizar
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-Means
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(features_scaled)

df_consolidado['cluster'] = clusters
```

**Interpretación de clusters:**
- Cluster 1: Grandes hubs logísticos (alta infraestructura + alto tráfico)
- Cluster 2: Regiones de paso (alto tráfico externo, baja infraestructura)
- Cluster 3: Regiones autosuficientes (alto tráfico interno)
- Cluster 4: Regiones periféricas (bajo tráfico + baja infraestructura)

---

## 📉 PASO 9: ANÁLISIS DE IMPACTO COVID-19

### 9.1 Comparación Pre/Post Pandemia

**Períodos:**
- Pre-COVID: 2017-2019
- COVID: 2020-2021
- Recuperación: 2022-2024

**Análisis:**
```python
# Impacto por CCAA
pre_covid = df_co280[df_co280['año'].isin([2017,2018,2019])].groupby('ccaa')['toneladas'].mean()
covid = df_co280[df_co280['año'].isin([2020,2021])].groupby('ccaa')['toneladas'].mean()
post_covid = df_co280[df_co280['año'].isin([2022,2023,2024])].groupby('ccaa')['toneladas'].mean()

# Calcular caída y recuperación
caida = ((covid - pre_covid) / pre_covid) * 100
recuperacion = ((post_covid - covid) / covid) * 100

# Identificar CCAA más/menos afectadas
ccaa_mas_afectada = caida.idxmin()
ccaa_menos_afectada = caida.idxmax()
```

### 9.2 Cambios Estructurales

**Hipótesis a validar:**
- ¿Aumentó el e-commerce y la logística de distribución?
- ¿Se redujo el tráfico internacional?
- ¿Cambió la distribución modal?

```python
# Comparar estructura de mercancías
estructura_pre = df_co280[df_co280['año']<2020].groupby('tipo_mercancia')['toneladas'].sum()
estructura_post = df_co280[df_co280['año']>=2022].groupby('tipo_mercancia')['toneladas'].sum()

cambio_estructural = ((estructura_post / estructura_pre) - 1) * 100
```

---

## 📊 PASO 10: GENERACIÓN DE KPIs Y DASHBOARDS

### 10.1 KPIs Principales

**Operativos:**
- Volumen total anual (toneladas)
- Toneladas-kilómetro (intensidad del transporte)
- Ratio de operaciones en vacío (%)
- Utilización de capacidad logística (%)

**Económicos:**
- Índice de precios del transporte (base 100)
- Coste medio por tonelada (€/ton)
- Coste medio por tonelada-kilómetro (€/ton·km)
- Margen precio-coste (%)

**Geográficos:**
- Concentración geográfica (HHI)
- Tráfico per cápita por CCAA (ton/habitante)
- Densidad logística (m²/millón toneladas)
- Índice de eficiencia logística por CCAA

**Internacionales:**
- Volumen de comercio exterior (toneladas)
- Saldo comercial de transporte (expedido - recibido)
- LPI España vs promedio europeo
- Cuota de mercado por país socio (%)

**Ambientales:**
- Emisiones evitables por viajes en vacío (ton CO2)
- Intensidad de carbono (kg CO2/ton·km)

### 10.2 Estructura de Dashboard

**Panel 1: Vista General**
- KPI cards: volumen total, variación anual, TOP 3 CCAA
- Gráfico de línea: evolución temporal del tráfico
- Mapa de España: choropleth por volumen de tráfico

**Panel 2: Análisis Geográfico**
- Ranking de CCAA por tráfico
- Matriz origen-destino (heatmap)
- Mapa de flujos principales (sankey diagram)

**Panel 3: Análisis Sectorial**
- Distribución por tipo de mercancía (treemap)
- Evolución sectorial (stacked area chart)
- Análisis de concentración

**Panel 4: Eficiencia y Costes**
- Ratio de operaciones en vacío
- Evolución de precios vs costes
- Ranking de eficiencia por CCAA

**Panel 5: Internacional**
- Top 10 países socios
- Balanza comercial
- Comparación LPI (radar chart)

---

## 🛠️ HERRAMIENTAS RECOMENDADAS

### Análisis Estadístico
- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **scipy**: Pruebas estadísticas
- **statsmodels**: Modelos econométricos

### Visualización
- **matplotlib**: Gráficos básicos
- **seaborn**: Gráficos estadísticos
- **plotly**: Gráficos interactivos
- **folium**: Mapas geográficos

### Machine Learning
- **scikit-learn**: Clustering, regresión
- **prophet**: Forecasting
- **networkx**: Análisis de redes

### Dashboards
- **Tableau**: Dashboards empresariales
- **Power BI**: Integración con Microsoft
- **Streamlit**: Dashboards en Python
- **Dash (Plotly)**: Dashboards web interactivos

---

## ✅ CHECKLIST DE ANÁLISIS COMPLETO

### Análisis Temporal
- [ ] Evolución del volumen total 2017-2024
- [ ] Variaciones interanuales
- [ ] Impacto COVID-19
- [ ] Tendencias por modo de transporte
- [ ] Evolución de precios y costes

### Análisis Geográfico
- [ ] Ranking de CCAA por tráfico
- [ ] Concentración geográfica (HHI, Gini)
- [ ] Matriz origen-destino
- [ ] Top 10 rutas comerciales
- [ ] Tráfico interno vs externo por región
- [ ] Mapa de infraestructura logística

### Análisis Sectorial
- [ ] Distribución por tipo de mercancía
- [ ] Evolución sectorial temporal
- [ ] Concentración sectorial
- [ ] Análisis por tipo de desplazamiento

### Análisis de Eficiencia
- [ ] Ratio de operaciones en vacío
- [ ] Índice de eficiencia por CCAA
- [ ] Utilización de infraestructura
- [ ] Ratio tráfico/superficie logística

### Análisis Internacional
- [ ] Top 10 países socios
- [ ] Balanza comercial por país
- [ ] Intensidad del comercio (ton·km/ton)
- [ ] Comparación LPI España vs Europa
- [ ] Fortalezas y debilidades por dimensión LPI

### Análisis Multivariado
- [ ] Correlación tráfico-infraestructura
- [ ] Elasticidad precio-demanda
- [ ] Regresión predictiva
- [ ] Clustering de CCAA

### Análisis de Costes
- [ ] Estructura de costes por dimensión
- [ ] Evolución de coste total
- [ ] Coste por tonelada
- [ ] Gap precios-costes

### Visualizaciones
- [ ] Serie temporal del tráfico
- [ ] Mapas coropléticos por CCAA
- [ ] Heatmap matriz origen-destino
- [ ] Radar chart LPI
- [ ] Sankey diagram de flujos
- [ ] Dashboard interactivo completo

### Outputs
- [ ] Notebook Jupyter con análisis completo
- [ ] Informe ejecutivo en PDF
- [ ] Dashboard interactivo
- [ ] Dataset consolidado de KPIs
- [ ] Presentación de resultados (PPT)

---

## 📚 REFERENCIAS Y RECURSOS

### Documentación Oficial
- [Portal OTLE / MITMA](https://otle.transportes.gob.es/)
- [Logistics Performance Index (World Bank)](https://lpi.worldbank.org/)
- [Eurostat - Transport Statistics](https://ec.europa.eu/eurostat/web/transport)

### Metodologías
- Análisis de series temporales: Box-Jenkins (ARIMA)
- Análisis de redes: Teoría de grafos
- Clustering: K-Means, DBSCAN, Hierarchical
- Índices de concentración: HHI, Gini, Theil

### Benchmarks Internacionales
- European Logistics Indicators (ELI)
- Transport Performance Indicators (TPI)
- Supply Chain Performance Indicators

---

## 💡 CONCLUSIÓN

Este análisis exhaustivo permite:

1. **Comprender la evolución** del sector logístico español (2017-2024)
2. **Identificar patrones** geográficos, sectoriales y temporales
3. **Medir eficiencia** operativa y uso de infraestructura
4. **Benchmarking** con países europeos
5. **Detectar oportunidades** de optimización y mejora
6. **Generar insights** para toma de decisiones estratégicas

**Próximos pasos sugeridos:**
- Integrar datos de PIB regional para análisis económico
- Añadir datos de población para calcular tráfico per cápita
- Incorporar datos de combustibles para análisis ambiental
- Desarrollar modelos predictivos para proyecciones 2025-2030
- Crear dashboard interactivo para stakeholders

---

**📌 NOTA**: Para ejecutar el análisis completo, utiliza el notebook `04_analisis_completo_guia.ipynb` que contiene todo el código implementado paso a paso.
