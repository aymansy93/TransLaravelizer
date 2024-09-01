# TransLaravelizer

TransLaravelizer is a Python utility designed to streamline the process of localizing Laravel applications. It automates the extraction of texts wrapped within `trans()` functions from Blade templates and generates language JSON files, facilitating a smoother translation workflow.

## Features

- Automatically scans Blade templates for `trans()` calls.
- Efficiently extracts text strings and organizes them into JSON format.
- Initializes language files for English and Arabic, with easy extension to other languages.
- Adaptable to various Laravel project structures.

## Getting Started

### Prerequisites

- Python 3.8 or later.
- A Laravel project with Blade templates utilizing the `trans()` function for translations.

### Installation

Clone this repository into your project's root directory:

```bash
git clone https://github.com/aymansy93/TransLaravelizer.git
```

## Usage

1. **Run the script** by executing the following command:

    ```bash
    python lang.py
    ```

    This command will extract all the translatable strings from your Blade templates and controller files and write them to JSON files located in the `langExport` directory.

**Note:** Set this script in the `resources` folder of your Laravel project to ensure it can access the necessary Blade and controller files.

### Customization

- **Change Search Directories**: If your Blade templates or controllers are in different directories, update the `search_directories` dictionary in the script:

    ```python
    search_directories = {
        'blade': 'path/to/your/views',
        'controller': 'path/to/your/controllers'
    }
    ```

- **Add More Languages**: To generate additional language files, modify the `lang_files` list:

    ```python
    lang_files = ['en.json', 'ar.json', 'es.json']
    ```

### Output

After running the script, the `langExport` directory will contain JSON files with the extracted translatable strings, formatted for easy localization.

## Notes

- The script uses the `trans()` function to identify translatable strings. If you use a different function or need to support additional patterns, you may need to modify the regex pattern in the script.
- Make sure your project files are encoded in UTF-8 to avoid encoding issues.
- Ensure you have write permissions for the `langExport` directory.

## Contribution

Feel free to fork this project, make improvements, and submit pull requests. Suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
