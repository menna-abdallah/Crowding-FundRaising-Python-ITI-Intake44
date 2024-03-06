from datetime import datetime
import json
from models.projects import Project
from functions.helper import is_number,is_string,is_valid_date,print_project

def load_projects():
    try:
        with open("projects.json", "r") as file:
            projects_data = json.load(file)
            projects = [Project(project_data["title"], project_data["details"],
                                project_data["total_target"], 
                                datetime.strptime(project_data["start_date"], "%Y-%m-%d"), 
                                datetime.strptime(project_data["end_date"], "%Y-%m-%d"), 
                                project_data["owner"])
        for project_data in projects_data]
        return projects
    except FileNotFoundError:
        return []

def save_projects(projects):
    projects_data = [{"title": project.title,
                      "details": project.details,
                      "total_target": project.total_target,
                      "start_date": project.start_date.strftime("%Y-%m-%d"),
                      "end_date": project.end_date.strftime("%Y-%m-%d"),
                      "owner": project.owner}
    for project in projects]
    with open("projects.json", "w") as file:
        json.dump(projects_data, file, indent=4)

def create_project(current_user):
    title = input("Enter project title: ")
    while not is_string(title) :
        title = input("Required!\nEnter project title: ")
    details = input("Enter project details: ")
    while not is_string(details):
        details = input("Required! \nEnter project details: ")
    total_target = input("Enter total target amount (EGP): ")
    while not is_number(total_target):
        total_target = input("Required! \nEnter total target amount (EGP): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    while not is_valid_date(start_date):
        start_date = input("Required!\nEnter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    while not is_valid_date(end_date):
        end_date = input("Required! \nEnter end date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    if start_date > end_date or end_date < datetime.now():
        print("Invalid date format!, please TRY again")
        return

    projects = load_projects()
    

    project = Project(title, details, total_target, start_date, end_date, current_user)

    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")

def show_all(current_user):
    projects = load_projects()
    for project in projects:
        if (project.owner == current_user):
           print_project(project)
        else:
            print(f'There are no projects for {current_user}')
        

def update_project(current_user):
    projects = load_projects()
    title_to_update = input("Enter the title of the project to update: ")
    while not is_string(title_to_update) :
        title_to_update = input("Required!!... \nEnter the title of the project to update: ")
    for project in projects:
        if project.owner == current_user and project.title == title_to_update:
            print_project(project)
            project.title = input('Enter new title: ')
            while not is_string(project.title):
                project.title = input("Required!! . . . \nEnter new title: ")
            project.details = input('Enter new details: ')
            while not is_string(project.details):
                project.details = input("Required!!. . . \nEnter new details: ")
            project.total_target = input('Enter new total target amount (EGP): ')
            while not is_number(project.total_target):
                project.total_target = input("Required!! . . .\nEnter new total target amount (EGP): ")
            project.start_date = input('Required! Enter start date (YYYY-MM-DD): ')
            while not is_valid_date(project.start_date):
                project.start_date = input("Required! Enter start date (YYYY-MM-DD): ")
            project.end_date = input('Enter end date (YYYY-MM-DD): ')
            while not is_valid_date(project.end_date):
                project.end_date = input("Required! Enter end date (YYYY-MM-DD): ")
            project.start_date = datetime.strptime(project.start_date, "%Y-%m-%d")
            project.end_date = datetime.strptime(project.end_date, "%Y-%m-%d")
            if project.start_date > project.end_date or project.end_date < datetime.now():
                print("Invalid date format!, please TRY again")
                return
            save_projects(projects)
            print("Project updated successfully!")
            return
    print("Project not found or you don't have permission to update it.")

def delete_project(current_user):
    projects = load_projects()
    title_to_delete = input("Enter the title of the project to delete: ")
    while not is_string(title_to_delete) :
        title_to_delete = input("Required!!... \nEnter the title of the project to delete: ")
    for index, project in enumerate(projects):
        if project.owner == current_user and project.title == title_to_delete:
            print_project(project)
            del projects[index]
            save_projects(projects)
            print("Project deleted successfully!")
            return
    print("Project not found or you don't have permission to delete it.")

def search_projects_by_date(current_user):
    projects = load_projects()
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    while not is_valid_date(start_date_str):
        start_date_str = input("Required! Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    while not is_valid_date(end_date_str):
        end_date_str = input("Required! Enter end date (YYYY-MM-DD): ")

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    found_projects = [project for project in projects if project.owner == current_user and project.start_date >= start_date and project.end_date <= end_date]
    
    if found_projects:
        for project in found_projects:
            print_project(project)
    else:
        print("No projects found within the specified date range.")
