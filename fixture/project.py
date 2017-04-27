from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        self.start_creating_project(wd)
        self.fill_in_fields(wd, Project(name="New_Project", descritpion="Test"))
        self.add_project(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click

    def add_project(self, wd):
        # press add project
        wd.find_element_by_xpath("//input[@value='Add Project'").click
        # assert creation project
        wd.find_element_by_css_selector("p.bold.bigger-110").text

    def fill_in_fields(self, wd, project):
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)

    def start_creating_project(self, wd):
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click
        wd.find_element_by_link_text("Manage Projects").click
        wd.find_element_by_xpath("//input[@value='Create New Project'").click


