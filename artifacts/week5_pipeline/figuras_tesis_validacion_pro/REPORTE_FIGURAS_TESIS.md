# Reporte de figuras de validación para tesis

Carpeta generada:

`artifacts\week5_pipeline\figuras_tesis_validacion_pro`

## Figuras generadas

### 1. 01_distribucion_clases_por_subconjunto_tesis.png

**Uso:** Mostrar que los tres subconjuntos contienen representación de ambas clases.

**Mensaje para exposición:** En esta figura presento el conteo absoluto por clase y por subconjunto, lo que permite verificar cobertura en train, validation y test.

### 2. 02_proporcion_clases_por_subconjunto_tesis.png

**Uso:** Sustentar que el dataset se mantiene balanceado entre clases.

**Mensaje para exposición:** Aquí verifico que la proporción de Anemia y Normal se mantiene cercana en train, validation y test, reduciendo el riesgo de sesgo por clase dominante.

### 3. 03_auditoria_separacion_y_no_leakage_tesis.png

**Uso:** Mostrar la ausencia de repetición de imágenes entre train, validation y test.

**Mensaje para exposición:** En esta auditoría verifiqué que no existan coincidencias por imagen base entre los subconjuntos, lo que fortalece la validez del test formal.

### 4. 04_metricas_principales_por_variante_tesis.png

**Uso:** Comparar el rendimiento de Baseline, Var1 y Var2 con una lectura clara.

**Mensaje para exposición:** En esta figura resumo las métricas principales por variante para identificar el mejor equilibrio entre desempeño global y sensibilidad frente a la clase Anemia.

### 5. 05_heatmap_metricas_por_variante_tesis.png

**Uso:** Presentar todas las métricas principales en una sola visualización comparativa.

**Mensaje para exposición:** Con este mapa de calor sintetizo el comportamiento integral de cada variante y facilito la comparación global.

### 6. 06_matriz_confusion_test_formal_tesis.png

**Uso:** Analizar con detalle los aciertos y errores del modelo en el test formal.

**Mensaje para exposición:** La matriz de confusión me permite identificar no solo el nivel de acierto, sino también el tipo de error, especialmente los falsos negativos de Anemia.

### 7. 07_resumen_errores_test_formal_tesis.png

**Uso:** Resumir el comportamiento del modelo con énfasis en el riesgo de error.

**Mensaje para exposición:** En esta figura sintetizo los aciertos, errores, falsos negativos y falsos positivos para interpretar mejor el desempeño del sistema.

### 8. 08_panel_ejecutivo_validacion_tesis.png

**Uso:** Abrir o cerrar la exposición con una síntesis ejecutiva del experimento.

**Mensaje para exposición:** En este panel resumo los principales hallazgos metodológicos del experimento: separación de datos, balance, auditoría de leakage y desempeño formal en test.



## Advertencias y control de consistencia

- Sin advertencias críticas detectadas.

## Orden recomendado para exposición

1. `08_panel_ejecutivo_validacion_tesis.png`
2. `02_proporcion_clases_por_subconjunto_tesis.png`
3. `03_auditoria_separacion_y_no_leakage_tesis.png`
4. `04_metricas_principales_por_variante_tesis.png`
5. `06_matriz_confusion_test_formal_tesis.png`
6. `07_resumen_errores_test_formal_tesis.png`

## Frase recomendada para sustentación

En esta etapa organicé la validación metodológica del experimento mediante figuras que sintetizan la separación del dataset, el balance de clases, la auditoría de leakage, la comparación formal de variantes y el análisis de errores sobre el test formal.  
Mi objetivo no fue limitarme a reportar accuracy, sino demostrar que el experimento tiene trazabilidad, control de datos y evidencia reproducible.

## Precisión metodológica obligatoria

No corresponde afirmar validación clínica.  
No corresponde afirmar separación por paciente si el dataset no contiene `patient_id`.  
El sistema debe presentarse como prototipo experimental de apoyo al tamizaje y no como diagnóstico médico.
