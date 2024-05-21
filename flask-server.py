from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json
from io import StringIO

# Create flask application
app = Flask(__name__)

# Load the trained model
with open('best_gb_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load and save to dict the encoded states values
state_encoding_dict = {}
with open('state_encoding_dict.json', 'r') as file:
    state_encoding_dict = json.load(file)

# Load and save to dict the encoded misc values (mix/max total_day_charge & num_service_calls)
misc_encoding_dict = {}
with open('misc_encoding_dict.json', 'r') as file:
    misc_encoding_dict = json.load(file)

# Define a function to preprocess the input data
def encode_new_data(data):
    # Read data
    encoded_data = data.copy()
    # Drop unused columns
    columns_to_drop = ['area_code', 'total_day_minutes', 'total_eve_minutes', 'total_eve_charge', 'total_intl_charge', 'total_intl_minutes', 'total_night_minutes', 'total_night_charge', 'account_length', 'total_day_calls', 'total_night_calls', 'total_eve_calls', 'total_intl_calls', 'number_vmail_messages']
    for column in encoded_data.columns.tolist():
        if column in columns_to_drop:
            encoded_data.drop(columns=column, inplace=True)

    # Label encoding (binary variables)
    label_encoding_columns = ['international_plan', 'voice_mail_plan']
    for column in label_encoding_columns:
        encoded_data[column] = encoded_data[column].map({'yes': 1, 'no': 0})

    # min-max normalization (numeric variables) for total_day_charge and number_customer_service_calls
    global misc_encoding_dict
    total_day_charge_min = misc_encoding_dict['total_day_charge_min']
    total_day_charge_max = misc_encoding_dict['total_day_charge_max']
    encoded_data['total_day_charge'] = (encoded_data['total_day_charge'] - total_day_charge_min) / (total_day_charge_max - total_day_charge_min)
    number_customer_service_calls_min = misc_encoding_dict['number_customer_service_calls_min']
    number_customer_service_calls_max = misc_encoding_dict['number_customer_service_calls_max']
    encoded_data['number_customer_service_calls'] = (encoded_data['number_customer_service_calls'] - number_customer_service_calls_min) / (number_customer_service_calls_max - number_customer_service_calls_min)

    # Map state categorical value to its numerical mean encoding
    global state_encoding_dict
    encoded_data['state_encoded'] = encoded_data['state'].map(state_encoding_dict)
    encoded_data.drop(columns=['state'], inplace=True, errors='ignore')

    return encoded_data

# Define a route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    if 'file' in request.files:
        file = request.files['file']
        data = pd.read_csv(file)
        print(data)
    else:
        return jsonify({'error': 'Invalid content type, text/csv required', 'content type': request.content_type}), 400

    # Preprocess the data
    preprocessed_data = encode_new_data(data)
    print(preprocessed_data)

    # Make prediction
    prediction = model.predict(preprocessed_data)
    print(str(prediction))

    # Prepare response
    data['payment_delay'] = ['yes' if p == 1 else 'no' for p in prediction]
    data['model_precision'] = misc_encoding_dict['gb_model_precision']
    response = data.to_csv(index=False)

    return response, 200, {'Content-Type': 'text/csv'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
