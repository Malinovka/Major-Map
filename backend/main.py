from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
async def get_sqlite_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Major")
    major_rows = cursor.fetchall()
    print(len(major_rows))
    
    cursor.execute("SELECT * FROM Courses")
    course_rows = cursor.fetchall()
    print(len(course_rows))
    
    conn.close()

    major_data = []
    for row in major_rows:
        row_data = {"name": row[0], "year": row[1]}
        major_data.append(row_data)

    course_data = []
    for row in course_rows:
        row_data = {"Courses_Name": row[0], "Courses_Code_Name": row[1], "Courses_Code_Number": row[2], "Number_of_Credits": row[3], "Course_Description": row[4]}
        course_data.append(row_data)

    return {"major_data": major_data, "course_data": course_data}


#async def get_sqlite_version():
#    conn = sqlite3.connect("database.db")
#    cursor = conn.cursor()
 #   cursor.execute("SELECT sqlite_version()")
 #   result = cursor.fetchone()[0]
 #   conn.close()
 #   return {"message": result}


