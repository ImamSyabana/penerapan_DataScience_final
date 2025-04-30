import streamlit as st
import pandas as pd
import numpy as np
import joblib
from data_preprocessing import input_df_builder
import data_preprocessing
from prediction import prediction
import importlib

col1, col2 = st.columns([1, 5])
with col1:
    st.image("report.png", width=130)
with col2:
    st.header('Student Drop Rate Predictor App')
    
data = pd.DataFrame()
 
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Marital_status

with col1:
    st.markdown("Select your marital status from the options below.")
    Marital_status = st.selectbox(label='Marital_status', options=encoder_Marital_status.classes_, index=0)
    data["Marital_status"] = [Marital_status]
    
with col2:
    st.markdown("#### Marital Status Description")
    legends = ['single', 'married', 'widower', 'divorced', 'facto union', 'legally separated']
    legend_text = ""
    for idx, label in enumerate(encoder_Marital_status.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)

#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Application_mode

with col1:
    st.markdown("Select your Application mode from the options below.")
    Application_mode = st.selectbox(label='Application_mode', options=encoder_Application_mode.classes_, index=0)
    data["Application_mode"] = [Application_mode]
    
with col2:
    st.markdown("#### Application Mode Description")
    legends = [
        " 1st phase - general contingent",
        " Ordinance No. 612/93",
        " 1st phase - special contingent (Azores Island)",
        " Holders of other higher courses", 
        " Ordinance No. 854-B/99 ",
        " International student (bachelor) ",
        " 1st phase - special contingent (Madeira Island) ",
        " 2nd phase - general contingent ",
        " 3rd phase - general contingent ",
        " Ordinance No. 533-A/99, item b2) (Different Plan) ",
        " Ordinance No. 533-A/99, item b3 (Other Institution) ",
        " Over 23 years old ",
        " Transfer ",
        " Change of course ",
        " Technological specialization diploma holders ",
        " Change of institution/course ",
        " Short cycle diploma holders ",
        " Change of institution/course (International)"
    ]
    legend_text = ""
    for idx, label in enumerate(encoder_Application_mode.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    

#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Course

with col1:
    st.markdown("Select Course from the options below.")
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=0)
    data["Course"] = [Course]
    
with col2:
    st.markdown("#### Course Description")
    legends = [
        "Biofuel Production Technologies ",
        "Animation and Multimedia Design ",
        "Social Service (evening attendance) ",
        "Agronomy ",
        "Communication Design ",
        "Veterinary Nursing ",
        "Informatics Engineering ",
        "Equinculture ",
        "Management ",
        "Social Service ",
        "Tourism ",
        "Nursing ",
        "Oral Hygiene ",
        "Advertising and Marketing Management ",
        "Journalism and Communication ",
        "Basic Education ",
        "Management (evening attendance)"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Course.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Daytime_evening_attendance

with col1:
    st.markdown("Select Daytime from the options below.")
    Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=0)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
    
with col2:
    st.markdown("#### Daytime_evening_attendance Description")
    legends = [
        "evening",
        "daytime"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Daytime_evening_attendance.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    

#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Debtor

with col1:
    st.markdown("Select Debtor parameter from the options below.")
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=0)
    data["Debtor"] = [Debtor]
    
with col2:
    st.markdown("#### Debtor Parameter Description")
    legends = [
        "no",
        "yes"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Debtor.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Displaced

with col1:
    st.markdown("Select Displaced parameter from the options below.")
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0)
    data["Displaced"] = [Displaced]
    
with col2:
    st.markdown("#### Displaced Parameter Description")
    legends = [
        "no",
        "yes"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Displaced.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Educational_special_needs

with col1:
    st.markdown("Select Educational_special_needs parameter from the options below.")
    Educational_special_needs = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=0)
    data["Educational_special_needs"] = [Educational_special_needs]
    
