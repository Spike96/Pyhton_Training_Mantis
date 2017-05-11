
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
            soap_list=client.service.mc_projects_get_user_accessible(username, password)
            for project in soap_list:
                project_list.append(Project(id=project.id, name=project.name, description=project.description))
            return project_list
        except WebFault:
            return False