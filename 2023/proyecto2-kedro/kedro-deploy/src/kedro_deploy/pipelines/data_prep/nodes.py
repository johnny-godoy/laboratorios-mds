"""
This is a boilerplate pipeline 'data_prep'
generated using Kedro 0.18.11
"""
import pandas as pd
from sklearn.model_selection import train_test_split


def caracteristica_producto(
    datos: pd.DataFrame,
) -> pd.DataFrame:
    """Crear una caracteristica que multiplica outstanding_debt por interest rate."""
    return (datos["outstanding_debt"] * datos["interest_rate"]).to_frame()


def crear_tabla(
    datos: pd.DataFrame,
    producto: pd.DataFrame,
) -> pd.DataFrame:
    """Crear una tabla con las columnas de datos y caracteristica_producto."""
    return pd.concat([datos, producto], axis=1)


def division_train_test(
    datos: pd.DataFrame,
    split_params: dict,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Dividir los datos en train y test."""
    X, y = datos.drop(columns=["credit_score"]), datos["credit_score"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, **split_params
    )
    return X_train, y_train.to_frame(), X_test, y_test.to_frame()


def limpiar_datos(
    datos: pd.DataFrame,
) -> pd.DataFrame:
    """Realiza limpiezas que se pueden realizar antes del train-test split,
    dado que no causan contaminación de datos."""
    datos_ = datos.copy()
    datos_["payment_behaviour_low_spent"] = datos_.payment_behaviour.apply(
        lambda x: "Low_spent" in x
    ).astype(int)
    datos_["payment_behaviour_value"] = datos_.payment_behaviour.apply(
        lambda x: -1 if "Small_value" in x else 1 if "High_value" in x else 0
    )
    datos_["payment_behaviour_na"] = (datos_.payment_behaviour == "!@9#%8").astype(int)
    datos_["payment_of_min_amount"].replace(
        {"No": 0.0, "Yes": 1.0, "NM": -1.0}, inplace=True
    )
    datos_["payment_of_min_amount"] = datos_["payment_of_min_amount"].astype(float)
    return datos_
