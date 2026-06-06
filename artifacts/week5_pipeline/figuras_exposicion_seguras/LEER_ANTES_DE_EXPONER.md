# Figuras seguras para exposición

Carpeta:

`artifacts\week5_pipeline\figuras_exposicion_seguras`

## Figuras generadas

- `01_distribucion_clases_por_split.png`
- `02_porcentaje_clases_por_split.png`
- `03_resultado_leakage_interpretable.png`
- `04_comparacion_metricas_por_variante.png`
- `05_matriz_confusion_test_formal.png`
- `06_resumen_aciertos_errores_test_formal.png`


## Figuras retiradas de exposición

No se deben mostrar dashboards con estado global `FALLA`, barras vacías de leakage, conteos de `metrics_test.json = 0` ni gráfica de SHA256 con `before` faltante.

## Nota sobre control de dataset

No se grafica la huella SHA256 porque falta la huella inicial o no coincide. No se debe afirmar visualmente que la data no cambió.

## Frase correcta para exposición

Estas figuras muestran control experimental: distribución de clases, balance de splits, ausencia de leakage por imagen base, comparación de variantes y matriz de confusión del test formal.  
No se afirma validación clínica ni split por paciente, porque el dataset no contiene `patient_id`.
