# Muestras de salida end-to-end

Estas muestras prueban el flujo real: imagen → YOLO ROI → recorte → EfficientNet → predicción.

| sample_id | image | true_label | true_name | status | prediction_id | prediction_name | prob_anemia | prob_normal | threshold_anemia | yolo_conf | correct | output_image | message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\104_png.rf.09385316752ae2230e31961fd5a03f52.jpg | 0 | Anemia | OK | 1 | Normal | 0.04300401732325554 | 0.9569960236549377 | 0.5500000000000003 | 0.2232915461063385 | False | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_01_true_Anemia_104_png.rf.09385316752ae2230e31961fd5a03f52.png |  |
| 2 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\104_png.rf.9fe670b02ab3e4b9e796743b0877948b.jpg | 0 | Anemia | OK | 1 | Normal | 0.04672837629914284 | 0.9532716274261475 | 0.5500000000000003 | 0.22574368119239807 | False | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_02_true_Anemia_104_png.rf.9fe670b02ab3e4b9e796743b0877948b.png |  |
| 3 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\10_png.rf.44e757574c6aa5d39c383ca15bf1b463.jpg | 1 | Normal | OK | 1 | Normal | 0.1576940417289734 | 0.8423060178756714 | 0.5500000000000003 | 0.22880439460277557 | True | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_03_true_Normal_10_png.rf.44e757574c6aa5d39c383ca15bf1b463.png |  |
| 4 | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\dataset_clean\test\images\10_png.rf.481d60386b20fedcbf73c0e0bcba208f.jpg | 1 | Normal | OK | 1 | Normal | 0.1534324735403061 | 0.8465675115585327 | 0.5500000000000003 | 0.2354203164577484 | True | C:\Users\JohnR\Documents\GitHub\Proyecto_Deteccion_Conjuntiva_v1\artifacts\week5_pipeline\evidence_pack\08_sample_predictions\sample_04_true_Normal_10_png.rf.481d60386b20fedcbf73c0e0bcba208f.png |  |

## Nota

Si `quick_mode=True`, estas muestras demuestran funcionamiento técnico, no rendimiento clínico final.
