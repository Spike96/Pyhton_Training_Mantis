from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_delete_project(app):
    if app.project.count() == 0:
        project = Project(name=random_string("name", 10), description=random_string("description", 20))
        app.project.create(project)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)




'''def test_delete_project(app):
    username = "administrator"
    password = "root"
    project_name = "new project"
    if app.project.count() == 0:
        app.project.create()
    else:
        app.project.delete()
    assert app.soap.soap_project_list(username, password, project_name)'''