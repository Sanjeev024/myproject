import json
import os

def reformat_json(input_file, output_file):
    # Get the full path to the input file
    input_file_path = os.path.join(os.path.dirname(__file__), input_file)

    # Read JSON data from input file
    with open(input_file_path, 'r') as f:
        data = json.load(f)
    
    reformatted_data = []
    # Iterate over each entry in the data
    for entry in data:
        # Check if the 'entries' key exists
        if "entries" in entry and entry["entries"]:
            # Access relevant fields and format the data
            accession = entry["metadata"]["accession"]
            name = entry["metadata"]["name"]
            organism = entry["metadata"]["source_organism"]["scientificName"]
            start = entry["entries"][0]["entry_protein_locations"][0]["fragments"][0]["start"]
            end = entry["entries"][0]["entry_protein_locations"][0]["fragments"][0]["end"]
            name= "Lysozyme-like"
            protien = entry["entries"][0]["accession"]
            domain = f"{name}-{protien} ({start}-{end})"
            
            # Create a new dictionary with the formatted data
            formatted_entry = {
                "Id": accession,
                "name": name,
                "organism": organism,
                "domain": domain
            }
            reformatted_data.append(formatted_entry)
        else:
            print("No 'entries' found for entry:", entry)

    # Get the full path to the output file
    output_file_path = os.path.join(os.path.dirname(__file__), output_file)

    # Write the formatted data to a new JSON file
    with open(output_file_path, 'w') as f:
        json.dump(reformatted_data, f, indent=4)

# Example usage
if __name__ == "__main__":
    input_file = 'new_data.json'
    output_file = 'formatted_data3.json'
    reformat_json(input_file, output_file)
