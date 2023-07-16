"""
This is a boilerplate pipeline 'eval_model'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline
from sklearn.metrics import classification_report

from .nodes import prediccion_modelo, explicacion_global, explicacion_local


def create_pipeline(**_) -> Pipeline:
    return pipeline(
        [
            node(
                func=prediccion_modelo,
                inputs=["modelo_ebm", "imputed_test_x"],
                outputs="pred_y",
                name="crear_predicciones",
            ),
            node(
                func=classification_report,
                inputs=["test_y", "pred_y"],
                outputs="reporte_metricas",
                name="crear_reporte_metricas",
            ),
            node(
                func=explicacion_global,
                inputs=["modelo_ebm"],
                outputs="explicacion_global",
                name="generar_explicacion_global",
            ),
            node(
                func=explicacion_local,
                inputs=["modelo_ebm", "imputed_test_x"],
                outputs="explicacion_local",
                name="generar_explicacion_local",
            ),
        ]
    )
