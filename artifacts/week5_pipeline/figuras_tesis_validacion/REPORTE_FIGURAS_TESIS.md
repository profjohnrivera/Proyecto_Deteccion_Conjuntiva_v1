# Reporte de figuras de validación para tesis

Carpeta generada:

`artifacts\week5_pipeline\figuras_tesis_validacion`

## Figuras generadas

### 1. 01_distribucion_clases_por_split_tesis.png

**Uso:** Demostrar que train, validation y test contienen ambas clases.

**Mensaje para exposición:** El dataset mantiene representación de Anemia y Normal en todos los subconjuntos.

### 2. 02_porcentaje_clases_por_split_tesis.png

**Uso:** Sustentar balance estadístico entre Anemia y Normal.

**Mensaje para exposición:** Las proporciones son cercanas entre clases, reduciendo riesgo de sesgo por clase dominante.

### 3. 03_auditoria_no_leakage_tesis.png

**Uso:** Mostrar que no se detectó repetición de imágenes entre train, val y test.

**Mensaje para exposición:** El resultado esperado es cero coincidencias. Esto fortalece la validez del test formal.

### 4. 04_metricas_clave_por_variante_tesis.png

**Uso:** Comparar Baseline, Var1 y Var2 sin sobrecargar la gráfica.

**Mensaje para exposición:** La comparación separa rendimiento global y sensibilidad sobre Anemia.

### 5. 05_heatmap_metricas_por_variante_tesis.png

**Uso:** Mostrar todas las métricas principales en una vista compacta.

**Mensaje para exposición:** Permite identificar qué variante prioriza desempeño global y cuál prioriza sensibilidad por clase.

### 6. 06_matriz_confusion_test_formal_tesis.png

**Uso:** Explicar errores críticos del modelo en el test formal.

**Mensaje para exposición:** En tamizaje, los falsos negativos de Anemia son el error más delicado.

### 7. 07_resumen_errores_tamizaje_tesis.png

**Uso:** Resumir los errores principales sin saturar la exposición.

**Mensaje para exposición:** El análisis no solo mira accuracy; prioriza el riesgo de falsos negativos.

### 8. 08_resumen_validacion_metodologica_tesis.png

**Uso:** Abrir o cerrar la exposición con una síntesis metodológica.

**Mensaje para exposición:** La validación fortalece la trazabilidad experimental, pero no reemplaza una validación clínica.



## Advertencias y control de consistencia

- La matriz de confusión coincide más con la variante 'Var2' (accuracy comparison=0.6877, accuracy matriz=0.6877).

## Frase recomendada para exposición

En esta etapa organicé la validación metodológica del experimento mediante figuras de balance, separación de datos, auditoría de leakage, comparación de variantes y análisis de errores en el test formal.  
El objetivo no fue solo mostrar accuracy, sino demostrar que el experimento tiene trazabilidad, control de datos y evidencia reproducible.

## Limitación obligatoria

No se debe afirmar validación clínica.  
No se debe afirmar split por paciente si el dataset no contiene `patient_id`.  
El sistema debe presentarse como prototipo experimental de apoyo al tamizaje, no como diagnóstico médico.
