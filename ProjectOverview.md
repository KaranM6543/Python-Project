This project is a Database-driven Employee Management System built in Python, designed to manage employee records stored in a MySQL database. The system provides several key functionalities:

Add Employee: Inserts a new employee record into the Employees table in the database.

Remove Employee: Deletes an existing employee’s record based on their unique identifier.

Promote Employee: Updates the position or other attributes of an employee to reflect their promotion.

Display Employees: Retrieves and displays a list of all existing employees from the database.

Edit Employee Data: Allows for modifications to an existing employee’s details, such as their name, position, or salary, based on their unique identifier.

The system enables real-time updates to employee records, with each function interacting directly with the database. For example, the Add_Employee function inserts new data, the Remove_Employee function deletes specific records, and the Promote_Employee function updates employee positions. The Edit_Employee_Data function allows for modifying an employee's information. By connecting the application to a MySQL database, the system ensures that employee information remains persistent, with all data being safely stored in the database and intact even after the program is closed and reopened multiple times.

There are following steps :

Step 1: Database Connection
To connect the Employee Management System to a MySQL database, we use the mysql.connector library in Python. This step establishes the communication between the Python script and the MySQL database, enabling the program to perform operations such as adding, removing, and editing employee records.

Step 2: Get the valid input from the user
The get_valid_input function is designed to prompt the user for input and ensure that the entered value is a valid integer. It repeatedly asks the user for input until a valid integer is provided.

Step 3: Get the non empty input
The non_empty_input function is designed to prompt the user for input and ensure that the entered value is both non-empty and not a number. 

Step 4: Get valid salary input
The get_valid_salary function is designed to prompt the user for input and ensure that the entered salary is a valid positive number. 

Step 5: Check Employee Function
The check_employee function takes an employee's ID as a parameter and checks whether a record with the given ID exists in the employee database. This is done by executing a SQL query to search for the employee's details, and the function uses cursor.rowcount to count the number of matching rows returned by the query. 

step 6: Add Employee Function
The Add Employee function prompts the user to enter an Employee ID. It then uses the check_employee function to verify whether an employee with the provided ID already exists in the database. If no matching employee is found, the system proceeds to ask for additional details such as the employee's name, position, and salary.

Step 7: Remove Employee Function
The Remove Employee function prompts the user to enter the Employee ID of the employee to be removed. The function uses the check_employee function to verify whether the employee with the given ID exists in the database. If the employee's details are found, the function proceeds to delete the corresponding record based on the provided ID, effectively removing the employee from the system.

Step 8: Promote Employee Function
The Promote Employee function prompts the user to enter the Employee ID of the employee to be promoted. It then uses the check_employee function to verify whether the employee with the given ID exists in the database. If the employee’s details are found, the system requests the amount by which the employee’s salary should be increased.
After receiving valid input, the function updates the employee's salary by adding the specified amount to their current salary, effectively promoting the employee and reflecting the new salary in the database.

Step 9: Edit Employee Data Function
The Edit Employee Data function prompts the user to enter the Employee ID of the employee whose details are to be updated. It uses the check_employee function to verify whether an employee with the given ID exists in the database. If the employee’s details are found, the system proceeds to retrieve the current data for that employee using a SELECT query.
Once the existing employee details are fetched, the function then asks the user to provide the updated name, position, and salary for the employee.
After collecting the updated information, the function executes an UPDATE query to modify the employee's details in the database, updating the employee's name, position, and salary with the new values.

Step 10: Display Employees Function
The Display Employees function is simply a select query of SQL which fetches all the records stored in the employee details table and prints them line by line.

Step 11: Menu Function
The menu function serves as the main interface for the user, allowing them to interact with the Employee Management System. It continuously displays a menu of available operations and prompts the user to choose one.

