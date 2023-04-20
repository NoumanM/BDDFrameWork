from Elements.LogoutPageElements  import LogoutPageElements


class LogoutPage(LogoutPageElements):

    def __init__(self, driver):
        super().__init__(driver)

    def click_logout_btn(self):
        self.click_element(self.logout_btn)