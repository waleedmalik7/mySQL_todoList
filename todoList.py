import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="3407",
    database="testdatabase"
)

mycursor = db.cursor()
exit = False 
# mycursor.execute("CREATE TABLE List (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, task VARCHAR(50) NOT NULL)")

while (not exit):
    print("""Todo List Manager
    ----------------
    1. View all tasks
    2. Add a new task
    3. Delete a task
    4. Exit """)

    print("")
    choice_number = input("Enter your choice: ")
    print("")

    match choice_number:
        case "1":
            print("You have chosen to view the table")
            print("")
            mycursor.execute("SELECT * FROM List")
            for x in mycursor:
                id_val = str(x[0])
                task_val = x[1]
                print(id_val + ".) " + task_val) 
            print("")

        case "2":
            print("You have chosen to add to the table")
            print("")
            task = input("Enter task name: ")
            mycursor.execute("INSERT INTO List (task) VALUES (%s)", (task,))
            db.commit()
            print("")

        case "3":
            print("Delete Task")
            print("")
            task_num = input("Enter id of the task name: ")
            mycursor.execute("DELETE FROM List WHERE id = %s",(task_num,)) #%s is used for values
            db.commit()
            print("")

        case "4":
            print("Exit")
            exit = True
            print("")

        case _:
            print("Wrong input")
            print("")