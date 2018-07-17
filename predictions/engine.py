from sklearn.externals import joblib
import numpy as np
import pandas as pd
from predictions.choices import forms_num_cols, forms_cat_cols, pd_num_cols, pd_cat_cols
from predictions.models import *

class Engine:

    def __init__(self):
        self.cat_pipeline = None
        self.model = None
        self.num_pipeline = None
        self.pca = None
        self.data = None

    def load_pickle(self):
        self.model = joblib.load("predictions/saves/model.pkl")
        self.pca = joblib.load("predictions/saves/pca.pkl")
        self.data = joblib.load("predictions/saves/cleaned_data.pkl")
        self.num_pipeline = joblib.load("predictions/saves/num_pipeline.pkl")
        self.cat_pipeline = joblib.load("predictions/saves/cat_pipeline.pkl")


    def pd_to_vector(self, numerical_v, categorical_v):

        numerical_prev = self.data.loc[:, pd_num_cols]
        categorical_prev = self.data.loc[:, pd_cat_cols]
        numerical = numerical_prev.append(numerical_v)
        categorical = categorical_prev.append(categorical_v)
        categorical = categorical + 2

        num_prepared = self.num_pipeline.fit_transform(numerical)
        cat_prepared = self.cat_pipeline.fit_transform(categorical)
        X = np.concatenate((num_prepared, cat_prepared.toarray()), axis=1)
        x = X[-1, :]
        return x

    def predict(self, x):
        x_comp = self.pca.transform(x)
        y = self.model.predict(x_comp)
        return y

    def cleaned_data_to_pandas(self, cd):
        return pd.DataFrame(cd, index=[0], dtype="float64")

    def pandas_to_model(self, df, y):
        default = Default(did_default=True if y else False)
        features = Features(amount_of_given_credit=df["amount_of_given_credit"][0], gender=df["gender"][0], education=df["education"][0],
                             marital_status=df["marital_status"], age=df["age"][0], payment_status_6=df["payment_status_6_months_ago"][0],
                             payment_status_5=df["payment_status_5_months_ago"][0], payment_status_4=df["payment_status_4_months_ago"][0], payment_status_3=df["payment_status_3_months_ago"][0],
                             payment_status_2=df["payment_status_2_months_ago"][0], payment_status_1=df["payment_status_1_month_ago"][0], bill_statement_6=df["amount_on_bill_statement_6_months_ago"][0],
                             bill_statement_5=df["amount_on_bill_statement_5_months_ago"][0], bill_statement_4=df["amount_on_bill_statement_4_months_ago"][0], bill_statement_3=df["amount_on_bill_statement_3_months_ago"][0],
                             bill_statement_2=df["amount_on_bill_statement_2_months_ago"][0], bill_statement_1=df["amount_on_bill_statement_1_month_ago"][0], previous_payment_6=df["previous_payment_6_months_ago"][0],
                             previous_payment_5=df["previous_payment_5_months_ago"][0], previous_payment_4=df["previous_payment_4_months_ago"][0], previous_payment_3=df["previous_payment_3_months_ago"][0],
                             previous_payment_2=df["previous_payment_2_months_ago"][0], previous_payment_1=df["previous_payment_1_month_ago"][0], prediction=default)
        return features, default

    def split_data(self, df):
        numerical = df.loc[:, forms_num_cols]
        categorical = df.loc[:, forms_cat_cols]

        numerical_map = {}
        categorical_map = {}
        for i in range(len(forms_num_cols)):
            numerical_map[forms_num_cols[i]] = pd_num_cols[i]
        for i in range(len(forms_cat_cols)):
            categorical_map[forms_cat_cols[i]] = pd_cat_cols[i]

        numerical.rename(columns=numerical_map, inplace=True)
        categorical.rename(columns=categorical_map, inplace=True)
        return numerical, categorical