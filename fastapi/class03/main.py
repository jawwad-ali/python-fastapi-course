from fastapi import FastAPI

app = FastAPI()

fruits = ["apple", "banana", "cherry"]

# To take the data from the server
@app.get("/home")
def read_message():
    return fruits

# To send the data to the server
@app.post("/add_fruit")
def add_fruit(phal: str):
    fruits.append(phal)
    return {"message": f"Fruit added: {phal} \n fruits list: {fruits}"}

@app.delete("/delete_fruit")
def delete_fruit(phal):
    if phal in fruits:
        fruits.remove(phal)
        return {"message": f"Fruit deleted: {phal} \n fruits list: {fruits}"}
    else:
        return {"message": f"Fruit not found: {phal} \n fruits list: {fruits}"}