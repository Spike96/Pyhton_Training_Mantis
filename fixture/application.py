from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Next method can remove if a page and its elements are uploaded quickly
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def go_to_control_page(self):
        wd = self.wd
        control_link = wd.find_element_by_css_selector("a[href$='manage_overview_page.php']")
        control_link.click()