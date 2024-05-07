# Demo: ML model for Payment Delay Prediction

## Provided data set
- the data set is found in the csv file (`train (1) 1 (1).csv`)
## EDA, ML Build & Train
- All info regarding Exploratory Data Analysis (EDA) can be found in the `EDA.ipynb` Jupyter notebook file
- this file also holds the code for model fitting, selection, tuning and saves it in the `best_rf_model.pkl` file.

## ML model Deployment
- the model is deployed on an AWS EC2 instance, as a flask server (`flask-server.py`) file
- a demo for the request format and EC2 address can be found in the `demo-request.py` file
