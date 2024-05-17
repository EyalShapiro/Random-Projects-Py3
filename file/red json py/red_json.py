
import json


def Read_Data_Json(file_path):
    """
    פונקציה שקראת נתונים מקובץ JSON.
    
    פרמטרים:
        file_path (str): הנתיב לקובץ JSON.
    
    מחזיר:
        dict: הנתונים מהקובץ JSON כמפה.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
        file.close()

    return data


print(Read_Data_Json("./data.json"))