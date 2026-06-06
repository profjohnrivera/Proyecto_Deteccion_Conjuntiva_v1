# 07 - Análisis de errores

## Qué mirar primero

- Falsos negativos de anemia: `fn_anemia_as_normal`.
- Falsos positivos: `fp_normal_as_anemia`.
- Fallas de detección YOLO: `detection_failures`.
- Diferencia entre Var1 y Var2: si Var2 cae mucho, el cuello de botella es YOLO/ROI.

## Tabla base

| experiment | input_type | status | accuracy | f1_macro | precision_macro | recall_macro | recall_anemia | recall_normal | fp_normal_as_anemia | fn_anemia_as_normal | detection_failures | detection_rate | ms_per_image | support_total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baseline | Imagen completa | OK | 0.7228070175438597 | 0.7177899499880924 | 0.7429318254560973 | 0.724290780141844 | 0.8652482269503546 | 0.5833333333333334 | 60 | 19 | 0 | 1.0 | 23.469475087742403 | 285 |
| Var1 | ROI con bbox real/label | OK | 0.7228070175438597 | 0.709037102131014 | 0.7690736513276463 | 0.720596926713948 | 0.5106382978723404 | 0.9305555555555556 | 10 | 69 | 0 | 1.0 | 16.777019649172168 | 285 |
| Var2 | YOLO ROI + clasificador ROI | OK | 0.8140350877192982 | 0.8139526290507335 | 0.8141821946169772 | 0.8139036643026005 | 0.8014184397163121 | 0.8263888888888888 | 25 | 28 | 0 | 1.0 | 51.68263824562656 | 285 |