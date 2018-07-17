gender_choices = [(1, "Male"), (2, "Female")]
education_choices = [(1, "Graduate School"), (2, "University"), (3, "High School"), (4, "Other")]
marital_choices = [(1, "Married"), (2, "Single"), (3, "Other")]
payment_choices = [(-1, "Paid Duly"), (1, "One Month Delay"), (2, "Two Month Delay"),
                   (3, "Three Month Delay"), (4, "Four Month Delay"), (5, "Five Month Delay"),
                   (6, "Six Month Delay"), (7, "Seven Month Delay"), (8, "Eight Month Delay"),
                   (9, "Nine Month Delay")]

forms_num_cols = ["amount_of_given_credit", "age", "amount_on_bill_statement_6_months_ago",
                    "amount_on_bill_statement_5_months_ago", "amount_on_bill_statement_4_months_ago",
                    "amount_on_bill_statement_3_months_ago", "amount_on_bill_statement_2_months_ago",
                    "amount_on_bill_statement_1_month_ago", "previous_payment_6_months_ago",
                    "previous_payment_5_months_ago", "previous_payment_4_months_ago",
                    "previous_payment_3_months_ago", "previous_payment_2_months_ago",
                    "previous_payment_1_month_ago"]
forms_cat_cols = ["gender", "education", "marital_status", "payment_status_6_months_ago",
                        "payment_status_5_months_ago", "payment_status_4_months_ago",
                        "payment_status_3_months_ago", "payment_status_2_months_ago",
                        "payment_status_1_month_ago"]
pd_num_cols = ["limit_bal", "age", "bill_amt1", "bill_amt2", "bill_amt3",
                        "bill_amt4", "bill_amt5", "bill_amt6",                                                                                            "pay_amt1", "pay_amt2",
                        "pay_amt3", "pay_amt4", "pay_amt5", "pay_amt6"]
pd_cat_cols = ["sex", "education", "marriage", "pay_1", "pay_2",
                        "pay_3", "pay_4", "pay_5", "pay_6"]