"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import entrenar_imputador, entrenar_ebm, imputar_datos


def create_pipeline(**_) -> Pipeline:
    return pipeline(
        [
            node(
                func=entrenar_imputador,
                inputs=["train_x"],
                outputs="imputador",
                name="entrenar_imputador",
            ),
            node(
                func=imputar_datos,
                inputs=["train_x", "test_x", "imputador"],
                outputs=["imputed_train_x", "imputed_test_x"],
                name="imputar_datos",
            ),
            node(
                func=entrenar_ebm,
                inputs=["imputed_train_x", "train_y", "params:ebm_params"],
                outputs="modelo_ebm",
                name="entrenar_ebm",
            ),
        ]
    )
