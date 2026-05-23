# Bitácora de progreso del pipeline Semana 5

- Pasos registrados: 11/11
- Tiempo acumulado: 440.885 segundos

| Paso | Estado | Duración (s) | Etapa | Salida esperada |
|---:|---|---:|---|---|
| 1/11 | OK | 0.004 | Configuración y validación de entorno | config_used.json + entorno validado |
| 2/11 | OK | 0.0 | Selección de dispositivo | device=cuda si PyTorch CUDA está activo |
| 3/11 | OK | 0.014 | Carga de dataset limpio | rutas train/val/test + clases Anemia/Normal |
| 4/11 | OK | 0.218 | Auditoría de leakage | split_leakage_audit.json con overlaps en 0 |
| 5/11 | OK | 0.0 | Transformaciones train/eval | train_tf + eval_tf |
| 6/11 | OK | 134.175 | YOLO ROI detector/localizador | runs/detect/week5_yolo_*/weights/best.pt |
| 7/11 | OK | 145.982 | Baseline: EfficientNet con imagen completa | baseline_full/best.pt + metrics_test.json |
| 8/11 | OK | 107.83 | Var1: EfficientNet con ROI real desde label | roi_gt/best.pt + metrics_test.json |
| 9/11 | OK | 50.138 | Var2: YOLO ROI + clasificador ROI | yolo_e2e/metrics_test.json + threshold elegido con val |
| 10/11 | OK | 2.309 | Muestra visual de salida end-to-end | evidence_pack/08_sample_predictions/*.png + sample_predictions.csv |
| 11/11 | OK | 0.199 | Tabla comparable, README, bitácora y evidence_pack | comparison_results.csv + README_semana5.md + evidence_pack/ |