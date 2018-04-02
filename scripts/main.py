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

    #set strings to lowercase, leave everything else alone, this should help when dealing with strings (can re-Caps later for output)
    employee_preferences = employee_preferences.apply(lambda x: x.str.lower() if(x.dtype == 'object') else x)

    #Show all  employees without fixed schedules that are available on monday
    monday_availability_non_fixed = employee_preferences.loc[(employee_preferences["day1"] != "monday") 
                                                & (employee_preferences["day2"] != "monday") 
                                                & (employee_preferences["set_schedule"] == "no"),
                                                ["first_name", "last_name", "position", "shift"]]

    #Find employees with fixed schedules that are available on monday
    monday_availability_fixed = employee_preferences.loc[(employee_preferences["day1"] != "monday") 
                                                & (employee_preferences["day2"] != "monday") 
                                                & (employee_preferences["set_schedule"] == "yes") 
                                                & (employee_preferences["position"] != "pt"),
                                                ["first_name", "last_name", "position", "shift"]]

    #Append dataframes together
    monday_availability = monday_availability_non_fixed.append(monday_availability_fixed)

    #Get the number available workers
    number_of_workers_monday = len(monday_availability)

    print(monday_availability)
    print("On Monday there are {} available employees".format(number_of_workers_monday))


def main():
    #Create pandas dataframe out of csv file
    create_df_from_csv()


if __name__ == '__main__':
    main()
