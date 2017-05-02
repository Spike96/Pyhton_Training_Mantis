

'''def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create()
    old_projects = app.project.get_project_list()
    app.project.delete()
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)'''
    # app.session.logout()


def test_delete_project(app):
    username = "administrator"
    password = "root"
    project_name = "new project"
    if app.project.count() == 0:
        app.project.create()
    else:
        app.project.delete()
    assert app.soap.soap_project_list(username, password, project_name)