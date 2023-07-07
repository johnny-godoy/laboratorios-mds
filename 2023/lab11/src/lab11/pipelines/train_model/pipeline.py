"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.18.11
"""
from kedro.pipeline import node
from kedro.pipeline import Pipeline
from kedro.pipeline import pipeline

from .nodes import evaluate_model
from .nodes import split_data
from .nodes import train_model


def create_pipeline(**_) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["model_input_table", "params:split_params"],
                outputs=[
                    "X_train",
                    "X_valid",
                    "X_test",
                    "y_train",
                    "y_valid",
                    "y_test",
                ],
                name="data_splitter",
            ),
            node(
                func=train_model,
                inputs=["X_train", "X_valid", "y_train", "y_valid"],
                outputs="best_model",
                name="model_trainer",
            ),
            node(
                func=evaluate_model,
                inputs=["best_model", "X_test", "y_test"],
                outputs=None,
                name="model_evaluator",
            ),
        ]
    )
