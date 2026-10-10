# 这个文件当中才是真正去操作数据库
from model.student import Student


def add_student(student,session):
  session.add(student)
  session.commit()

def update_student(student_info,session):
  session.query(Student).filter(Student.id == student_info.id).update(student_info.__dict__)
  # student = session.query(Student).filter(Student.id == student_info.id).first()
  # student.name = student_info.name
  # student.age = student_info.age
  # student.birthday = student_info.birthday
  session.commit()

def delete_student(id,session):
  session.query(Student).filter(Student.id == id).delete()
  session.commit()

def get_student(id,session):
  student = session.query(Student).filter(Student.id == id).first()
  return student

def get_student_list(session):
  students = session.query(Student).all()
  return students
  