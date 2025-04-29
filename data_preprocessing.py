
import joblib
import numpy as np
import pandas as pd

rdf_model = joblib.load("models\\rdf_model.joblib")

encoder_Application_mode= joblib.load("models\\encoder_Application_mode")
encoder_Course= joblib.load("models\\encoder_Course")
encoder_Daytime_evening_attendance= joblib.load("models\\encoder_Daytime_evening_attendance")
encoder_Debtor= joblib.load("models\\encoder_Debtor")
encoder_Displaced= joblib.load("models\\encoder_Displaced")
encoder_Educational_special_needs= joblib.load("models\\encoder_Educational_special_needs")
encoder_Fathers_occupation= joblib.load("models\\encoder_Fathers_occupation")
encoder_Fathers_qualification= joblib.load("models\\encoder_Fathers_qualification")
encoder_Gender= joblib.load("models\\encoder_Gender")
encoder_International= joblib.load("models\\encoder_International")
encoder_Marital_status= joblib.load("models\\encoder_Marital_status")
encoder_Mothers_occupation= joblib.load("models\\encoder_Mothers_occupation")
encoder_Mothers_qualification= joblib.load("models\\encoder_Mothers_qualification")
encoder_Nationality= joblib.load("models\\encoder_Nationality")
encoder_Previous_qualification= joblib.load("models\\encoder_Previous_qualification")
encoder_Scholarship_holder= joblib.load("models\\encoder_Scholarship_holder")
encoder_Status= joblib.load("models\\encoder_Status")
encoder_Tuition_fees_up_to_date= joblib.load("models\\encoder_Tuition_fees_up_to_date")

scaler_Admission_grade= joblib.load("models\\scaler_Admission_grade")
scaler_Age_at_enrollment= joblib.load("models\\scaler_Age_at_enrollment")
scaler_Application_order= joblib.load("models\\scaler_Application_order")
scaler_Curricular_units_1st_sem_approved= joblib.load("models\\scaler_Curricular_units_1st_sem_approved")
scaler_Curricular_units_1st_sem_credited= joblib.load("models\\scaler_Curricular_units_1st_sem_credited")
scaler_Curricular_units_1st_sem_enrolled= joblib.load("models\\scaler_Curricular_units_1st_sem_enrolled")
scaler_Curricular_units_1st_sem_evaluations= joblib.load("models\\scaler_Curricular_units_1st_sem_evaluations")
scaler_Curricular_units_1st_sem_grade= joblib.load("models\\scaler_Curricular_units_1st_sem_grade")
scaler_Curricular_units_1st_sem_without_evaluations= joblib.load("models\\scaler_Curricular_units_1st_sem_without_evaluations")
scaler_Curricular_units_2nd_sem_approved= joblib.load("models\\scaler_Curricular_units_2nd_sem_approved")
scaler_Curricular_units_2nd_sem_credited= joblib.load("models\\scaler_Curricular_units_2nd_sem_credited")
scaler_Curricular_units_2nd_sem_enrolled= joblib.load("models\\scaler_Curricular_units_2nd_sem_enrolled")
scaler_Curricular_units_2nd_sem_evaluations= joblib.load("models\\scaler_Curricular_units_2nd_sem_evaluations")
scaler_Curricular_units_2nd_sem_grade= joblib.load("models\\scaler_Curricular_units_2nd_sem_grade")
scaler_Curricular_units_2nd_sem_without_evaluations= joblib.load("models\\scaler_Curricular_units_2nd_sem_without_evaluations")
scaler_GDP= joblib.load("models\\scaler_GDP")
scaler_Inflation_rate= joblib.load("models\\scaler_Inflation_rate")
scaler_Previous_qualification_grade= joblib.load("models\\scaler_Previous_qualification_grade")
scaler_Status= joblib.load("models\\scaler_Status")
scaler_Unemployment_rate= joblib.load("models\\scaler_Unemployment_rate")























