# Import library
import joblib
import numpy as np
import pandas as pd
import os

# load model RDF yang telah dibuat
rdf_model = joblib.load(os.path.join("models", "rdf_model.joblib"))

# Load semua encoder dan scaler 
encoder_Application_mode= joblib.load(os.path.join("models", "encoder_Application_mode.joblib"))
encoder_Course= joblib.load(os.path.join("models", "encoder_Course.joblib"))
encoder_Daytime_evening_attendance= joblib.load(os.path.join("models", "encoder_Daytime_evening_attendance.joblib"))
encoder_Debtor= joblib.load(os.path.join("models", "encoder_Debtor.joblib"))
encoder_Displaced= joblib.load(os.path.join("models", "encoder_Displaced.joblib"))
encoder_Educational_special_needs= joblib.load(os.path.join("models", "encoder_Educational_special_needs.joblib"))
encoder_Fathers_occupation= joblib.load(os.path.join("models", "encoder_Fathers_occupation.joblib"))
encoder_Fathers_qualification= joblib.load(os.path.join("models", "encoder_Fathers_qualification.joblib"))
encoder_Gender= joblib.load(os.path.join("models", "encoder_Gender.joblib"))
encoder_International= joblib.load(os.path.join("models", "encoder_International.joblib"))
encoder_Marital_status= joblib.load(os.path.join("models", "encoder_Marital_status.joblib"))
encoder_Mothers_occupation= joblib.load(os.path.join("models", "encoder_Mothers_occupation.joblib"))
encoder_Mothers_qualification= joblib.load(os.path.join("models", "encoder_Mothers_qualification.joblib"))
encoder_Nationality= joblib.load(os.path.join("models", "encoder_Nationality.joblib"))
encoder_Previous_qualification= joblib.load(os.path.join("models", "encoder_Previous_qualification.joblib"))
encoder_Scholarship_holder= joblib.load(os.path.join("models", "encoder_Scholarship_holder.joblib"))
encoder_Status= joblib.load(os.path.join("models", "encoder_Status.joblib"))
encoder_Tuition_fees_up_to_date= joblib.load(os.path.join("models", "encoder_Tuition_fees_up_to_date.joblib"))

scaler_Admission_grade= joblib.load(os.path.join("models", "scaler_Admission_grade.joblib"))
scaler_Age_at_enrollment= joblib.load(os.path.join("models", "scaler_Age_at_enrollment.joblib"))
scaler_Application_order= joblib.load(os.path.join("models", "scaler_Application_order.joblib"))
scaler_Curricular_units_1st_sem_approved= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_approved.joblib"))
scaler_Curricular_units_1st_sem_credited= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_credited.joblib"))
scaler_Curricular_units_1st_sem_enrolled= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_enrolled.joblib"))
scaler_Curricular_units_1st_sem_evaluations= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_evaluations.joblib"))
scaler_Curricular_units_1st_sem_grade= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_grade.joblib"))
scaler_Curricular_units_1st_sem_without_evaluations= joblib.load(os.path.join("models", "scaler_Curricular_units_1st_sem_without_evaluations.joblib"))
scaler_Curricular_units_2nd_sem_approved= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_approved.joblib"))
scaler_Curricular_units_2nd_sem_credited= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_credited.joblib"))
scaler_Curricular_units_2nd_sem_enrolled= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_enrolled.joblib"))
scaler_Curricular_units_2nd_sem_evaluations= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_evaluations.joblib"))
scaler_Curricular_units_2nd_sem_grade= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_grade.joblib"))
scaler_Curricular_units_2nd_sem_without_evaluations= joblib.load(os.path.join("models", "scaler_Curricular_units_2nd_sem_without_evaluations.joblib"))
scaler_GDP= joblib.load(os.path.join("models", "scaler_GDP.joblib"))
scaler_Inflation_rate= joblib.load(os.path.join("models", "scaler_Inflation_rate.joblib"))
scaler_Previous_qualification_grade= joblib.load(os.path.join("models", "scaler_Previous_qualification_grade.joblib"))
scaler_Status= joblib.load(os.path.join("models", "scaler_Status.joblib"))
scaler_Unemployment_rate= joblib.load(os.path.join("models", "scaler_Unemployment_rate.joblib"))


# Fungsi untuk data preprocessing
def input_df_builder(data):
    """Preprocessing data
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 
        
    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()
    
    
    df["Application_mode"] = encoder_Application_mode.transform(data["Application_mode"]) ###
    df["Course"] = encoder_Course.transform(data["Course"])
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"])
    df["Debtor"] = encoder_Debtor.transform(data["Debtor"])
    df["Displaced"] = encoder_Displaced.transform(data["Displaced"])
    df["Educational_special_needs"] = encoder_Educational_special_needs.transform(data["Educational_special_needs"])
    df["Fathers_occupation"] = encoder_Fathers_occupation.transform(data["Fathers_occupation"])
    df["Fathers_qualification"] = encoder_Fathers_qualification.transform(data["Fathers_qualification"])
    df["Gender"] = encoder_Gender.transform(data["Gender"])
    df["International"] = encoder_International.transform(data["International"])
    df["Marital_status"] = encoder_Marital_status.transform(data["Marital_status"])
    df["Mothers_occupation"] = encoder_Mothers_occupation.transform(data["Mothers_occupation"])
    df["Mothers_qualification"] = encoder_Mothers_qualification.transform(data["Mothers_qualification"])
    df["Nationality"] = encoder_Nationality.transform(data["Nationality"])
    df["Previous_qualification"] = encoder_Previous_qualification.transform(data["Previous_qualification"])
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"])
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"])
    
    df["Admission_grade"] = scaler_Admission_grade.transform(data[["Admission_grade"]])
    df["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(data[["Age_at_enrollment"]])
    df["Application_order"] = scaler_Application_order.transform(data[["Application_order"]])
    df["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(data[["Curricular_units_1st_sem_approved"]])
    df["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(data[["Curricular_units_1st_sem_credited"]])
    df["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(data[["Curricular_units_1st_sem_enrolled"]])
    df["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(data[["Curricular_units_1st_sem_evaluations"]])
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(data[["Curricular_units_1st_sem_grade"]])
    df["Curricular_units_1st_sem_without_evaluations"] = scaler_Curricular_units_1st_sem_without_evaluations.transform(data[["Curricular_units_1st_sem_without_evaluations"]])
    df["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(data[["Curricular_units_2nd_sem_approved"]])
    df["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(data[["Curricular_units_2nd_sem_credited"]])
    df["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(data[["Curricular_units_2nd_sem_enrolled"]])
    df["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(data[["Curricular_units_2nd_sem_evaluations"]])
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(data[["Curricular_units_2nd_sem_grade"]])
    df["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(data[["Curricular_units_2nd_sem_without_evaluations"]])
    df["GDP"] = scaler_GDP.transform(data[["GDP"]])
    df["Inflation_rate"] = scaler_Inflation_rate.transform(data[["Inflation_rate"]])
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(data[["Previous_qualification_grade"]])
    df["Unemployment_rate"] = scaler_Unemployment_rate.transform(data[["Unemployment_rate"]])
    
    #df["Status"] = encoder_Status.transform(data["Status"])
    #df["Status"] = scaler_Status.transform(data["Status"])
    return df





















