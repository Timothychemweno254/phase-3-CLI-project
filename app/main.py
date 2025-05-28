from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, User, Skill, LearningLesson
import os

#db connection
engine = create_engine("sqlite:///skill.db",echo=False )
Session = sessionmaker(bind=engine)

session = Session()

#===========USER===============
def create_user():
    username = input("Enter username: ")
    email =    input("Enter email   : ")
    password = input("Enter password: ")

    if not username or not email or not password:
        print("All fields are required.")
        return

    new_user = User(username=username, email=email, password=password)
    session.add(new_user)
    session.commit()
    print(f"User {username} created successfully.")

def fetch_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")

#FETCH USER
def fetch_user_by_id():
    user_id = input("Enter user ID to fetch: ")
    user = session.query(User).filter_by(id=user_id).first()
    
    if user:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print("User not found.")

#UPDATE USER
def update_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        username = input("Enter new username : ")
        email = input("Enter new email : ")
        password = input("Enter new password : ")
        user.username = username
        user.email = email
        user.password = password
        session.commit()
        print("User updated successfully!")
    else:
        print("User not found!")

#DELETE USER
def delete_user():
    user_id = input("Enter user ID : ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
    else:
        print("User not found!")

#===========SKILL===============
def create_skills():
    name = input("Enter skills title : ")
    goal_description = input("Enter skills description : ")
    user_id = input("Enter user ID : ")
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    learning_lessons = session.query(User).filter_by(id=user_id).first()
    user = session.query(User).filter_by(id=user_id).first()
    if learning_lessons and user:
        skill = Skill(name=name, goal_description=goal_description, user_id=user.id)
        session.add(skill)
        session.commit()
        print(f"skills '{name}' created successfully.")
    else:
        print("User not found. skill creation failed.")
    
def fetch_skillss():
    skills = session.query(Skill).all()
    for skill in skills:
        print(f"ID: {skill.id}, Name: {skill.name}, Description: {skill.goal_description}, User ID: {skill.user_id}")
def fetch_skills_by_id():
    skill_id = input("Enter skill ID : ")
    skill = session.query(Skill).get(skill_id)
    if skill:
        print(f"ID: {skill.id}, Name: {skill.name}, Description: {skill.goal_description}, User ID: {skill.user_id}")
    else:
        print("Skill not found.")

def update_skills():
    skill_id = input("Enter skill ID : ")
    skill = session.query(Skill).get(skill_id)
    if skill:
        name = input("Enter new skills title : ")
        goal_description = input("Enter new skills description : ")
        user_id = input("Enter new user ID : ")

        date_created = datetime.now().strftime("%Y-%m-%d ")

        skill.name = name
        skill.goal_description = goal_description
        skill.user_id = user_id
        session.commit()
        print("Skill updated successfully!")
    else:
        print("Skill not found!")

def delete_skills():
    skill_id = input("Enter skill ID : ")
    skill = session.query(Skill).get(skill_id)
    if skill:
        session.delete(skill)
        session.commit()
        print("Skill deleted successfully!")
    else:
        print("Skill not found!")

#===========LEARNING LESSONS===============
def create_learning_lesson():
    skill_id = input("Enter skill ID :")
    content = input("Enter lesson content: ")
    duration = input("Enter lesson duration (in minutes) : ") 
    notes = input("Enter lesson notes : ")

    learning_lesson = LearningLesson(
    skill_id=skill_id,
    content=content,
    date=datetime.now(),
    duration=duration,
    notes=notes
    )
    session.add(learning_lesson) 
    session.commit()
    print("Learning lesson created successfully.")
def fetch_learning_lessons():
    learning_lessons = session.query(LearningLesson).all()
    for lesson in learning_lessons:
        print(f"ID: {lesson.id}, Skill ID: {lesson.skill_id}, Date: {lesson.date}, Duration: {lesson.duration} minutes, Notes: {lesson.notes}")

def fetch_learning_lesson_by_id():
    lesson_id = input("Enter learning lesson ID : ")
    lesson = session.query(LearningLesson).get(lesson_id)
    if lesson:
        print(f"ID: {lesson.id}, Skill ID: {lesson.skill_id}, Date: {lesson.date}, Duration: {lesson.duration} minutes, Notes: {lesson.notes}")
    else:
        print("Learning lesson not found.")

def update_learning_lesson():
    lesson_id = input("Enter learning lesson ID : ")
    lesson = session.query(LearningLesson).get(lesson_id)
    if lesson:
        skill_id = input("Enter new skill ID : ")
        date = input("Enter new lesson date (YYYY-MM-DD HH:MM:SS) : ")
        duration = input("Enter new lesson duration (in minutes) : ") 
        notes = input("Enter new lesson notes : ")

        lesson.skill_id = skill_id
        lesson.date = datetime.strptime(date, "%Y-%m-%d ")

        lesson.duration = duration
        lesson.notes = notes
        session.commit()
        print("Learning lesson updated successfully!")
    else:
        print("Learning lesson not found!")

def delete_learning_lesson():
    lesson_id = input("Enter learning lesson ID : ")
    lesson = session.query(LearningLesson).get(lesson_id)
    if lesson:
        session.delete(lesson)
        session.commit()
        print("Learning lesson deleted successfully!")
    else:
        print("Learning lesson not found!")

        #CLI INPUTS

def main():
      while True:
        print("============Skill MANAGER=============")
        print("1. Manage Users ")
        print("2. Manage Skills ")
        print("3. Manage Learning Lessons ")
        main_choice = input("Enter your choice : ")

        if main_choice == '1':
            os.system("clear")
            print("============USER MANAGEMENT=============")
            print("1. Create User")
            print("2. List Users")
            print("3. 1fetch User by ID") 
            print("4. Update User")
            print("5. Delete User")

            choice = input("Enter your choice : ")

            if choice == '1':
                create_user()
            elif choice == '2':
                fetch_users()
            elif choice == '3':
                fetch_user_by_id()
            elif choice == '4':
                update_user()
            elif choice == '5':
                delete_user()
            elif choice == '0':
                print("Exiting .")
                break
            else:
                print("Invalid choice. Please try again.")

        elif main_choice == '2':
            os.system("clear")
            print("============SKILL MANAGEMENT=============")
            print("1. Create Skill")
            print("2. List Skills")
            print("3. Fetch Skill by ID")
            print("4. Update Skill")
            print("5. Delete Skill")
            print("0. Exit")

            choice = input("Enter your choice : ")

            if choice == '1':
                create_skills()
            elif choice == '2':
                fetch_skillss()
            elif choice == '3':
                fetch_skills_by_id()
            elif choice == '4':
                update_skills()
            elif choice == '5':
                delete_skills()
            elif choice == '0':
                print("Exiting .")
                break
            else:
                print("Invalid choice. Please try again.")

        elif main_choice == '3':
            os.system("clear")
            print("============LEARNING LESSON MANAGEMENT=============")
            print("1. Create Learning Lesson")
            print("2. List Learning Lessons")
            print("3. Fetch Learning Lesson by ID")
            print("4. Update Learning Lesson")
            print("5. Delete Learning Lesson")
            print("0. Exit")

            choice = input("Enter your choice : ")

            if choice == '1':
                create_learning_lesson()
            elif choice == '2':
                fetch_learning_lessons()
            elif choice == '3':
                fetch_learning_lesson_by_id()
            elif choice == '4':
                update_learning_lesson()
            elif choice == '5':
                delete_learning_lesson()
            elif choice == '0':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")

main()


