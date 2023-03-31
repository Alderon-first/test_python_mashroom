from test_python_mashroom.UI.model.pages.user_page_no_activity import UserPage
from dotenv import load_dotenv

load_dotenv()
user_page = UserPage()


def test_testpage(browser_user_site):
    user_page.open_user_testpage()
    user_page.chek_title_user_testpage()


def test_not_page(browser_user_event):
    user_page.open_user_widget()
    user_page.chek_title_user_widget()

