from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import datetime

origins = [
    "http://localhost:3000",
]

class Item(BaseModel):
    name: str


app = FastAPI()

items = []

count = 0

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return items

@app.post("/create")
async def create_item(item: Item):
    global count
    items.append({"id": count, "name": item.name, "create_at": datetime.datetime.now()})
    count += 1
    return  {
                "list": items,
                "Success": "Item successfully added"
            }

@app.get("/items/{id_item}")
async def get_item(id_item: int):
    for i in items:
        if i["id"] == id_item:
            return  i
    return  {
                        "list": items,
                        "Error": "ID Not Found"}



@app.delete("/items/{id_item}")
async def delete_item(id_item: int):
    for i in items:
        if i["id"] == id_item:
            items.remove(i)
            return  {
                        "list": items,
                        "Success": "Item successfully deleted"
                    }
    return  {
                "list": items,
                "Error": "ID Not Found"
            }

