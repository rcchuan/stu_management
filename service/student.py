
from model.student import Student
from crud.student import add_student, delete_student, get_student, get_student_list, update_student

def add_student_service(student_info,session): 
  # 转化student_info成为学生student对象
  # student = Student(name=student_info['name'], age=student_info['age'], birthday=student_info['birthday'])
  student=Student(**student_info.__dict__)
  #print(type(student))
  add_student(student,session)

def update_student_service(student_info,session): 
  update_student(student_info,session)

def delete_student_service(id,session):
  delete_student(id,session)

def get_student_srevice(id,session):
  return get_student(id,session)

def get_student_list_service(session):
  return get_student_list(session)

  