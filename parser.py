from selenium.webdriver.common.by import By

from selenium import webdriver
import json
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#ссылка на категорию, которую хотим запарсить
url = 'https://svoe-selo.ru/services-catalog/category/remont-3'


answer_filename = "ИМЯ ФАЙЛА ДЛЯ СОХРАНЕНИЯ"

driver.get(url)

menu_buttons_footer = driver.find_elements(By.CLASS_NAME, "pagination__wrapper--g6bGx")[0].text.split('\n')[-1]
driver.set_window_size(1800, 900)
final_data = dict()
counter = 0
for i in range(1, int(menu_buttons_footer) + 1):
    if i != 1:
        driver.get(url + '/list/' + str(i))
    specs_list = driver.find_elements(By.CLASS_NAME, "serviceCard")
    for  index, spec in enumerate(specs_list):
        title = spec.find_element(By.CLASS_NAME, 'textBlock__link--DvqaO')
        spec_data = spec.find_elements(By.CLASS_NAME, 'textBlock__infoText--T63Oz')
        category = spec_data[0].text[10:]
        first_overview = spec_data[1].text[9:]
        original_window = driver.current_window_handle
        link = title.get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(link)
        datik = driver.find_element(By.CLASS_NAME, 'serviceCardDescription__text--suYrR').text
        driver.close()
        driver.switch_to.window(original_window)
        final_data[title.text +'~'+ str(counter)+'~'+link] = category + '\n' + first_overview + '\n' + datik + '\n\n'
        print(title.text +'~'+ str(counter), '\n', category + '\n' + first_overview + '\n' + datik + '\n\n')
        counter+=1
with open(answer_filename, 'w', encoding='utf-8') as fp:
    json.dump(final_data, fp, ensure_ascii=False)