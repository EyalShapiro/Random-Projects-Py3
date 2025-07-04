import os
import pandas as pd

PATH = os.path.split(os.path.abspath(__file__))[0]
FILE_TXT = PATH + r"\input.txt"
OUTPUT_CSV = PATH + r"\output.csv"


def read_and_tokenize(file_path):
    """הפעולה מקבלת את נתיב הקובץ ומקריאה את התוכן שלו. לאחר מכן,"""
    with open(file_path, "r", encoding="utf-8") as file:
        reading = file.read()
    return reading


def text_to_table_with_pandas(input_text, output_csv, delimiter):
    """
    input_text:הטקס שאנחנו רוצים להעביר לטבלה
    output_csv: מיקום הקובץ רוצים לסים את CSV
    delimiter:התוחם
    """
    # Split the input text into parts using the specified delimiter
    parts = input_text.strip().split(delimiter)

    # Create a DataFrame with the parts
    df = pd.DataFrame({"Part": parts})

    # Write the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    # Example usage
    input_text = read_and_tokenize(FILE_TXT)
    delimiter = ","  # תוחם

    text_to_table_with_pandas(input_text, OUTPUT_CSV, delimiter)
    print("Conversion complete. CSV file saved as output_table.csv")
