from selene import have


def test_profile_page_createactivity(mashroom_api):
    mashroom_api.open('')
    mashroom_api.element(
        '#app > div.v-application--wrap > main > div > div > div > div > div.row.mb-4.no-gutters > '
        'div.col.col-auto > button > span').click()
    mashroom_api.element("//div[@id='app']/div[3]/div/div/div[2]/span/form/div/div/span/div/div/div/div").click()
    mashroom_api.element("//div[@id='app']/div[3]/div/div/div[2]/span/form/div/div/span/div/div/div/div/input"). \
        type("test_activity_py")
    mashroom_api.element("//div[@id='app']/div[3]/div/div/div[2]/span/form/button/span").click()
    mashroom_api.element(
        '//*[@id="app"]/div/main/div/div/div/div/div/div[1]/span[1]'). \
        should(have.text('test_activity_py'))


def test_profile_page_deleteactivity(mashroom_api):
    mashroom_api.open('')
    mashroom_api.element(
        '//*[@id="app"]/div[1]/main/div/div/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[5]/button[3]').\
        click()
    mashroom_api.element(
        '#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions > '
        'button:nth-child(3)').click()
    mashroom_api.element(
        '//*[@id="app"]/div/main/div/div/div/div/div[2]/div/div/div/div/div[1]/table/tbody/tr/td/div/div'). \
        should(have.text('Нажмите на кнопку "Новое мероприятие", чтобы создать мероприятие'))
