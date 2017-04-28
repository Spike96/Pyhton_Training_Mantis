
def test_add_project(app):
    # old_projects = app.project.get_group_list()
    app.project.create()
    # new_projects = app.project.get_group_list()
    # assert len(old_projects) + 1 == len(new_projects)
    # app.session.logout()