import os
import json
import django

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# Now you can import your model using relative import
from gangaGen.models import Protein

def populate_database():
    with open('formatted_data3.json') as f:  # Replace 'new_data.json' with the path to your new JSON file
        new_data = json.load(f)
        for item in new_data:
            # Check if the entry already exists in the database based on the 'Id'
            if not Protein.objects.filter(id=item['Id']).exists():
                # If the entry doesn't exist, create a new entry
                Protein.objects.create(
                    id=item['Id'],
                    name=item['name'],
                    organism=item['organism'],
                    domain=item['domain']
                )

if __name__ == '__main__':
    populate_database()