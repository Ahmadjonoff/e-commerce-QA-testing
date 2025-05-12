from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.signup_login_button = page.locator('a[href="/login"]')
        self.products_button = page.locator('a[href="/products"]')
        self.cart_button = page.locator('a[href="/view_cart"]')
        self.contact_button = page.locator('a[href="/contact_us"]')
        self.logout_button = page.locator('a[href="/logout"]')

    def navigate_to_homepage(self):
        self.page.goto('https://automationexercise.com/')

    def navigate_to_login(self):
        self.signup_login_button.click()

    def navigate_to_contact_us(self):
        self.contact_button.click()

    def verify_homepage_is_visible(self):
        expect(self.page).to_have_title('Automation Exercise')