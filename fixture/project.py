from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("(//INPUT[@type='submit'])[1]").click()
        # fill in fields
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys("new project")
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys("test_test")
        # press add project
        wd.find_element_by_xpath("//INPUT[@type='submit']").click()
        # assert creation project
        wd.find_element_by_css_selector("p.bold.bigger-110").text
        # logout
        # wd.find_element_by_link_text("Logout").click()



