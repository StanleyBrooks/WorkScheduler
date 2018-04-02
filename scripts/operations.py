
def monday(employee_preferences):
    #Show all  employees without fixed schedules that are available on monday
    monday_availability_non_fixed = employee_preferences.loc[(employee_preferences["day1"] != "Monday") 
                                                & (employee_preferences["day2"] != "Monday") 
                                                & (employee_preferences["set_schedule"] == "no"),
                                                ["first_name", "last_name", "position", "shift"]]

    #Find employees with fixed schedules that are available on monday
    monday_availability_fixed = employee_preferences.loc[(employee_preferences["day1"] != "Monday") 
                                                & (employee_preferences["day2"] != "Monday") 
                                                & (employee_preferences["set_schedule"] == "yes") 
                                                    & (employee_preferences["position"] != "PT"),
                                                ["first_name", "last_name", "position", "shift"]]

    #Append dataframes together
    monday_availability = monday_availability_non_fixed.append(monday_availability_fixed)

    #Get the number available workers
    number_of_workers_monday = len(monday_availability)

    print(monday_availability)
    print("On monday there are {} available employees".format(number_of_workers_monday))
    return employee_preferences

monday(employee_preferences)