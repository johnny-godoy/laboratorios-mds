"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.11
"""
from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    create_model_input_table,
    get_data,
    preprocess_companies,
    preprocess_shuttles,
)


def create_pipeline(**_) -> Pipeline:
    return pipeline(
        [
            node(
                func=get_data,
                inputs=None,
                outputs=["raw_companies", "raw_shuttles", "raw_reviews"],
                name="data_loader",
            ),
            node(
                func=preprocess_companies,
                inputs="raw_companies",
                outputs="preprocessed_companies",
                name="company_preprocessor",
            ),
            node(
                func=preprocess_shuttles,
                inputs="raw_shuttles",
                outputs="preprocessed_shuttles",
                name="shuttle_preprocessor",
            ),
            node(
                func=create_model_input_table,
                inputs=[
                    "preprocessed_shuttles",
                    "preprocessed_companies",
                    "raw_reviews",
                ],
                outputs="model_input_table",
                name="model_input_table_creator",
            ),
        ]
    )
