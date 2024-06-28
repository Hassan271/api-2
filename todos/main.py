# for run api you need 4 infor ...................
# Route 
# method = get / post / 
# ip address 
# posrt # 8012

# 1----------------------
from fastapi import FastAPI
import uvicorn 

# 2----------------------
app = FastAPI()

# 3  app called the function form outside ------------------------
# http://127.0.0.1:8012/gettodos/    ..................................

@app.get("/gettodos")

def gettodos():
    print("Print get todos APi ")
    return "Return gettodos " 
# called manually-------------------
# gettodos()

# # POST API-------------------------
@app.post("/postTodo")

def postTodo():
    print("print postTodo ")
    return "Return postTodo"


# Define function uvcorn ----------------------
# 
def start():
    # todos is folder and main.py id file ,, reload=True Refresh auto
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8012, reload=True)
    
    

# # http://127.0.0.1:8011/students/    ..................................

# # app = FastAPI()

# students = [
#     {
#     "userName": "Hassan",
#     "rollNo":   1111
#     },
#     {
#     "userName": "Hassan2",
#     "rollNo":   2222
#     }
    
#         ]

# @app.get("/students")
# def getStudents():
#     return students