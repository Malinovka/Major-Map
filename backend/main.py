from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
async def get_sqlite_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Major")
    major_rows = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Course")
    course_rows = cursor.fetchall()
    
    conn.close()

    major_data = []
    for row in major_rows:
        row_data = {"name": row[0], "year": row[1]}
        major_data.append(row_data)

    course_data = []
    for row in course_rows:
        row_data = {"Course_Name": row[0], "Course_Code_Name": row[1], "Course_Code_Number": row[2], "Credits": row[3], "Description": row[4]}
        course_data.append(row_data)

    return {"major_data": major_data, "course_data": course_data}


#async def get_sqlite_version():
#    conn = sqlite3.connect("database.db")
#    cursor = conn.cursor()
 #   cursor.execute("SELECT sqlite_version()")
 #   result = cursor.fetchone()[0]
 #   conn.close()
 #   return {"message": result}


