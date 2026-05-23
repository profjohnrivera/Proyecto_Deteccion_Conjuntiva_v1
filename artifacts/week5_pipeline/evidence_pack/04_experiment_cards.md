# 04 - Tarjetas de experimentos

## Baseline

- Entrada: imagen completa.
- Modelo: EfficientNet-B0.
- Cambio: ninguno; referencia base.

## Var1

- Entrada: ROI con bounding box real desde label.
- Modelo: EfficientNet-B0.
- Cambio único: imagen completa → recorte ROI real.

## Var2

- Entrada: ROI detectada por YOLO.
- Modelo: YOLOv8n + EfficientNet-B0.
- Cambio único frente a Var1: ROI real → ROI detectada automáticamente.

## Métrica principal recomendada

- `recall_anemia`: crítico para reducir falsos negativos.
- `f1_macro`: balancea ambas clases.
- `fn_anemia_as_normal`: error clínicamente más delicado.
