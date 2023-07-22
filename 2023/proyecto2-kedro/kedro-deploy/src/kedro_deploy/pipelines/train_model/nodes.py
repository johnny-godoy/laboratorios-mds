import pandas as pd
from interpret.glassbox import ExplainableBoostingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


def entrenar_imputador(train_x: pd.DataFrame) -> ColumnTransformer:
    imputador = ColumnTransformer(
        [
            (
                "imputador",
                SimpleImputer(strategy="median"),
                train_x.select_dtypes(include="number").columns
            ),
        ],
        remainder="passthrough",
        verbose_feature_names_out=False,
    )
    imputador.set_output(transform="pandas")
    imputador.fit(train_x)
    return imputador


def imputar_datos(
    train_x: pd.DataFrame, test_x: pd.DataFrame, imputador: SimpleImputer
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Retorna los datos imputados."""
    train_x = pd.DataFrame(imputador.transform(train_x), columns=train_x.columns)
    test_x = pd.DataFrame(imputador.transform(test_x), columns=test_x.columns)
    return train_x, test_x


def entrenar_ebm(
    train_x: pd.DataFrame, train_y: pd.Series, params: dict
) -> ExplainableBoostingClassifier:
    ebm = ExplainableBoostingClassifier(random_state=0, **params)
    ebm.fit(train_x, train_y)
    return ebm
