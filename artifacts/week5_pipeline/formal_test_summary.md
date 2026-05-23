# Resumen formal de resultados en TEST

## Regla metodológica

Los resultados de esta sección provienen del conjunto `test`. El conjunto `test` no se usa para entrenar, calibrar temperatura ni elegir umbral.

## Qué gráfico va dónde

| Tipo de gráfico | Datos usados | Uso correcto | Archivo esperado |
|---|---|---|---|
| Curva de entrenamiento | Train + validación por época | Evidenciar progreso y posible sobreajuste | `baseline_full/training_progress.png`, `roi_gt/training_progress.png` |
| Matriz de confusión | Test final | Evaluar errores finales | `*/confusion_matrix_test.png`, `yolo_e2e/confusion_matrix_e2e_test.png` |
| Comparación final | Test final | Comparar Baseline / Var1 / Var2 | `test_comparison_summary.png` |
| Muestra visual | Imágenes de ejemplo | Demostrar flujo end-to-end | `evidence_pack/08_sample_predictions/` |

## Tabla formal comparable

| experiment | input_type | status | accuracy | f1_macro | precision_macro | recall_macro | recall_anemia | recall_normal | fp_normal_as_anemia | fn_anemia_as_normal | detection_failures | detection_rate | ms_per_image | support_total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | Imagen completa | OK | 0.6982456140350877 | 0.697944395149364 | 0.6997177658942365 | 0.6986554373522458 | 0.7375886524822695 | 0.6597222222222222 | 49 | 37 | 0 | 1.0 | 44.76877894736837 | 285 |
| Var1 | ROI con bbox real/label | OK | 0.7333333333333333 | 0.7315852086844453 | 0.7379560572465229 | 0.732565011820331 | 0.6595744680851063 | 0.8055555555555556 | 28 | 48 | 0 | 1.0 | 30.095997894731177 | 285 |
| Var2 | YOLO ROI + clasificador ROI | OK | 0.6877192982456141 | 0.684675725065576 | 0.6934299122628036 | 0.6867612293144207 | 0.5957446808510638 | 0.7777777777777778 | 32 | 57 | 3 | 0.9894736842105263 | 90.33112561403853 | 285 |

## Mejor F1 macro

`Var1` con `f1_macro=0.7316` entrada=`ROI con bbox real/label`

## Mejor recall de Anemia

`Baseline` con `recall_anemia=0.7376` entrada=`Imagen completa`

## Interpretación objetiva

- Para anemia, `recall_anemia` y `fn_anemia_as_normal` son críticos.
- Un falso negativo significa: etiqueta real `Anemia`, predicción `Normal`.
- Un resultado alto en `quick_mode=True` no debe presentarse como rendimiento final de tesis; solo valida el flujo.
- La prueba manual con `testImage` es demostrativa. La tabla formal comparable debe salir de `dataset_clean/test`.
