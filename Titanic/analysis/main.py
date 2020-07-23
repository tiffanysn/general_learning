# Load Package
# import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer, MissingIndicator
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
    LabelEncoder,
    OrdinalEncoder,
)
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_score, RandomizedSearchCV

# Load data
train_df = pd.read_csv("input/train.csv")
test_df = pd.read_csv("input/test.csv")

# Save data
target = train_df[["Survived"]]
submission = test_df[["PassengerId"]]

# Join and Clean
combine = pd.concat([train_df, test_df])

# EDA
combine.info()

# pd.options.plotting.backend = 'plot'

train_df.pivot(columns="Survived", values="Age").plot(kind="hist", stacked=True)

combine.Name.apply(lambda x: x.split(", ")[0]).value_counts().to_list()
