import allure

@allure.feature('Contact_us')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Contact Us Form')
def test_contact_us(home_page, contace_page):
    with allure.step('Open market site'):
        home_page.navigate_to_homepage()

    with allure.step('Verify that home page is visible successfully'):
        home_page.verify_homepage_is_visible()

    with allure.step("Click on 'Contact Us' button"):
        home_page.navigate_to_contact_us()

    with allure.step('Verify "GET IN TOUCH" is visible'):
        contace_page.verify_get_in_touch()

    with allure.step('Enter name, email, subject, message. Upload file and click "Submit"'):
        contace_page.fill_form('Alibek', 'admin2000@gmail.com', 'Nima u', 'Nimajon nimani nima qilding', 'files/file.txt')

    with allure.step('Verify success message "Success! Your details have been submitted successfully." is visible'):
        contace_page.verify_success_msg()

    with allure.step('Click "Home" button and verify that landed to home page successfully'):
        contace_page.click_home_button()