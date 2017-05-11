
from model.project import Project
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project_mantis(app):
    project = Project(name=random_string("name", 10), description=random_string("description", 20))
    new_project = project
    old_projects = app.soap.soap_project_list("administrator", "root")
    app.project.create(new_project)
    new_projects = app.soap.soap_project_list("administrator", "root")
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


# '''def test_add_project_mantis(app):
#     old_projects = app.project.get_project_list()
#     project = Project(name=random_string("name", 10), description=random_string("description", 20))
#     app.project.create(project)
#     new_projects = app.project.get_project_list()
#     old_projects.append(project)
#     assert sorted(old_projects, key=Project.key) == sorted(new_projects, key=Project.key)'''



# '''def test_add_project(app):
#     old_projects = app.project.get_project_list()
#     app.project.create()
#     new_projects = app.project.get_project_list()
#     assert len(old_projects) + 1 == len(new_projects)'''

