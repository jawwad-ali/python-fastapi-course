from fastapi import FastAPI

app = FastAPI()

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# To get the data from the API, you can use the following endpoint:
# This is only readonly
@app.get("/")
def read_my_message():
    return fruits
