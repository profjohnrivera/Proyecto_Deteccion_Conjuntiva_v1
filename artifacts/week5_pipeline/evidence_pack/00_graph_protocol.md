# 00 - Protocolo de gráficos y evidencias

## Decisión metodológica

No todos los gráficos significan lo mismo. Para sustentar correctamente:

| Evidencia | Dataset permitido | Qué demuestra | Qué NO demuestra |
|---|---|---|---|
| Curvas de entrenamiento | Train + validación | Progreso del aprendizaje y señales de sobreajuste | Rendimiento final |
| Matriz de confusión final | Test | Errores finales por clase | No sirve para ajustar el modelo |
| Tabla Baseline / Var1 / Var2 | Test | Comparación formal entre variantes | No debe recalibrar umbrales |
| Muestra visual end-to-end | Ejemplos del test o externos | Que el pipeline ejecuta ROI + clasificación | No es validación clínica |

## Regla anti-sobreajuste

Si se mira el resultado de test y luego se cambia el modelo, el umbral o el preprocesamiento para mejorar ese mismo test, se contamina la evaluación.

## Recomendación para exposición

1. Mostrar curva de entrenamiento para demostrar que hubo entrenamiento real.
2. Mostrar matriz de confusión de test para resultados finales.
3. Mostrar muestra visual para explicar el flujo.
4. Declarar límites: sin ID de paciente no se puede afirmar cero leakage clínico absoluto.
