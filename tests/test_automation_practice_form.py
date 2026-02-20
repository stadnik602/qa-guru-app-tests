from selene import browser, have, command

#given
first_name_element = browser.element('input[data-testid="firstName"]')
last_name_element = browser.element('input[data-testid="lastName"]')
email_element = browser.element('input[data-testid="email"]')
phone_number_element = browser.element('input[data-testid="phone"]')
genders_element = {
    'Male': browser.element('[data-testid="gender"][value="Male"]'),
    # 'Female': browser.all('[data-testid="gender"]'),
    'Female': browser.element('[data-testid="gender"][value="Female"]'),
    'Other': browser.element('[data-testid="gender"][value="Other"]')
}

submit_button_element = browser.element('[type="submit"]')

results_rows_element = browser.all('[class="MuiGrid-root css-1tz2jme"] div div')

def test_successful_student_registration():
    #when
    browser.open('https://app.qa.guru/automation-practice-form/')
    browser.element('[data-testid="ClearIcon"]').click()
    first_name_element.type('John')
    last_name_element.type('Snow')
    email_element.type('john.s@gmail.com')
    phone_number_element.type('999 999 9999')
    # genders_element.get('Female').element_by(have.value('Female')).click()
    genders_element.get('Other').click()
    submit_button_element.perform(command.js.scroll_into_view).click()

    #then
    results_rows_element.should(have.exact_texts(
        ('firstName', 'John'),
        ('lastName', 'Snow'),
        ('email', 'john.s@gmail.com'),
        ('gender', 'Other'),
        ('phone', '+1 999 999 9999')
    ))
    pass