from fastapi import FastAPI
from pydantic import EmailStr, BaseModel
import uvicorn

app = FastAPI()


class User(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello World!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.title()
    return {
        "message": f"Hello {name}",
    }


@app.post("/users/")
def create_user(user: User):
    return {
        "message": "success",
        "user": user.email,
    }


@app.get("/items/")
def list_items():
    return [
        "Item 1",
        "Item 2",
        "Item 3",
    ]


@app.post("/calk/")
def add(a: int, b: int):
    return {
        'a': a,
        'b': b,
        'result': a+b,
    }


@app.get("/items/latest/")
def get_last_item():
    return {
        "last_item": {
            "id": 0,
            "name": "item_name",
        },
    }


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: int):
    return {
        "item_id": item_id,
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
