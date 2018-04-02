import pandas as pd

def create_df_from_csv():
    #Csv data to load into pandas dataframe
    file = '.././input/preferences.csv'

    #Columns in csv file and corresponding data types
    DATATYPES = {'employeeID': int,
                'first_name': str,
                'last_name': str,
                'position': str,
                'day1': str,
                'day2': str,
                'shift': str,
                'set_schedule': str}

    #Assigned values for pandas to consider to be Null
    NA=['N/A','null', '0', 'NaN', 'NaT']

    #Read the csv data into dataframe
    employee_preferences = pd.read_csv(file, dtype=DATATYPES, na_values=NA, encoding="utf-8")

    #Set employee_ID to index
    employee_preferences.set_index('employeeID', inplace=True)
    return employee_preferences

create_df_from_csv()