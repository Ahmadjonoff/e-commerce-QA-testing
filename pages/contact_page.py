from pages.home_page import HomePage
import time

class ContactPage(HomePage):
    def __init__(self, page):
        self.page = page
        self.get_touch = page.locator('div[class="contact-form"] h2')
        self.contact_name_input = page.locator("input[data-qa='name']")
        self.contact_email_input = page.locator('input[data-qa="email"]')
        self.contact_subject_input = page.locator('input[data-qa="subject"]')
        self.contact_message_input = page.locator('textarea[data-qa="message"]')
        self.contact_upload_file_input = page.locator('input[type="file"]')
        self.contact_submit_button = page.locator('input[data-qa="submit-button"]')
        self.contact_succ_msg = page.locator('div[class="status alert alert-success"]')
        self.contact_home_button = page.locator('a[class="btn btn-success"]')

    def verify_get_in_touch(self):
        return self.get_touch.is_visible()
    
    def fill_form(self, name, email, subject, msg, file_path):
        self.contact_name_input.fill(name)
        self.contact_email_input.fill(email)
        self.contact_subject_input.fill(subject)
        self.contact_message_input.fill(msg)
        self.contact_upload_file_input.set_input_files(file_path)
        time.sleep(1)
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.contact_submit_button.click()

    def verify_success_msg(self):
        return self.contact_succ_msg.is_visible()

    def click_home_button(self):
        self.contact_home_button.click()
        self.verify_homepage_is_visible()