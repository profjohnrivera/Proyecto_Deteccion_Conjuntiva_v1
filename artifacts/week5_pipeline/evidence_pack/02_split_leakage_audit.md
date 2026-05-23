# 02 - Auditoría de split / leakage

Esta auditoría valida que no existan imágenes base repetidas entre train/val/test.

```json
{
  "split_sizes_images": {
    "train": 2053,
    "val": 251,
    "test": 285
  },
  "intersections_by_base_id": {
    "train_vs_val": {
      "count": 0,
      "examples": []
    },
    "train_vs_test": {
      "count": 0,
      "examples": []
    },
    "val_vs_test": {
      "count": 0,
      "examples": []
    }
  },
  "rule": "Si count > 0, hay leakage por imagen base/aumentaciones entre splits.",
  "fail_on_leakage": true,
  "data_yaml": "C:\\Users\\JohnR\\Documents\\GitHub\\Proyecto_Deteccion_Conjuntiva_v1\\data_clean.yaml"
}
```

## Límite metodológico

No prueba leakage clínico por paciente si el dataset no contiene ID de paciente. Sí controla leakage por imagen base/aumentaciones.
