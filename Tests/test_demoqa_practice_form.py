from Models import controls
from Models import pages
from selene.support.conditions import have

def test_demo_qa_form(open_and_close_form):
    pages.fill_fullname("Andrew", "Vasutenko")
    pages.fill_user_email("qqqqq@qqqq.qq")
    controls.select_gender_male()
    pages.fill_user_number_phone("8800555353")
    controls.fill_date_of_birthday("19 April,1993")
    pages.fill_subjects(("Art", "Commerce"))
    controls.select_hobby_music()
    controls.download_picture()
    pages.fill_curent_adress("Russia,Moscow")
    controls.select_state_and_city("rajasthan", "jaipur")
    controls.submit()

    pages.table_result.should(have.text("Andrew"))
    pages.table_result.should(have.text("Vasutenko"))
    pages.table_result.should(have.text("qqqqq@qqqq.qq"))
    pages.table_result.should(have.text("Male"))
    pages.table_result.should(have.text("8800555353"))
    pages.table_result.should(have.text("19 April,1993"))
    pages.table_result.should(have.text("Arts, Commerce"))
    pages.table_result.should(have.text("Music"))
    pages.table_result.should(have.text("meme.jpg"))
    pages.table_result.should(have.text("Russia,Moscow"))
    pages.table_result.should(have.text("Rajasthan"))
    pages.table_result.should(have.text("Jaipur"))