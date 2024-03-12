import argparse
import asyncio
import psycopg

dbname="COMP3005_A3"
user="postgres"
password="postgres"
host="localhost"
port="5432"
        
async def getAllStudents():
    """
    Retrieves and displays all records from the students table 
    """
    async with await psycopg.AsyncConnection.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM students")
            rows = await cursor.fetchall()
            for row in rows:
                print(row)
  
async def addStudent(first_name:str, last_name:str, email: str, enrollment_date: str): 
    """
    Inserts a new student record into the students table 
    """
    async with await psycopg.AsyncConnection.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")

async def updateStudentEmail(student_id: int, new_email: str): 
    """
    Updates the email address for a student with the specified student_id
    """
    async with await psycopg.AsyncConnection.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(f"UPDATE students SET email='{new_email}' WHERE student_id={student_id}")

async def deleteStudent(student_id: int):
    """
    Deletes the record of the student with the specified student_id
    """
    async with await psycopg.AsyncConnection.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute(f"DELETE FROM students WHERE student_id={student_id}")

def main():
    parser = argparse.ArgumentParser(description='students table - CRUD operations')

    parser.add_argument('--get','-g', action='store_true', help='Retrieves and displays all records from the students table')
    parser.add_argument('--add','-a', nargs=4, metavar=('first_name', 'last_name', 'email', 'enrollment_date'), help='Inserts a new student record into the students table given the first name, last name, email, and enrollement date')
    parser.add_argument('--update','-u',nargs=2, metavar=('student_id', 'email'), help='Updates the email address for a student with the specified student_id')
    parser.add_argument('--delete','-d', metavar='student_id', type=int, help='Deletes the record of the student with the specified student_id')

    args = parser.parse_args()

    if args.get:
        asyncio.run(getAllStudents())
    elif args.add:
        first_name, last_name, email, enrollment_date = args.add
        asyncio.run(addStudent(first_name, last_name, email, enrollment_date))
    elif args.update:
        id, email = args.update
        asyncio.run(updateStudentEmail(id, email))
    elif args.delete:
        #id = args.delete
        asyncio.run(deleteStudent(args.delete))

if __name__ == "__main__":
    main()
    # print("getAllStudents:\n")
    # asyncio.run(getAllStudents())
    # print()
    # print("addStudent:\n")
    # asyncio.run(addStudent('Victoria', 'Malouf', 'victoriamalouf@cmail.carleton.ca', '2024-03-09'))
    # asyncio.run(getAllStudents())
    # print()
    # print("updateStudentEmail:\n")
    # asyncio.run(updateStudentEmail(4, 'victoriam@gmail.com'))
    # asyncio.run(getAllStudents())
    # print()
    # print("deleteStudent:\n")
    # asyncio.run(deleteStudent(4))
    # asyncio.run(getAllStudents())
    # asyncio.run(getAllStudents())
    
