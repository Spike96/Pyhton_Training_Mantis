# from model.project import Project

def create_project(app):
    app.session.login("administrator", "root")
    app.project.create()
