from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get("/")
async def get_sqlite_version():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    result = cursor.fetchone()[0]
    conn.close()
    return {"message": result}