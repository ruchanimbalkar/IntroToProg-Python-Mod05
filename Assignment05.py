# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# <Rucha Nimbalkar>, <11/07/2024> <Update the starter file with my name and other details>
# <Rucha Nimbalkar>, <11/08/2024> <Add dictionary variable row{}>
# <Rucha Nimbalkar>, <11/10/2024> <GitHub and Json>
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data : str = ''
student_data: dict = {}  # one row of student data
#row : dict ={} #one row of student data in {"Key" :"Value} format
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME,"r") #open the json file in read mode
    json_data = json.load(file) #Now json_data contains the parsed JSON data as a Python list of dictionaries
    for item in json_data:
        student_first_name = item["FirstName"]
        student_last_name = item["LastName"]
        course_name = item["CourseName"]
        student_data ={"FirstName" :student_first_name,"LastName" :student_last_name,"CourseName" : course_name}
        students.append(student_data)
    file.close() #close the file
except FileNotFoundError as e: #Handle FileNotFoundError
    print("File not found!")
    print("---Technical Error Message")
    print(e, e.__doc__, type(e), sep="\n")
    print("Creating new file , since file does not exist.")
    file = open(FILE_NAME, "w")
    json.dump(students, file)
except JSONDecodeError as e: #HandleJSONDecodeError
    print("Data in file is invalid! Resetting it.")
    file = open(FILE_NAME, "w")
    json.dump(students, file)
    print(e, e.__doc__, type(e), sep="\n")
except Exception as e:#Handle general (unexpected non-specific) error
    print("There was a non-specific error!\n")
    print("--- Technical Error Message ---")
    print(e,e.__doc__, type(e), sep="\n")
finally:
    if file.closed == False:
        file.close() #close the file if it is not closed.

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e) #prints the custom message
            print("--- Technical Error Message")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was aa non-specific error!\n")
            print("--- Technical Error Message")
            print(e.__doc__, type(e), sep ="\n")

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("="*70)
        for student in students:
            student_first_name = student["FirstName"]
            student_last_name = student["LastName"]
            course_name = student["CourseName"]
            print(f"Student {student_first_name} {student_last_name} is registered for {course_name}.")
        print("="*70)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        '''file = open(FILE_NAME, "w") #This is the code from the starter file and it is commented because it is not relevant to this assignment.
        for student in students:
            csv_data = f"{student[0]},{student[1]},{student[2]}\n"
            file.write(csv_data)
        file.close()'''
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            print("-" * 60)
            for student in students:
                print(f" 'FirstName' :{student["FirstName"]},'LastName': {student["LastName"]},'CourseName':{student["CourseName"]}")
            print("-" * 60)
            continue

        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("---Technical Error Message")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("---Technical Error Message")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if file.closed == False:
                file.close()


    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
