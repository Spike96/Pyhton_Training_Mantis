from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        # self.app.open_home_page()
        self.go_to_manage_project()
        self.fill_in_fields(Project(name="new project", description="test_test"))
        # press add project
        wd.find_element_by_xpath("//INPUT[@type='submit']").click()
        # assert creation project
        wd.find_element_by_css_selector("p.bold.bigger-110").text

    def go_to_manage_project(self):
        wd = self.app.wd
        # go to manage project
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("(//INPUT[@type='submit'])[1]").click()

    def fill_in_fields(self, project):
        wd = self.app.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)

    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_manage_proj_for_del()
        # select project
        wd.find_element_by_link_text("new project").click()
        # press and confirm removing
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@class='row']/div/div[2]/form/input[4]").click()

    def go_to_manage_proj_for_del(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        list_proj = []
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()
        for element in wd.find_elements_by_css_selector("i.fa.fa-check.fa-lg"):
            i = element.find_element_by_css_selector("i.fa.fa-check.fa-lg")
            list_proj.append(Project(i=i))
        return list_proj

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_manage_proj_for_del()
        return len(wd.find_elements_by_css_selector(".fa.fa-check.fa-lg"))
