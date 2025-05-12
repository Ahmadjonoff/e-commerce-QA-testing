from pages.home_page import HomePage

class LoginPage(HomePage):
    def __init__(self, page):
        self.page = page
        self.login_your_acc = page.locator('div[class="login-form"] h2')
        self.email_input = page.locator("input[data-qa='login-email']")
        self.password_input = page.locator("input[data-qa='login-password']")
        self.login_btn = page.locator("button[data-qa='login-button']")
        self.logged_in_text = page.locator("a:has-text('Logged in as')")
        self.error_login_msg = page.locator('form[action="/login"] p')

        #for reg
        self.reg_new_user = page.locator("div[class='signup-form'] h2")
        self.reg_name_input = page.locator('input[data-qa="signup-name"]')
        self.reg_email_input = page.locator('input[data-qa="signup-email"]')
        self.reg_signup_button = page.locator('button[data-qa="signup-button"]')
        self.reg_error_msg = page.locator("div[class='signup-form'] p")

    def verify_login_to_your_acc_is_visible(self):
        return self.login_your_acc.is_visible()

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_btn.click()

    def is_logged_in(self):
        return self.logged_in_text.is_visible()
    
    def have_error_msg(self):
        return self.error_login_msg.is_visible()
    
    #for reg
    def verify_reg_new_user(self):
        return self.reg_new_user.is_visible()
    
    def signup(self, name, email):
        self.reg_name_input.fill(name)
        self.reg_email_input.fill(email)
        self.reg_signup_button.click()
    
    def have_reg_error_msg(self):
        return self.reg_error_msg.is_visible()