with col2:
    st.markdown("#### Educational_special_needs Parameter Description")
    legends = [
        "no",
        "yes"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Educational_special_needs.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Fathers_occupation

with col1:
    st.markdown("Select Fathers_occupation from the options below.")
    Fathers_occupation = st.selectbox(label='Fathers_occupation', options=encoder_Fathers_occupation.classes_, index=0)
    data["Fathers_occupation"] = [Fathers_occupation]
    
with col2:
    st.markdown("#### Fathers_occupation Parameter Description")
    legends = [
        "Student ",
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers ",
        "Specialists in Intellectual and Scientific Activities ",
        "Intermediate Level Technicians and Professions ",
        "Administrative staff ",
        "Personal Services, Security and Safety Workers and Sellers ",
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry ",
        "Skilled Workers in Industry, Construction and Craftsmen ",
        "Installation and Machine Operators and Assembly Workers", 
        "Unskilled Workers ",
        "Armed Forces Professions ",
        "Other Situation ",
        "(blank) ",
        " Armed Forces Officers ",
        " Armed Forces Sergeants ",
        " Other Armed Forces personnel ",
        " Directors of administrative and commercial services ",
        " Hotel, catering, trade and other services directors ",
        " Specialists in the physical sciences, mathematics, engineering and related techniques ",
        " Health professionals ",
        " teachers ",
        " Specialists in finance, accounting, administrative organization, public and commercial relations ",
        " Intermediate level science and engineering technicians and professions ",
        " Technicians and professionals, of intermediate level of health ",
        " Intermediate level technicians from legal, social, sports, cultural and similar services ",
        " Information and communication technology technicians ",
        " Office workers, secretaries in general and data processing operators ",
        " Data, accounting, statistical, financial services and registry-related operators ",
        " Other administrative support staff ",
        " personal service workers ",
        " sellers ",
        " Personal care workers and the like ",
        " Protection and security services personnel ",
        " Market-oriented farmers and skilled agricultural and animal production workers ",
        " Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence ",
        " Skilled construction workers and the like, except electricians ",
        " Skilled workers in metallurgy, metalworking and similar ",
        " Skilled workers in electricity and electronics ",
        " Workers in food processing, woodworking, clothing and other industries and crafts ",
        " Fixed plant and machine operators ",
        " assembly workers ",
        " Vehicle drivers and mobile equipment operators ",
        " Unskilled workers in agriculture, animal production, fisheries and forestry ",
        " Unskilled workers in extractive industry, construction, manufacturing and transport ",
        " Meal preparation assistants ",
        " Street vendors (except food) and street service providers"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Fathers_occupation.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Fathers_qualification

with col1:
    st.markdown("Select Fathers_qualification from the options below.")
    Fathers_qualification = st.selectbox(label='Fathers_qualification', options=encoder_Fathers_qualification.classes_, index=0)
    data["Fathers_qualification"] = [Fathers_qualification]
    
with col2:
    st.markdown("#### Fathers_qualification Parameter Description")
    legends = [
        "Secondary Education - 12th Year of Schooling or Eq. ",
        "Higher Education - Bachelor's Degree ",
        "Higher Education - Degree ",
        "Higher Education - Master's ",
        "Higher Education - Doctorate ",
        "Frequency of Higher Education ",
        "12th Year of Schooling - Not Completed ",
        "11th Year of Schooling - Not Completed ",
        "7th Year (Old) ",
        "Other - 11th Year of Schooling ",
        "2nd year complementary high school course ",
        "10th Year of Schooling ",
        "General commerce course ",
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. ",
        "Complementary High School Course ",
        "Technical-professional course ",
        "Complementary High School Course - not concluded ",
        "7th year of schooling ",
        "2nd cycle of the general high school course ",
        "9th Year of Schooling - Not Completed ",
        "8th year of schooling ",
        "General Course of Administration and Commerce ",
        "Supplementary Accounting and Administration ",
        "Unknown ",
        "Can't read or write ",
        "Can read without having a 4th year of schooling ",
        "Basic education 1st cycle (4th/5th year) or equiv. ",
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. ",
        "Technological specialization course ",
        "Higher education - degree (1st cycle) ",
        "Specialized higher studies course ",
        "Professional higher technical course ",
        "Higher Education - Master (2nd cycle) ",
        "Higher Education - Doctorate (3rd cycle)"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Fathers_qualification.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Gender

with col1:
    st.markdown("Select gender from the options below.")
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=0)
    data["Gender"] = [Gender]
    
with col2:
    st.markdown("#### Gender Parameter Description")
    legends = [
        "female",
        "male"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Gender.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_International

with col1:
    st.markdown("Select International student parameter from the options below.")
    International = st.selectbox(label='International', options=encoder_International.classes_, index=0)
    data["International"] = [International]
    
with col2:
    st.markdown("#### International Student Parameter Description")
    legends = [
        "no",
        "yes"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_International.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Mothers_occupation

with col1:
    st.markdown("Select Mothers_occupation from the options below.")
    Mothers_occupation = st.selectbox(label='Mothers_occupation', options=encoder_Mothers_occupation.classes_, index=0)
    data["Mothers_occupation"] = [Mothers_occupation]
    
with col2:
    st.markdown("#### Mothers_occupation Parameter Description")
    legends = [
        "Student ",
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers ",
        "Specialists in Intellectual and Scientific Activities ",
        "Intermediate Level Technicians and Professions ",
        "Administrative staff ",
        "Personal Services, Security and Safety Workers and Sellers ",
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry ",
        "Skilled Workers in Industry, Construction and Craftsmen ",
        "Installation and Machine Operators and Assembly Workers", 
        "Unskilled Workers ",
        "Armed Forces Professions ",
        "Other Situation ",
        "(blank) ",
        " Armed Forces Officers ",
        " Armed Forces Sergeants ",
        " Other Armed Forces personnel ",
        " Directors of administrative and commercial services ",
        " Hotel, catering, trade and other services directors ",
        " Specialists in the physical sciences, mathematics, engineering and related techniques ",
        " Health professionals ",
        " teachers ",
        " Specialists in finance, accounting, administrative organization, public and commercial relations ",
        " Intermediate level science and engineering technicians and professions ",
        " Technicians and professionals, of intermediate level of health ",
        " Intermediate level technicians from legal, social, sports, cultural and similar services ",
        " Information and communication technology technicians ",
        " Office workers, secretaries in general and data processing operators ",
        " Data, accounting, statistical, financial services and registry-related operators ",
        " Other administrative support staff ",
        " personal service workers ",
        " sellers ",
        " Personal care workers and the like ",
        " Protection and security services personnel ",
        " Market-oriented farmers and skilled agricultural and animal production workers ",
        " Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence ",
        " Skilled construction workers and the like, except electricians ",
        " Skilled workers in metallurgy, metalworking and similar ",
        " Skilled workers in electricity and electronics ",
        " Workers in food processing, woodworking, clothing and other industries and crafts ",
        " Fixed plant and machine operators ",
        " assembly workers ",
        " Vehicle drivers and mobile equipment operators ",
        " Unskilled workers in agriculture, animal production, fisheries and forestry ",
        " Unskilled workers in extractive industry, construction, manufacturing and transport ",
        " Meal preparation assistants ",
        " Street vendors (except food) and street service providers"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Mothers_occupation.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Mothers_qualification

with col1:
    st.markdown("Select Mothers_qualification from the options below.")
    Mothers_qualification = st.selectbox(label='Mothers_qualification', options=encoder_Mothers_qualification.classes_, index=0)
    data["Mothers_qualification"] = [Mothers_qualification]
    
with col2:
    st.markdown("#### Mothers_qualification Parameter Description")
    legends = [
        "Secondary Education - 12th Year of Schooling or Eq. ",
        "Higher Education - Bachelor's Degree ",
        "Higher Education - Degree ",
        "Higher Education - Master's ",
        "Higher Education - Doctorate ",
        "Frequency of Higher Education ",
        "12th Year of Schooling - Not Completed ",
        "11th Year of Schooling - Not Completed ",
        "7th Year (Old) ",
        "Other - 11th Year of Schooling ",
        "2nd year complementary high school course ",
        "10th Year of Schooling ",
        "General commerce course ",
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv. ",
        "Complementary High School Course ",
        "Technical-professional course ",
        "Complementary High School Course - not concluded ",
        "7th year of schooling ",
        "2nd cycle of the general high school course ",
        "9th Year of Schooling - Not Completed ",
        "8th year of schooling ",
        "General Course of Administration and Commerce ",
        "Supplementary Accounting and Administration ",
        "Unknown ",
        "Can't read or write ",
        "Can read without having a 4th year of schooling ",
        "Basic education 1st cycle (4th/5th year) or equiv. ",
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv. ",
        "Technological specialization course ",
        "Higher education - degree (1st cycle) ",
        "Specialized higher studies course ",
        "Professional higher technical course ",
        "Higher Education - Master (2nd cycle) ",
        "Higher Education - Doctorate (3rd cycle)"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Mothers_qualification.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    

#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Nationality

with col1:
    st.markdown("Select Nationality from the options below.")
    Nationality = st.selectbox(label='Nationality', options=encoder_Nationality.classes_, index=0)
    data["Nationality"] = [Nationality]
    
with col2:
    st.markdown("#### Nationality Parameter Description")
    legends = [
      "Portuguese ",
      "German ",
      "Spanish ",
      "Italian ",
      "Dutch ",
      "English ",
      "Lithuanian ",
      "Angolan ",
      "Cape Verdean ",
      "Guinean ",
      "Mozambican ",
      "Santomean ",
      "Turkish ",
      "Brazilian ",
      "Romanian ",
      "Moldova (Republic of) ",
      "Mexican ",
      "Ukrainian ",
      "Russian ",
      "Cuban ",
      "Colombin",
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Nationality.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Previous_qualification

with col1:
    st.markdown("Select Previous_qualification from the options below.")
    Previous_qualification = st.selectbox(label='Previous_qualification', options=encoder_Previous_qualification.classes_, index=0)
    data["Previous_qualification"] = [Previous_qualification]
    
with col2:
    st.markdown("#### Previous_qualification Parameter Description")
    legends = [
      "Secondary education ",
      "Higher education - bachelor's degree ",
      "Higher education - degree ",
      "Higher education - master's ",
      "Higher education - doctorate ",
      "Frequency of higher education ",
      "12th year of schooling - not completed ",
      "11th year of schooling - not completed ",
      "Other - 11th year of schooling ",
      "10th year of schooling ",
      "10th year of schooling - not completed ",
      "Basic education 3rd cycle (9th/10th/11th year) or equiv. ",
      "Basic education 2nd cycle (6th/7th/8th year) or equiv.", 
      "Technological specialization course ",
      "Higher education - degree (1st cycle) ",
      "Professional higher technical course ",
      "Higher education - master (2nd cycle)"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Previous_qualification.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
    
#######################################################
col1, col2 = st.columns(2)

from data_preprocessing import encoder_Scholarship_holder

with col1:
    st.markdown("Select Scholarship_holder from the options below.")
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=0)
    data["Scholarship_holder"] = [Scholarship_holder]
    
with col2:
    st.markdown("#### Scholarship_holder Parameter Description")
    legends = [
      "no",
      "yes"
    ]
    
    legend_text = ""
    for idx, label in enumerate(encoder_Scholarship_holder.classes_):
        legend_text += f"- **{label}**: {legends[idx]}\n"
    st.markdown(legend_text)
    
#######################################################
# col1, col2 = st.columns(2)

# from data_preprocessing import encoder_Tuition_fees_up_to_date

# with col1:
#     st.markdown("Select Tuition_fees_up_to_date from the options below.")
#     Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=0)
#     data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
    
# with col2:
#     st.markdown("#### Tuition_fees_up_to_date Parameter Description")
#     legends = [
#       "no",
#       "yes"
#     ]
    
#     legend_text = ""
#     for idx, label in enumerate(encoder_Tuition_fees_up_to_date.classes_):
#         legend_text += f"- **{label}**: {legends[idx]}\n"
#     st.markdown(legend_text)
    
# #######################################################
#######################################################



def streamlit_categorical_col_builder(encoder_name, data, legendsArray, col1,col2):
    
    module = importlib.import_module("data_preprocessing")
    encoder = getattr(module, encoder_name)
    
    label = encoder_name.replace("encoder_", "")
    
    
    with col1:
        st.markdown("Select one value from the options below.")
        selectedValue = st.selectbox(label=label, options=encoder.classes_, index=0)
        data[label] = [selectedValue]
        
    with col2:
        st.markdown(f"#### {label} Parameter Description")
        legends = legendsArray
    
        legend_text = ""
        for idx, keterangan in enumerate(encoder.classes_):
            legend_text += f"- **{keterangan}**: {legends[idx]}\n"
        st.markdown(legend_text)
    
    return data


streamlit_categorical_col_builder(
    encoder_name= "encoder_Tuition_fees_up_to_date",
    data = data,
    legendsArray= ["no", "yes"],
    col1 = col1,
    col2 = col2
)