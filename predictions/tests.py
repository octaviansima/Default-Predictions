from django.test import TestCase
from predictions.engine import Engine
import numpy as np
import pandas as pd
from predictions.choices import forms_cat_cols, forms_num_cols
from predictions.models import *

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score


class EngineTestCase(TestCase):

    def test_predictions(self):
        engine = Engine()
        engine.load_pickle()

        data = engine.data

        numerical = data.loc[:,
                    ["limit_bal", "age", "bill_amt1", "bill_amt2", "bill_amt3", "bill_amt4", "bill_amt5", "bill_amt6",
                     "pay_amt1", "pay_amt2", "pay_amt3", "pay_amt4", "pay_amt5", "pay_amt6"]]
        categorical = data.loc[:, ["sex", "education", "marriage", "pay_1", "pay_2",
                                   "pay_3", "pay_4", "pay_5", "pay_6"]]

        categorical = categorical + 2
        y = data.loc[:, "default payment next month"]

        num_prepared = engine.num_pipeline.fit_transform(numerical)
        cat_prepared = engine.cat_pipeline.fit_transform(categorical)
        X = np.concatenate((num_prepared, cat_prepared.toarray()), axis=1)

        X_comp = engine.pca.transform(X)
        X_train_comp, X_val_comp, y_train, y_val = train_test_split(X_comp, y, test_size=0.2, random_state=12)

        y_forest_proba = engine.model.predict_proba(X_val_comp)
        y_forest_pred = engine.model.predict(X_val_comp)
        accuracy = accuracy_score(y_val, y_forest_pred)
        auc = roc_auc_score(y_val, y_forest_proba[:, 1], average="macro", sample_weight=None)

        self.assertAlmostEqual(accuracy, 0.8156666666666667)
        self.assertAlmostEqual(auc, 0.7720735011050118)

class ModelTestCase(TestCase):

    def test_model_saves(self):
        engine = Engine()

        forms_cols = forms_num_cols + forms_cat_cols
        test_data = [1000, 1, 1, 1, 25, -1, -1, -1, -1, -1, -1,
                     10, 10 ,10 ,10 ,10, 10, 10, 10, 10, 10, 10, 10]
        mapper = {}
        for i in range(len(forms_cols)):
            mapper[forms_cols[i]] = test_data[i]
        df = pd.DataFrame(data=mapper, index=[0], dtype="float64")
        features, default = engine.pd_to_model_and_save(df, True)
        features.prediction_id = default.id
        self.assertEquals(Default.objects.get(pk=1), default)
        self.assertEquals(Features.objects.get(pk=1), features)