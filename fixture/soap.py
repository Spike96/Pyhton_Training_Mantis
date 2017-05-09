
from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.3.1/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def soap_project_list(self, username, password):
        client = Client("http://localhost/mantisbt-2.3.1/api/soap/mantisconnect.php?wsdl")
        project_list = []
        try:
            for project in client.service.mc_projects_get_user_accessible(username, password):
                project_list.append(Project(id=project.id, name=project.name, description=project.description))
            return True
        except WebFault:
            return False

