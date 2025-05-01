import joblib

rdf_model = joblib.load("models\\rdf_model.joblib")
encoder_Status= joblib.load("models\encoder_Status.joblib")
expected_features = joblib.load("models\\feature_names.joblib")

def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result ("Dropout", "Enrolled", "Graduate")
    """
    data = data.reindex(columns=expected_features)
    
    result = rdf_model.predict(data)
    final_result = encoder_Status.inverse_transform(result)[0]
    return final_result