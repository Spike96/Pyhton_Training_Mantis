

def test_delete_project(app):
    if app.project.count() == 0:
        app.project.create()
    app.project.delete()
    # app.session.logout()