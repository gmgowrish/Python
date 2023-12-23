import string

file_path = 'Tools/read.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        lower_case = text.lower()
        cleaned_txt = lower_case.translate(str.maketrans('', '', string.punctuation))
        print(cleaned_txt)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
