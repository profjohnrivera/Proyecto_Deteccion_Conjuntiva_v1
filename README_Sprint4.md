# Sprint 4 — Análisis exploratorio de subgrupos

## Punto de partida
El test formal evaluó **285 imágenes** y registró **53 errores**.
La tasa de error global fue **18.6%** (IC 95 % Wilson: **14.5%–23.5%**).

## Hallazgo principal
El mayor diferencial de error se observó en **Distancia al umbral operativo de Anemia ≤ 0.172 (P33 post hoc)**: +19.5 pp frente a su complemento (IC 95 %: +5.6 a +33.3 pp). Este resultado identifica una zona de incertidumbre del modelo; no demuestra una causa clínica, visual ni técnica.

## Comparación de subgrupos

| Subgrupo | Tipo | Error subgrupo | Error complemento | Diferencia de riesgo | Interpretación |
|---|---|---:|---:|---:|---|
| Clase real: Anemia | Subgrupo clínico | 19.9% (28/141) | 17.4% (25/144) | +2.5 pp [-10.3, +15.2] | Resultado no concluyente: el IC de la diferencia incluye cero. |
| Múltiples ROI candidatas (≥ 2 cajas) | Subgrupo técnico | 20.2% (23/114) | 17.5% (30/171) | +2.6 pp [-10.1, +15.9] | Resultado no concluyente: el IC de la diferencia incluye cero. |
| Distancia al umbral operativo de Anemia ≤ 0.172 (P33 post hoc) | Indicador interno | 31.6% (30/95) | 12.1% (23/190) | +19.5 pp [+5.6, +33.3] | Zona de incertidumbre prioritaria: presenta mayor error, pero no debe interpretarse como causa raíz. |
| YOLO baja confianza ≤ 0.501 (P33 post hoc) | Indicador interno | 18.9% (18/95) | 18.4% (35/190) | +0.5 pp [-12.2, +14.4] | Indicador interno del modelo; no se interpreta como causa raíz. |

## Gráficas

### Sprint4 Diferencia Riesgo Subgrupo Vs Complemento

![sprint4_diferencia_riesgo_subgrupo_vs_complemento](graficas/sprint4_diferencia_riesgo_subgrupo_vs_complemento.png)

## Conclusión
Los subgrupos pueden solaparse, por lo que no representan causas independientes ni sus errores deben sumarse.
Los indicadores internos del modelo, como cercanía al umbral o confianza baja, sirven para priorizar revisión humana; no prueban una causa raíz.

## Siguiente paso
Revisar los casos erróneos y controles correctos exportados para comparar iluminación, desenfoque, oclusión, tamaño de ROI, alineación anatómica y posibles inconsistencias de etiqueta.

## Restricción metodológica
El test formal solo se usa para describir resultados. No se reentrena ni se recalibra el umbral con este conjunto.