# Semana 5 - Pipeline Anemia por Conjuntiva

## Objetivo

Pipeline reproducible para comparar máximo 2-3 variantes contra un baseline:

1. **Baseline**: imagen completa → EfficientNet-B0.
2. **Var 1**: ROI usando bounding box real del label → EfficientNet-B0.
3. **Var 2**: YOLO detecta ROI → EfficientNet-B0. Evaluación end-to-end estricta.

## Mapeo contra entregables de Semana 5

| requisito_docente | evidencia | estado |
| --- | --- | --- |
| Experimentos A/B máx. 2-3 variantes vs baseline | Baseline / Var1 / Var2 | Cumplido |
| Documentar logs | pipeline_progress.md, history.csv, resultados YOLO | Cumplido |
| Tabla estándar comparable | comparison_results.csv | Cumplido |
| 1 gráfico clave | confusion_matrix_test.png y confusion_matrix_e2e_test.png | Cumplido |
| Feature set y pipeline | 03_pipeline_diagram.md y 04_experiment_cards.md | Cumplido |
| Fit solo en train | train_tf con augmentación; eval_tf sin augmentación | Cumplido |
| Cero leakage y split correcto | split_leakage_audit.json | Cumplido por imagen base |
| Validación | Holdout train/val/test; val calibra; test solo evalúa | Cumplido |
| README en branch | README_semana5.md | Listo para subir a GitHub |
| Muestra de salida | evidence_pack/08_sample_predictions | Cumplido |

## Configuración usada

- `data_yaml`: `data_clean.yaml`
- `quick_mode`: `False`
- `yolo_epochs`: `10`
- `classifier_epochs`: `40`
- `freeze_backbone`: `False`
- `loss`: `FocalLoss`
- `threshold`: elegido solo con validación.
- `temperature scaling`: calibrado solo con validación.
- `fail_on_leakage`: `True`
- `require_clean_yaml`: `True`
- `yolo_imgsz`: `416`
- `yolo_batch`: `2`
- `yolo_workers`: `0`
- `yolo_fraction`: `1.0`

## Reglas anti-leakage

- Train usa aumentación.
- Val/Test no usan aumentación.
- Test no se usa para calibrar temperatura.
- Test no se usa para elegir umbral.
- Se genera `split_leakage_audit.json` para revisar imágenes base repetidas entre splits.
- El pipeline se detiene si detecta leakage y `fail_on_leakage=True`.

## Resultados comparables

| experiment | input_type | status | accuracy | f1_macro | precision_macro | recall_macro | recall_anemia | recall_normal | fp_normal_as_anemia | fn_anemia_as_normal | detection_failures | detection_rate | ms_per_image | support_total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | Imagen completa | OK | 0.7228070175438597 | 0.7177899499880924 | 0.7429318254560973 | 0.724290780141844 | 0.8652482269503546 | 0.5833333333333334 | 60 | 19 | 0 | 1.0 | 23.469475087742403 | 285 |
| Var1 | ROI con bbox real/label | OK | 0.7228070175438597 | 0.709037102131014 | 0.7690736513276463 | 0.720596926713948 | 0.5106382978723404 | 0.9305555555555556 | 10 | 69 | 0 | 1.0 | 16.777019649172168 | 285 |
| Var2 | YOLO ROI + clasificador ROI | OK | 0.8140350877192982 | 0.8139526290507335 | 0.8141821946169772 | 0.8139036643026005 | 0.8014184397163121 | 0.8263888888888888 | 25 | 28 | 0 | 1.0 | 51.68263824562656 | 285 |

## Muestra de salida end-to-end

| sample_id | image | true_label | true_name | status | prediction_id | prediction_name | prob_anemia | prob_normal | threshold_anemia | yolo_conf | bbox_xyxy | correct | output_image | message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\104_png.rf.09385316752ae2230e31961fd5a03f52.jpg | 0 | Anemia | OK | 1 | Normal | 0.04300401732325554 | 0.9569960236549377 | 0.5500000000000003 | 0.2232915461063385 | [560, 1037, 934, 1179] | False | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_01_true_Anemia_104_png.rf.09385316752ae2230e31961fd5a03f52.png |  |
| 2 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\104_png.rf.9fe670b02ab3e4b9e796743b0877948b.jpg | 0 | Anemia | OK | 1 | Normal | 0.04672837629914284 | 0.9532716274261475 | 0.5500000000000003 | 0.22574368119239807 | [559, 1035, 931, 1178] | False | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_02_true_Anemia_104_png.rf.9fe670b02ab3e4b9e796743b0877948b.png |  |
| 3 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\10_png.rf.44e757574c6aa5d39c383ca15bf1b463.jpg | 1 | Normal | OK | 1 | Normal | 0.1576940417289734 | 0.8423060178756714 | 0.5500000000000003 | 0.22880439460277557 | [978, 942, 1284, 1085] | True | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_03_true_Normal_10_png.rf.44e757574c6aa5d39c383ca15bf1b463.png |  |
| 4 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\10_png.rf.481d60386b20fedcbf73c0e0bcba208f.jpg | 1 | Normal | OK | 1 | Normal | 0.1534324735403061 | 0.8465675115585327 | 0.5500000000000003 | 0.2354203164577484 | [974, 942, 1281, 1087] | True | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_04_true_Normal_10_png.rf.481d60386b20fedcbf73c0e0bcba208f.png |  |

## Archivos generados

- `comparison_results.csv`
- `formal_test_summary.md`
- `test_comparison_summary.png`
- `split_leakage_audit.json`
- `pipeline_progress.md`
- `pipeline_progress.json`
- `baseline_full/history.csv`
- `baseline_full/training_progress.png`
- `roi_gt/history.csv`
- `roi_gt/training_progress.png`
- `*/test_metrics.json`
- matrices de confusión en PNG.
- `evidence_pack/` con evidencias organizadas para exposición.

## Nota objetiva sobre YOLO

Si `data.yaml` tiene clases YOLO `Anemia/Normal`, YOLO no está funcionando como detector puro de conjuntiva, sino como detector con clase diagnóstica. En este pipeline se usa su caja como ROI y el diagnóstico final lo decide EfficientNet. Para un diseño metodológicamente más limpio, YOLO debería tener una sola clase: `conjuntiva`.

## Nota objetiva sobre `quick_mode`

Si `quick_mode=True`, los resultados son una prueba funcional del pipeline. No deben presentarse como rendimiento final clínico. Para resultados defendibles de tesis, ejecutar con `quick_mode=False`, más épocas y conservar el mismo protocolo anti-leakage.
