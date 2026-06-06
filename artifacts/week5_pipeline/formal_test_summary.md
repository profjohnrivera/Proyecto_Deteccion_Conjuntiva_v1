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
| Baseline | Imagen completa | OK | 0.7228070175438597 | 0.7177899499880924 | 0.7429318254560973 | 0.724290780141844 | 0.8652482269503546 | 0.5833333333333334 | 60 | 19 | 0 | 1.0 | 23.469475087742403 | 285 |
| Var1 | ROI con bbox real/label | OK | 0.7228070175438597 | 0.709037102131014 | 0.7690736513276463 | 0.720596926713948 | 0.5106382978723404 | 0.9305555555555556 | 10 | 69 | 0 | 1.0 | 16.777019649172168 | 285 |
| Var2 | YOLO ROI + clasificador ROI | OK | 0.8140350877192982 | 0.8139526290507335 | 0.8141821946169772 | 0.8139036643026005 | 0.8014184397163121 | 0.8263888888888888 | 25 | 28 | 0 | 1.0 | 51.68263824562656 | 285 |

## Mejor F1 macro

`Var2` con `f1_macro=0.8140` entrada=`YOLO ROI + clasificador ROI`

## Mejor recall de Anemia

`Baseline` con `recall_anemia=0.8652` entrada=`Imagen completa`

## Interpretación objetiva

- Para anemia, `recall_anemia` y `fn_anemia_as_normal` son críticos.
- Un falso negativo significa: etiqueta real `Anemia`, predicción `Normal`.
- Un resultado alto en `quick_mode=True` no debe presentarse como rendimiento final de tesis; solo valida el flujo.
- La prueba manual con `testImage` es demostrativa. La tabla formal comparable debe salir de `dataset_clean/test`.
