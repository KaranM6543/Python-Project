from idlelib.pyparse import trans
from multiprocessing.managers import Value

import mysql.connector

try :
    con = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    password = "Mehta1@karan",
    database = "EmployeeManagement"
    )
    cursor = con.cursor()
    print("Database connection establised")


except mysql.connector.Error as err:
   print(f"Error: {err}")
   exit()

def get_valid_input (prompt):
   while True:
      try:
         value = int(input(prompt))
         return value
      except ValueError  as e:
         print("Invalid Input! Please try again")

def non_empty_input(prompt):
   while True:
      value = input(prompt).strip()
      if value and not value.isdigit():
         return value
      else:
         print("Invalid Input! Try again (Cannot be a number).")

def get_valid_salary(prompt):
   while True:
      salary = get_valid_input(prompt)
      if salary > 0:
         return salary
      else:
         print("Salary cannot be in negative! Try again")




def check_employee(id):
   sql=  'SELECT * FROM employees WHERE id = %s'
   data = (id,)

   cursor.execute(sql,data)
   cursor.fetchall()

   return cursor.rowcount == 1


def add_employee():
   id = get_valid_input("Enter the employee id: ")

   if check_employee(id):
      print("Employee id is already exists")
      return
   else:
      name = non_empty_input("Enter employee name: ")
      post = non_empty_input("Enter employee post: ")
      salary = get_valid_salary("Enter employee Salary: ")

   sql = 'INSERT INTO employees (id,name,post,salary) VALUES (%s,%s,%s,%s)'
   data = (id,name,post,salary)

   print(f"Executing Sql: {sql}")
   print(f"Data: {data}")


   try:
      cursor.execute(sql,data)

      con.commit()
      print("Employee details added successfully")

   except mysql.connector.Error as err:
      print(f"Error : {err}")
      con.rollback()


def remove_employee():
   id = get_valid_input("Enter the employee id: ")

   if not check_employee(id):
      print("Enter employee id is not exist")
      return
   else:
      sql = 'DELETE FROM employees WHERE id = %s'
      data = (id,)

   try:
      cursor.execute(sql,data)

      con.commit()
      print("Entered id data is deleted")

   except mysql.connector.Error as err:
      print(f"Error : {err}")
      con.rollback()



def promote_employee():

   id = get_valid_input("Enter the employee id: ")

   if not check_employee(id):
      print("Enter employee id is not exist")
      return
   else:
      try:
         Ammount = get_valid_salary("Enter increase in salary:")

         sql_select = 'SELECT salary FROM employees WHERE id = %s'
         data = (id,)

         cursor.execute(sql_select,data)

         current_salary = cursor.fetchone()[0]
         update_salary = current_salary + Ammount

         sql_update = 'update employees set salary= %s where id = %s'
         data_update = (update_salary,id)

         cursor.execute(sql_update,data_update)

         con.commit()
         print("Employee salary has been updated")


      except (ValueError,mysql.connector.Error) as e:
         print(f"Error: {e}")
         con.rollback()

def edit_employee_data():
   id = get_valid_input("Enter Employee Id: ")
   if not check_employee(id):
      print("Employee data in not found")
      return
   else:
      try:
         sql_select = 'SELECT * FROM employees WHERE id = %s'
         data_select = (id,)
         cursor.execute(sql_select,data_select)
         details = cursor.fetchall()

         name = non_empty_input("Enter Employee updated name: ")
         post = non_empty_input("Enter Employee updated position: ")
         salary = get_valid_salary("Enter employee updated salary: ")

         updated_sql = 'UPDATE employees SET name = %s , post= %s , salary = %s WHERE id = %s'
         updated_data = (name,post,salary,id)

         cursor.execute(updated_sql, updated_data)
         con.commit()
         print("Employee data has been updated")

      except mysql.connector.Error as err:
         print(f"Error: {err}")
         con.rollback()




def display_employees():
   try:
      sql = 'SELECT * FROM employees'


      cursor.execute(sql)
      employees = cursor.fetchall()

      for employee in employees:
         print("Employee id:" ,employee[0])
         print("Employee name:", employee[1])
         print("Employee post:", employee[2])
         print("Employee salary:", employee[3])
         print("_________________________________")

   except mysql.connector.Error as err:
      print(f"Error: {err}")
      con.rollback()



def menu():
   while True:
      print("\nWelcome to Employee management Record")
      print("Press:")
      print("1 to Add Employee")
      print("2 to Remove Employee")
      print("3 to Promote Employee")
      print("4 to Display Employees")
      print("5 to Update Employee data")
      print("6 to Exit")


      ch = input("Enter your choice: ")

      if ch == '1' :
         add_employee()
      elif ch == '2':
         remove_employee()
      elif ch == '3':
         promote_employee()
      elif ch == '4':
         display_employees()
      elif ch == '5':
         edit_employee_data()
      elif ch == '6':
         print("Exiting the program Good Bye")
         break
      else:
         print("You have entered invalid choice! Please try again")

if __name__ == "__main__":
   menu()

