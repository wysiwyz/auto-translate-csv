# Translate made easy
## Background
This repository aims to solve an issue when you have a whole bunch of csv file, and that you need to translate a few columns from source language into languages options like English, Spanish, or other majority languages.

## Library utilized 
- `csv`
- `io`
- `typing`
- `langdetect`
- `googletrans`

## Logics (to be finalized at later stage)

1. The translated_code_msg and the translated_description will be displayed in columns after description.

2. The input language should be auto-detectable, meaning this app can tell which language the input is. If not possible, then An user should be able to choose from a variety of language inputs.

3. An user should also be able to select which output language they want to get translated.

4. An user will get the output in CSV format and the column would look like below. 
   - In the newly added columns, the `<LanguagueOutput>` refers to the output language as chosen by the user.

     |# | column-a | column-b | code_msg | description | code_msg_\<LanguagueOutput> | description_\<LanguagueOutput> |
     |--|----------|----------|----------|-------------|----------------------------|------------------------------|

## Installing library

```
pip install langdetect googletrans==3.1.0a0
```

```
python csv_translator.py
```

```
pip install Faker
```

```
python generate_test_csv.py
python csv_translator.py
```

## Memos from author
This repository was first created with the motivation to brush up ~~rotten~~ Python coding skills.

