import csv
import io
from typing import List, Dict
from langdetect import detect
from googletrans import Translator

def translate_csv(input_file: str, output_file: str, output_language: str) -> None:
    """
    Translate the 'code_msg' and 'description' columns of a CSV file.
    
    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    :param output_language: The language code for the desired output language
    """
    translator = Translator()

    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8-sig') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + [f'code_msg_{output_language}', f'description_{output_language}']
        
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            code_msg = row['code_msg']
            description = row['description']
            
            # Detect input language
            input_language = detect(code_msg + ' ' + description)
            
            # Translate
            translated_code_msg = translator.translate(code_msg, src=input_language, dest=output_language).text
            translated_description = translator.translate(description, src=input_language, dest=output_language).text
            
            # Add translated columns
            row[f'code_msg_{output_language}'] = translated_code_msg
            row[f'description_{output_language}'] = translated_description
            
            writer.writerow(row)

def get_available_languages() -> List[Dict[str, str]]:
    """
    Return a list of available languages for translation.
    
    :return: List of dictionaries containing language codes and names
    """
    return [
        {'code': 'en', 'name': 'English'},
        {'code': 'es', 'name': 'Spanish'},
        {'code': 'fr', 'name': 'French'},
        {'code': 'de', 'name': 'German'},
        {'code': 'it', 'name': 'Italian'},
        {'code': 'ja', 'name': 'Japanese'},
        {'code': 'ko', 'name': 'Korean'},
        {'code': 'zh-cn', 'name': 'Chinese (Simplified)'},
        {'code': 'zh-tw', 'name': 'Chinese (Traditional)'},
        # Add more languages as needed
    ]

def main():
    input_file = input("Enter the path to the input CSV file: ")
    output_file = input("Enter the path for the output CSV file: ")
    
    print("\nAvailable output languages:")
    languages = get_available_languages()
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang['name']} ({lang['code']})")
    
    choice = int(input("\nEnter the number of the desired output language: ")) - 1
    output_language = languages[choice]['code']
    
    translate_csv(input_file, output_file, output_language)
    print(f"\nTranslation complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()