import requests

url = 'http://cloudboy.eu:5000/predict'
data = {
  "state": ["TN"],
  "account_length": [80],
  "area_code": ["area_code_415"],
  "international_plan": ["yes"],
  "voice_mail_plan": ["no"],
  "number_vmail_messages": [0],
  "total_day_minutes": [276.5],
  "total_day_calls": [122],
  "total_day_charge": [47.01],
  "total_eve_minutes": [195.6],
  "total_eve_calls": [79],
  "total_eve_charge": [16.63],
  "total_night_minutes": [210.3],
  "total_night_calls": [78],
  "total_night_charge": [9.46],
  "total_intl_minutes": [7.2],
  "total_intl_calls": [3],
  "total_intl_charge": [1.94],
  "number_customer_service_calls": [1]
}

response = requests.post(url, json=data)
print(response.json())
