from flask import Flask, request, jsonify
import pickle
import json
import pandas as pd

# Create flask application
app = Flask(__name__)

# Load the trained model
with open('best_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load and save to dict the encoded states values
state_encoding_dict = {}
with open('state_encoding_dict.json', 'r') as file:
    state_encoding_dict = json.load(file)


# Define a function to preprocess the input data
def encode_new_data(data):
    # Your preprocessing code here
    encoded_data = data.copy()
    # drop unused columns
    columns_to_drop = ['area_code', 'total_day_minutes', 'total_eve_minutes','total_eve_charge','total_intl_charge','total_intl_minutes','total_night_minutes','total_night_charge','account_length','total_day_calls','total_night_calls','total_eve_calls','total_intl_calls','number_vmail_messages','voice_mail_plan']
    for column in encoded_data.columns.tolist():
        if column in columns_to_drop:
            encoded_data.drop(columns=column, inplace=True)
   
    # label encoding (binary variables)
    label_encoding_columns = ['international_plan']
    for column in label_encoding_columns:
        encoded_data[column] = encoded_data[column].map({'yes': 1, 'no': 0})

    # map state categorical value to its numerical mean encoding
    global state_encoding_dict
    state_name = encoded_data.at[0, 'state']
    encoded_data.drop(columns=['state'], inplace=True)
    encoded_data.loc[0, 'state_encoded'] = state_encoding_dict[state_name]

    return encoded_data

# Define a route to handle POST requests
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    json_data = request.get_json()

    # Preprocess the data
    df_data = pd.DataFrame(json_data)
    preprocessed_data = encode_new_data(df_data)

    # Make prediction
    prediction = model.predict(preprocessed_data)

    if any(prediction.tolist()) == 1:
        prediction = 'yes'
    else:
        prediction = 'no'

    # Prepare response
    response = {'payment_delay': prediction}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
