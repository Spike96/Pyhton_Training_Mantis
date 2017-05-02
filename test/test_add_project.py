
'''def test_add_project(app):
    old_projects = app.project.get_project_list()
    app.project.create()
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)'''


def test_add_project(app):
    username = "administrator"
    password = "root"
    project_name = "new project"
    app.project.create()
    assert app.soap.soap_project_list(username, password, project_name)






