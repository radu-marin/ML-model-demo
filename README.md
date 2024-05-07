# Demo: ML model for Payment Delay Prediction

## Provided data set
- the data set is found in the csv file (`train (1) 1 (1).csv`)
## EDA, ML Build & Train
- All info regarding Exploratory Data Analysis (EDA) can be found in the `EDA.ipynb` Jupyter notebook file
- this file also holds the code for model fitting, selection, tuning and saves it in the `best_rf_model.pkl` file.

## ML model Deployment
- the model is deployed on an AWS EC2 instance, as a flask server (`flask-server.py`) file
- a state_encoding_dict.json file is used as a mapping between state ID and Mean Target encoding in order to process the POST request accordingly (more info on Mean Target encoding can be found in chapter 5b in the EDA.ipynb file)
- a demo for the request format (json) and EC2 address can be found in the `demo-request.py` file
- the response returns a json with a payment delay entry, eg `{'payment_delay': 'yes'}`
