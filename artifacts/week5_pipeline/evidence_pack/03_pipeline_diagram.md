# 03 - Pipeline experimental

```text
Imagen original
  ├─ Baseline: imagen completa → EfficientNet-B0 → Anemia/Normal
  ├─ Var1: bbox real del label → ROI → EfficientNet-B0 → Anemia/Normal
  └─ Var2: YOLO → ROI detectado → EfficientNet-B0 → Anemia/Normal

Reglas:
- Train ajusta pesos.
- Val calibra temperatura y umbral.
- Test solo evalúa al final.
```

## Lectura objetiva

Var1 mide si el recorte ROI ayuda cuando la región es conocida. Var2 mide el pipeline real end-to-end cuando la ROI debe ser detectada automáticamente.
