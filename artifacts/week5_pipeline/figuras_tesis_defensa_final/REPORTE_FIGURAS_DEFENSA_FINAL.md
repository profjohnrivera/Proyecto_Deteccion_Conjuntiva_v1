# Figuras finales para defensa de tesis

Carpeta generada: `artifacts\week5_pipeline\figuras_tesis_defensa_final`

## Figuras generadas

- `01_proporcion_clases_por_subconjunto.png`
- `02_auditoria_no_leakage.png`
- `03_metricas_principales_por_variante.png`
- `04_matriz_confusion_test_formal.png`
- `05_resumen_aciertos_errores_test_formal.png`
- `06_panel_ejecutivo_validacion.png`

## Advertencias

- Sin advertencias críticas detectadas.

## Orden recomendado para la sustentación

1. `06_panel_ejecutivo_validacion.png`
2. `01_proporcion_clases_por_subconjunto.png`
3. `02_auditoria_no_leakage.png`
4. `03_metricas_principales_por_variante.png`
5. `04_matriz_confusion_test_formal.png`
6. `05_resumen_aciertos_errores_test_formal.png`

## Idea central de exposición

En esta etapa consolidé la validación metodológica del experimento. Primero verifiqué el balance de clases entre subconjuntos; luego audité la separación entre train, validation y test para descartar leakage por imagen base; después comparé formalmente las variantes del pipeline; y finalmente analicé los errores del modelo en el test formal, con énfasis en los falsos negativos de Anemia.

## Precisión metodológica obligatoria

No corresponde afirmar validación clínica.
No corresponde afirmar separación por paciente si el dataset no contiene `patient_id`.
El sistema debe presentarse como prototipo experimental de apoyo al tamizaje y no como diagnóstico médico.
