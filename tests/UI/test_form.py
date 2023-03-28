from test_python_mashroom.UI.model.pages.user_page_mid import UserPage


def test_user_page_mid():

    practice_form.open_user_page_only_chat()
    practice_form.open_chat_reg()
    practice_form.send_message()
    practice_form.chek_message()

practice_form = UserPage()


