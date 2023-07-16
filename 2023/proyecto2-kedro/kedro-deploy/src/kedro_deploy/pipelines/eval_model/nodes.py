"""
This is a boilerplate pipeline 'eval_model'
generated using Kedro 0.18.11
"""
import pandas as pd


def prediccion_modelo(
    modelo,
    imputed_test_x: pd.DataFrame
) -> pd.DataFrame:
    """
    Predice las clases de los datos de entrada
    """
    y_pred = modelo.predict(imputed_test_x)
    return pd.DataFrame(y_pred)


def explicacion_global(
    modelo,
) -> pd.DataFrame:
    """
    Genera una explicación global del modelo
    """
    return modelo.explain_global()


def explicacion_local(
    modelo,
    imputed_test_x: pd.DataFrame
) -> pd.DataFrame:
    """Genera una explicación local del modelo"""
    return modelo.explain_local(imputed_test_x)
