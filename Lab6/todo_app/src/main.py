from fastapi import FastAPI, Body

app = FastAPI()


@app.get("/api")
def first_api():
    return {"msg": "hello_world"}


@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"msg": path_param}


@app.get("/books/")
def first_apiV3(title: str):
    return {"msg": title}



@app.get("/books/create_book/{title}")
def first_apiV4(title, author):
    return {"msg": f"new book {title} author {author}" }


@app.post("/api")
def first_post_api():
    return {"msg": "post api"}


@app.put("/api")
def put_something():
    return {"msg": "put api"}


@app.delete("/delete/something")
def delete_something():
    return {"success": True}
