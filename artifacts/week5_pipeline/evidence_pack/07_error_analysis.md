# 07 - Análisis de errores

## Qué mirar primero

- Falsos negativos de anemia: `fn_anemia_as_normal`.
- Falsos positivos: `fp_normal_as_anemia`.
- Fallas de detección YOLO: `detection_failures`.
- Diferencia entre Var1 y Var2: si Var2 cae mucho, el cuello de botella es YOLO/ROI.

## Tabla base

| experiment | input_type | status | accuracy | f1_macro | precision_macro | recall_macro | recall_anemia | recall_normal | fp_normal_as_anemia | fn_anemia_as_normal | detection_failures | detection_rate | ms_per_image | support_total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | Imagen completa | OK | 0.6982456140350877 | 0.697944395149364 | 0.6997177658942365 | 0.6986554373522458 | 0.7375886524822695 | 0.6597222222222222 | 49 | 37 | 0 | 1.0 | 44.76877894736837 | 285 |
| Var1 | ROI con bbox real/label | OK | 0.7333333333333333 | 0.7315852086844453 | 0.7379560572465229 | 0.732565011820331 | 0.6595744680851063 | 0.8055555555555556 | 28 | 48 | 0 | 1.0 | 30.095997894731177 | 285 |
| Var2 | YOLO ROI + clasificador ROI | OK | 0.6877192982456141 | 0.684675725065576 | 0.6934299122628036 | 0.6867612293144207 | 0.5957446808510638 | 0.7777777777777778 | 32 | 57 | 3 | 0.9894736842105263 | 90.33112561403853 | 285 |