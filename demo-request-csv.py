import requests

# Specify the URL of your Flask server
url = 'http://localhost:5001/predict'  # Update with your server URL

# Load the CSV file
with open('demo-request.csv', 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# Check if the request was successful
if response.status_code == 200:
    # Save the updated CSV file
    with open('predicted_tst.csv', 'wb') as f:
        f.write(response.content)
    print("Prediction successful. Updated CSV file saved as 'predicted_tst.csv'")
else:
    print("Error:", response.text)
