from test_python_mashroom.UI.model.pages.user_page_mid import UserPage

user_page = UserPage()


def test_user_page_mid():

    user_page.open_user_page_only_chat()
    user_page.open_chat_reg()
    user_page.send_message()
    user_page.chek_message()




