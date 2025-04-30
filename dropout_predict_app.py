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

Marital_status_list =  ['single', 'married', 'widower', 'divorced', 'facto union', 'legally separated']

Application_mode_list = [
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

Course_list = [
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

Daytime_evening_attendance_list = [
        "evening",
        "daytime"
    ]

Debtor_list = ["no","yes"]

Displaced_list = ["no","yes"]

Educational_special_needs_list=["no","yes"]

Fathers_occupation_list = [
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

Fathers_qualification_list =[
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

Gender_list = [
        "female",
        "male"
    ]

International_list = ["no","yes"]

Mothers_occupation_list = [
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
    
Mothers_qualification_list =[
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

Nationality_list = [
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

Previous_qualification_list =[
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

Scholarship_holder_list = ["no","yes"]
Tuition_fees_up_to_date_list =["no","yes"]

legendsDictionary = {
    "Marital_status" : Marital_status_list,
    "Application_mode" : Application_mode_list,
    "Course" : Course_list,
    "Daytime_evening_attendance" : Daytime_evening_attendance_list,
    "Debtor" : Debtor_list,
    "Displaced" : Displaced_list,
    "Educational_special_needs" : Educational_special_needs_list,
    "Fathers_occupation" : Fathers_occupation_list,
    "Fathers_qualification" : Fathers_qualification_list,
    "Gender" : Gender_list,
    "International" : International_list,
    "Mothers_occupation" : Mothers_occupation_list,
    "Mothers_qualification" : Mothers_qualification_list,
    "Nationality" : Nationality_list,
    'Previous_qualification':Previous_qualification_list,
    "Scholarship_holder": Scholarship_holder_list,
    "Tuition_fees_up_to_date": Tuition_fees_up_to_date_list
}



# Fungsi yang dah jadi

def streamlit_categorical_col_builder(encoder_name, data, legendsArray):
    col1, col2 = st.columns(2)
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

# Loop fungsi streamlit builder untuk categorical

for key in legendsDictionary.keys():
    streamlit_categorical_col_builder(
        encoder_name= f"encoder_{key}",
        data = data,
        legendsArray= legendsDictionary[key],
    )

