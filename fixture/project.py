from model.project import Project
import random

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.go_to_manage_project()
        self.fill_in_fields(project)
        # press add project
        wd.find_element_by_xpath("//INPUT[@type='submit']").click()
        # assert creation project
        wd.find_element_by_css_selector("p.bold.bigger-110").text

    def go_to_manage_project(self):
        wd = self.app.wd
        # go to manage project
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text("Управление проектами").click()
        wd.find_element_by_xpath("(//INPUT[@type='submit'])[1]").click()

    def fill_in_fields(self, project):
        self.change_field_value('project-name', project.name)
        self.change_field_value('project-description', project.description)
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)


    def delete(self, id):
        wd = self.app.wd
        # self.app.open_home_page()
        self.go_to_manage_proj_for_del()
        self.select_project()
        wd.find_element_by_xpath("//form[@id='project-delete-form']/fieldset/input[3]").click()
        wd.find_element_by_xpath("//input[4]").click()
        self.project_cache = None

    def select_project(self):
        wd = self.app.wd
        element_list = wd.find_elements_by_css_selector("a[href^='manage_proj_edit_page.php?project_id']")
        id = random.randrange(1, len(element_list))
        element = element_list[id]
        element.click()

    def go_to_manage_proj_for_del(self):
        wd = self.app.wd
        # self.app.open_home_page()
        wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
        wd.find_element_by_link_text("Управление проектами").click()

    def get_project_list(self):
        wd = self.app.wd
        # self.app.open_home_page()
        list_proj = []
        wd.find_element_by_css_selector(".menu-icon.fa.fa-gears").click()
        wd.find_element_by_link_text("Управление проектами").click()
        for element in wd.find_elements_by_xpath("//tbody/tr/td/a"):
            # text = element.text
            text = element.find_element_by_xpath("//tr/td/a").text
            list_proj.append(Project(name=text))
        return list_proj

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.go_to_manage_proj_for_del()
        return len(wd.find_elements_by_css_selector(".fa.fa-check.fa-lg"))
