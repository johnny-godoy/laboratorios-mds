"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.11
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import caracteristica_producto, crear_tabla, division_train_test


def create_pipeline(**_) -> Pipeline:
    return pipeline(
        [
            node(
                func=caracteristica_producto,
                inputs="raw_dataset",
                outputs="producto",
                name="calcular_característica_útil",
            ),
            node(
                func=crear_tabla,
                inputs=["raw_dataset", "producto"],
                outputs="tabla_datos",
                name="crear_tabla",
            ),
            node(
                func=division_train_test,
                inputs=["tabla_datos", "params:split_params"],
                outputs=["train_x", "train_y", "test_x", "test_y"],
                name="dividir_datos",
            ),
        ]
    )
