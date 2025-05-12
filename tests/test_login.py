import allure
from playwright.sync_api import expect

@allure.feature('Login')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Login with valid user data')
def test_successful_login(home_page, login_page):
    with allure.step('Open market site'):
        home_page.navigate_to_homepage()

    with allure.step('Verify that home page is visible successfully'):
        home_page.verify_homepage_is_visible()

    with allure.step("Click on 'Signup / Login' button"):
        home_page.navigate_to_login()

    with allure.step('Verify "Login to your account" is visible'):
        login_page.verify_login_to_your_acc_is_visible()

    with allure.step('Enter correct email address and password'):
        login_page.login('admin2000@gmail.com', 'admin2000')

    with allure.step('Verify that "Logged in as username" is visible'):
        assert login_page.is_logged_in()

@allure.feature('Login')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Login with invalid user data')
def test_failure_login(home_page, login_page):
    with allure.step('Open market site'):
        home_page.navigate_to_homepage()

    with allure.step('Verify that home page is visible successfully'):
        home_page.verify_homepage_is_visible()

    with allure.step("Click on 'Signup / Login' button"):
        home_page.navigate_to_login()

    with allure.step('Verify "Login to your account" is visible'):
        login_page.verify_login_to_your_acc_is_visible()

    with allure.step('Enter incorrect email address and password'):
        login_page.login('invaliduser@gmail.com', 'invaliduser')

    with allure.step('Verify error "Your email or password is incorrect" is visible'):
        assert login_page.have_error_msg()

@allure.feature('Logout')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing logout user')
def test_logout_user(home_page, login_page):
    with allure.step('Login'):
        test_successful_login(home_page, login_page)
    
    with allure.step('Click "Logout" button'):
        home_page.logout_button.click()

    with allure.step('Verify that user is navigated to login page'):
        expect(home_page.page).to_have_url('https://automationexercise.com/login')