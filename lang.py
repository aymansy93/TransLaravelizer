import os
import re
import json

# Directories to search for files that contain translatable strings
search_directories = {
    'blade': '../resources/views',  # Assuming Blade templates are in the resources/views directory
    'controller': '../app/Http/Controllers'
}

# Base language directory
lang_directory = './langExport'
# Files to generate
lang_files = ['en.json', 'ar.json']
# Pattern to match trans function
pattern = re.compile(r"trans\(['\"](.*?)['\"]\)")

def find_files(directory, extension):
    """
    Recursively find files with a given extension in a directory.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

def extract_translations(directories):
    """
    Extract translations from specified directories and file types.
    """
    translations = {}
    for dir_type, dir_path in directories.items():
        extension = '.blade.php' if dir_type == 'blade' else '.php'
        for file_path in find_files(dir_path, extension):
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()
                matches = pattern.findall(contents)
                for match in matches:
                    translations[match] = match
    return translations

def write_translations_to_files(translations, lang_directory, lang_files):
    """
    Write the extracted translations to specified language files.
    """
    for lang_file in lang_files:
        path = os.path.join(lang_directory, lang_file)
        try:
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(translations, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error writing to {lang_file}: {e}")

def main():
    translations = extract_translations(search_directories)
    write_translations_to_files(translations, lang_directory, lang_files)
    print("Export complete.")

if __name__ == '__main__':
    main()
