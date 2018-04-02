import pandas as pd

def read_csv_with_pandas():
    file = 'preferences.csv'

    DATATYPES = {'employeeID': int,
                'first_name': str,
                'last_name': str,
                'position': str,
                'day1': str,
                'day2': str,
                'shift': str,
                'set_schedule': str}

    NA=['N/A','null', '0', 'NaN', 'NaT']

    employee_preferences = pd.read_csv(file, dtype=DATATYPES, na_values=NA, encoding="utf-8")
    return employee_preferences

read_csv_with_pandas()

employee_preferences.head