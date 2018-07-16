from predictions.models import Features
import pandas as pd

def cleaned_data_to_pandas(cd):
    return pd.DataFrame(cd, index=[0], dtype="float64")

def pandas_to_model(df):
    """model = Features(amount_of_given_credit=cd["amount_of_given_credit"], gender=cd["gender"], education=cd["education"],
                         marital_status=cd["marital_status"], age=cd["age"], payment_status_6=cd["payment_status_6_months_ago"],
                         payment_status_5=cd["payment_status_5_months_ago"], payment_status_4=cd["payment_status_4_months_ago"], payment_status_3=cd["payment_status_3_months_ago"],
                         payment_status_2=cd["payment_status_2_months_ago"], payment_status_1=cd["payment_status_1_month_ago"], bill_statement_6=cd["amount_on_bill_statement_6_months_ago"],
                         bill_statement_5=cd["amount_on_bill_statement_5_months_ago"], bill_statement_4=cd["amount_on_bill_statement_4_months_ago"], bill_statement_3=cd["amount_on_bill_statement_3_months_ago"],
                         bill_statement_2=cd["amount_on_bill_statement_2_months_ago"], bill_statement_1=cd["amount_on_bill_statement_1_month_ago"], previous_payment_6=cd["previous_payment_6_months_ago"],
                         previous_payment_5=cd["previous_payment_5_months_ago"], previous_payment_4=cd["previous_payment_4_months_ago"], previous_payment_3=cd["previous_payment_3_months_ago"],
                         previous_payment_2=cd["previous_payment_2_months_ago"], previous_payment_1=cd["previous_payment_1_month_ago"])"""
    return None

def split_data(df):
    numerical = df.loc[:, ["amount_of_given_credit", "age", "amount_on_bill_statement_6_months_ago",
                           "amount_on_bill_statement_5_months_ago", "amount_on_bill_statement_4_months_ago",
                           "amount_on_bill_statement_3_months_ago", "amount_on_bill_statement_2_months_ago",
                           "amount_on_bill_statement_1_month_ago", "previous_payment_6_months_ago",
                           "previous_payment_5_months_ago", "previous_payment_4_months_ago",
                           "previous_payment_3_months_ago", "previous_payment_2_months_ago",
                           "previous_payment_1_month_ago"]]
    categorical = df.loc[:, ["gender", "education", "marital_status", "payment_status_6_months_ago",
                             "payment_status_5_months_ago", "payment_status_4_months_ago",
                             "payment_status_3_months_ago", "payment_status_2_months_ago",
                             "payment_status_1_month_ago"]]
    categorical = categorical + 2
    return numerical, categorical