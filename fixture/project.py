from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_manage_project(wd)
        self.fill_in_fields(wd, name="new project", description="test_test")
        # press add project
        wd.find_element_by_xpath("//INPUT[@type='submit']").click()
        # assert creation project
        wd.find_element_by_css_selector("p.bold.bigger-110").text

    def go_to_manage_project(self, wd):
        # go to manage project
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("(//INPUT[@type='submit'])[1]").click()

    def fill_in_fields(self, wd, name, description):
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(description)

    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        # go to manage project
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()
        # select project
        wd.find_element_by_link_text("new project").click()
        # press and confirm removing
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//div[@class='row']/div/div[2]/form/input[4]").click()




