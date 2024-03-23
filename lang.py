import os
import re
import json

# Directory containing your Blade templates
blade_directory = './views'
# Base language directory
lang_directory = './langExport'
# Files to generate
lang_files = ['en.json', 'ar.json']
# Pattern to match trans function
pattern = re.compile(r"trans\(['\"](.*?)['\"]\)")

translations = {}

# Function to recursively find Blade files
def find_blade_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.blade.php'):
                yield os.path.join(root, file)

# Extract translations
for blade_file in find_blade_files(blade_directory):
    with open(blade_file, 'r', encoding='utf-8') as file:
        contents = file.read()
        matches = pattern.findall(contents)
        for match in matches:
            translations[match] = match  # Initially, key and value are the same

# Write translations to language files
for lang_file in lang_files:
    path = os.path.join(lang_directory, lang_file)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(translations, file, ensure_ascii=False, indent=4)

print("Export complete.")
