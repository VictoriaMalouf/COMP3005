import unittest

from students import *

async def all_records():
    async with await psycopg.AsyncConnection.connect(dbname=dbname, user=user, password=password, host=host, port=port) as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM students")
            rows = await cursor.fetchall()
    return rows

class TestStudents(unittest.TestCase):

    def test_add_student(self):
        rows = asyncio.run(all_records())
        for row in rows:
            print(row)
        # asyncio.run(addStudent('Victoria', 'Malouf', 'victoriamalouf@cmail.carleton.ca', '2024-03-09'))

        
        
