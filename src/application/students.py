# import asyncio
import psycopg2


def getAllStudents():
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def addStudent(first_name:str, last_name:str, email: str, enrollment_date: str):
    with conn.cursor() as cursor:
        cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")
        conn.commit()
        


"""
async def getAllStudents():
    async with psycopg2.connect(dbname='COMP3005_A3', user="postgres", password="postgres", host="localhost", port="5432") as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM students")
            rows = await cursor.fetchall()
            for row in rows:
                print(row)
"""   

if __name__ == "__main__":
    try :
        conn = psycopg2.connect(dbname='COMP3005_A3', user="postgres", password="postgres", host="localhost", port="5432")
    except psycopg2.OperationalError as e:
        print(f'Error: {e}')
        exit(1)
    getAllStudents()
    addStudent('Victoria', 'Malouf', 'victoriamalouf@cmail.carleton.ca', '2024-03-09')
    
