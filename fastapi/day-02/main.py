from fastapi import FastAPI,Path,Query,HTTPException
from mockdata import students
from pydantic import BaseModel
app=FastAPI()

class Student(BaseModel):
   id:int
   name:str
   age:int
   student_class:str

@app.get("/")
def root():
    return {"message":"hello,from fastapi"}

@app.get("/students")
def get_students():
    return students

@app.get("/student/{id}")
def get_student(id:int=Path(...,description="ID of student",example=1,gt=0)):
    for student in students:
     if student["id"]==id:
        return student
    raise HTTPException(status_code=404,detail="Student not found")

@app.get("/filtered")
def filtered_data(
   name:str=Query(None,description="filter student data by name",min_length=2,example="nishu"),
   age:int=Query(None,description="Filter student data by age",example=18,gt=1)
):
  result=students
  if name:
     result=[student for student in result if student["name"].lower()==name.lower()]
  if age:
     result=[student for student in result if student["age"]==age]
  if not result:
      
     if name and age:
        detail = f"student not found of name {name} and age {age}"
     elif name:
        detail = f"student not found of name {name}"
     elif age:
        detail = f"student not found of age {age}"
     raise HTTPException(status_code=404,detail=detail)
  return result
    
@app.post("/create")
def create_student(student:Student):
   students.append(student.model_dump())
   return {"message":"add ho gaya","student":students}

@app.patch("/update/{id}")
def updated_student(
    id: int = Path(description="ID of student", example=1, gt=0),
    updated: Student = None
):
    for index, student in enumerate(students):
        if student["id"] == id:
            students[index] = updated.model_dump()
            return {"message": "update ho gaya", "student": updated}
    raise HTTPException(status_code=404, detail=f"student not found of id {id}")

@app.delete("/delete/{id}")
def delete_student(
   id:int=Path(description="ID  of student",example=1,gt=0),
):
   for index,student in enumerate(students):
      if student["id"]==id:
         deleted_student=students.pop(index)
         return {"message":"Student deleted succesfully","student":deleted_student}
   raise HTTPException(status_code=404, detail=f"student not found of id {id}")
