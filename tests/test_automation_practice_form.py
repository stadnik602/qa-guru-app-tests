from selene import browser
def test_successful_student_registration():
    browser.open('https://app.qa.guru/automation-practice-form/')
    browser.element('[data-testid="ClearIcon"]').click()
    pass