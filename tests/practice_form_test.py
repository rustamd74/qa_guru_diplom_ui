import datetime
import allure
from demoqa_tests.model.data.user import User, State, City, Subject, Gender, Hobbies
from demoqa_tests.model.pages.practice_form import Practice_form
from allure_commons.types import Severity

automation_form = Practice_form()


@allure.title("Successful fill form")
@allure.tag('web', 'smoke')
@allure.label('owner', 'dzhafarov_ro')
@allure.severity(Severity.CRITICAL)
@allure.feature('registration')
@allure.suite('demoqa')
def test_student_registration():
    student = User(first_name='John',
                   last_name='Doe',
                   email='johndoe@gmail.com',
                   phone_number='2223331110',
                   birthday=datetime.date(2004, 3, 4),
                   subject=[Subject.Computer_Science, Subject.Maths],
                   gender=Gender.Male,
                   hobbies=[Hobbies.Sports, Hobbies.Music],
                   picture='python_label.png',
                   address='221b, Baker street',
                   state=State.Uttar_Pradesh,
                   city=City.Lucknow)
    with allure.step("Open registration form"):
        automation_form.open_page()
    with allure.step("Filling form"):
        automation_form.fill_form(student)
    with allure.step("Checking the registration form"):
        automation_form.assert_registration_student(student)
