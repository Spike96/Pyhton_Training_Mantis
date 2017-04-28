
def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.create()
    app.session.logout()