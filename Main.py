# ------------------------------------------------------------------------ #
# Title: Assignment09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# P.Timchenko ,6.6.2021,Downloaded and added to File
# ------------------------------------------------------------------------ #
# Import the modules
if __name__ == "__main__":
    from DataClasses import Employee as EMP
    from ProcessingClasses import FileProcessor as FP
    from IOClasses import EmployeeIO as EIO
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Declare the variables
file_name = "EmployeeData.txt"
list_of_employees = []
choice = ""

# Load data from file into a list of employee objects when script starts
lstFile = FP.read_data_from_file(file_name)
for line in lstFile:
    list_of_employees.append(EMP(line[0], line[1], line[2].strip()))


while True:
    EIO.print_menu_items()  # Show user a menu of options
    choice = EIO.input_menu_options()  # Get user's menu option choice

    if choice == "1":  # Show user current data in the list of employee objects
        EIO.print_current_list_items(list_of_employees)
    elif choice == "2":  # Let user add data to the list of employee objects
        try:
            objEmployee = EIO.input_employee_data()
            list_of_employees.append(objEmployee)
            print(objEmployee, "has been added.")
        except Exception as e:
            print("\n", e, "\n")
    elif choice == "3":  # let user save current data to file
        FP.save_data_to_file(file_name, list_of_employees)
        print("The list has been saved.")
    elif choice == "4":  # Let user exit program
        print("Goodbye")
        break
    else:
        print("Please only choose from 1 - 4.")
