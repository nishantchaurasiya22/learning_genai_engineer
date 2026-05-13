from fastapi import FastAPI,HTTPException,Path,Query
from mockdata import students
app=FastAPI()

@app.get("/")
def root():
    return {"message":"hello, from fastapi"}

@app.get("/students")
def get_students():
    return students

@app.get("/student/{id}")                  
def get_one_student(id:int=Path(...,description="ID of student",example="nishu",gt=0)): 
    for student in students:
        if student["id"].lower()==id.lower():
            return student
    raise HTTPException(status_code=404,detail="Student not found")

@app.get("/filtered_students")
def filtered_students(
    name:str=Query(
          default=None,
        description="filter student by name",
    ),
    age:int=Query(
          default=None,
         description="filter student by age",
    ),
    student_class:str=Query(
          default=None,
         description="filter student class",
    )
):
    filtered_students=students
    if name:filtered_students = [student for student in filtered_students if student["name"].lower() == name.lower()]
    if age:filtered_students = [student for student in filtered_students if student["age"] == age]
    if student_class:filtered_students = [student for student in filtered_students if student["student_class"].lower() == student_class.lower()]
    return filtered_students