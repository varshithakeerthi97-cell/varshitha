from fastapi import FastAPI
app = FastAPI(title="varshitha")


students = [
    {"id" : 1,"name":"a","dept":"python"},
    {"id" : 2,"name":"b","dept":"c"},
    {"id" : 3, "name":"c","dept":"java"},
    {"id" : 4, "name":"d","dept":"python"},
    {"id" : 5, "name":"e","dept":"c"}
]

# path parameters
@app.get("/students/{student_id}")
def get_student_id(student_id: int):
    print(student_id)
    print(type(student_id))
    for student in students:
        if student["id"]== student_id:
            return student
    return{"error":"student not found"}
@app.get("/students")
def get_student_dept(dept : str):
    result = []
    for student in students:
        if student["dept"] == dept:
            result.append(student)
    return result
@app.get("/students")
def home():
    return {"message" : "Hi fastapi"}
@app.get("/name")
def name():
    return {"batch - 576"} 
    