from flask import request, jsonify
import requests
from app import app

# Azure ML Endpoint details
AZURE_ML_ENDPOINT = "http://0d87102a-b3f2-46d0-98c7-7ea58e051276.eastus.azurecontainer.io/score"

@app.route("/predict", methods=["POST"])
def predict():
    input_data = request.json
    # Forward input data to Azure ML model endpoint
    try:
        input_text = input_data.get("text", "")
        payload = {"text": input_text}
        response = requests.post(
            AZURE_ML_ENDPOINT,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

    # Parse the response JSON
    response_data = response.json()
    print(response_data)
    if isinstance(response_data, str):  # Manually parse if needed
        import json
        response_data = json.loads(response_data)

    parsed_response = {
        category: {
            "Probability": details["Probability"],
            "Prediction": details["Prediction"]
        }
        for category, details in response_data.items()
    }

    # Determine if the content is low quality
    low_quality = parsed_response.get("High quality", {}).get("Prediction", 0) != 1

    # Create a list of low-quality categories
    low_quality_categories = [
        category for category, details in parsed_response.items()
        if details["Prediction"] == 1 and category != "High quality"
    ]

    return jsonify({
        "low-quality": low_quality,
        "low-quality-categories": low_quality_categories
    })