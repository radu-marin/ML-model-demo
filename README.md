# Demo: ML model for Payment Delay Prediction

## Provided data set
- the data set is found in the csv file (`train (1) 1 (1).csv`)
## EDA, ML Build & Train
- All info regarding Exploratory Data Analysis (EDA) can be found in the `EDA.ipynb` Jupyter notebook file
- this file also holds the code for model fitting, selection, tuning and saves it in the `best_gb_model.pkl` file (remark: another good model is saved in the `best_rf_model.pkl` file - more details can be found in the notebook from the separate feature branch - rf-model)

## ML model Deployment
- the model is deployed on an AWS EC2 instance, as a flask server (`flask-server.py`) file
- a state_encoding_dict.json file is used as a mapping between state ID and Mean Target encoding, and a misc_encoding_dict.json is used as a mapping for min/max normalization of total cahrge and number of service calls, in order to process the POST request accordingly (more info on Mean Target encoding can be found in section `EDA - 5b` & normalization info in section `ML Model Building - A)` in the `EDA.ipynb` file)
- the accuracy of the model is evaluated at `78.98%` (more info can be found in the `EDA.ipynb` notebook - ML Model Building - subchapters E) to F))
- a demo for the request format (cvs) and EC2 address can be found in the `demo-request-csv.py` file
- the response returns a csv with payment delay & precision columns added.
