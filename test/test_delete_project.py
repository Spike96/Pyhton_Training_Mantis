

def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create()
    old_projects = app.project.get_project_list()
    app.project.delete()
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    # app.session.logout()