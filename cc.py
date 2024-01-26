"""

Develop a basic API that can receive data and create a database entry and another API to get list that data .
Additionally, create a script to make a call to that APIs.

"""
from typing import Optional

import uvicorn
from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel

connection = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="localhost")
cursor = connection.cursor()
# cursor.execute("create table l2_test (name varchar(15), age Integer)")
# connection.commit()
# connection.close()
# exit()
app = FastAPI()


class UserSchema(BaseModel):
    name: str
    age: Optional[int]


@app.get("/get_data", status_code=200)
async def get_data_from_db():
    cursor.execute("select * from l2_test")
    all_data = cursor.fetchall()
    return {"output_data": all_data}


@app.post("/store_data", status_code=201)
async def insert_data(user: UserSchema):
    cursor.execute(f"insert into l2_test (name, age) values {user.name, user.age}")
    connection.commit()
    return {"message": f"successfully stored the data of name {user.name}"}

if __name__ == "__main__":
# uvicorn.run("cc:app", host="0.0.0.0", port=5654)
    uvicorn.run("cc:app", port=5654)
