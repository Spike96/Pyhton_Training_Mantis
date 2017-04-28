
def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.delete()
    app.session.logout()