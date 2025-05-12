import allure

@allure.feature('Signup')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Register user with existing email')
def test_failure_signup(home_page, login_page):
    with allure.step('Open market site'):
        home_page.navigate_to_homepage()

    with allure.step('Verify that home page is visible successfully'):
        home_page.verify_homepage_is_visible()

    with allure.step("Click on 'Signup / Login' button"):
        home_page.navigate_to_login()

    with allure.step('Verify "New User Signup!" is visible'):
        login_page.verify_reg_new_user()

    with allure.step('Enter name and already registered email address'):
        login_page.signup('Alivoy', 'admin2000@gmail.com')

    with allure.step('Verify error "Email Address already exist!" is visible'):
        assert login_page.have_reg_error_msg()