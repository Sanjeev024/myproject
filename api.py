import requests
import json

def fetch_and_save_data(url, filename):
    all_results = []
    while url:
        response = requests.get(url)
        data = response.json()
        all_results.extend(data['results'])
        url = data['next']
    
    with open(filename, 'w') as f:
        json.dump(all_results, f, indent=4)

# URL of the initial API endpoint
initial_url = "https://www.ebi.ac.uk/interpro/api/protein/UniProt/entry/pfam/PF00704/?amp%3Bformat=tsv&amp;amp%3Bpage_size=1000&amp;format=json"

# Name of the JSON file to save data
json_filename = "api_response.json"

# Fetch data and save to JSON file
fetch_and_save_data(initial_url, json_filename)

print("Data fetched and saved successfully.")