from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import signal
import json
import time

rows = []

driverpath = r'C:\Users\sohel\Desktop\chromedriver.exe'

browser = webdriver.Chrome(r'D:\chromedriver.exe')

url = 'http://www.cmfchile.cl/portal/principal/605/w3-propertyvalue-23492.html'

def hover(browser, xpath):
    element_to_hover_over = browser.find_element_by_xpath(xpath)
    hover = ActionChains(browser).move_to_element(element_to_hover_over)
    hover.perform()



browser.get(url)

time.sleep(2)

xpath = '//*[@id="nav"]/div/ul/li[3]/a/span'

hover(browser,xpath)

tab = None

while tab is None:
    try:
        tab = browser.find_element_by_xpath('//*[@id="nav"]/div/ul/li[3]/ul/li/div[1]/ul/li[1]/a')
    except Exception:
        continue

tab.click()

time.sleep(0.5)
xpath = '//*[@id="lista_valores_i__w3_pa_MV_entidades_1"]/select'

select = Select(browser.find_element_by_xpath(xpath))
# browser.find_element_by_xpath(xpath).click()
select.select_by_visible_text('Fondos de Inversión No Rescatables')

time.sleep(7)


tbody = None
while tbody is None:
    try:
        tbody = browser.find_element_by_xpath('//*[@id="listado_fiscalizados"]/table/tbody')
    except Exception:
        continue

trs = tbody.find_elements_by_tag_name('tr')

last = len(trs)

print(last)

for i in range(1,3):
    tbody = None
    while tbody is None:
        try:
            tbody = browser.find_element_by_xpath('//*[@id="listado_fiscalizados"]/table/tbody')
        except Exception:
            continue

    trs = tbody.find_elements_by_tag_name('tr')

    td = None
    while td is None:
        try:
            td = trs[i].find_elements_by_tag_name('td')[1]
        except Exception:
            continue
    td.click()
    time.sleep(5)
    row = {}
    try:
        row["R.U.N. del Fondo"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[1]/td').text
        row["Nombre Fondo Inversión"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[2]/td').text
        row["Tipo de Fondo de Inversión"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[6]/td').text
        row["R.U.T. Administradora"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[7]/td').text
        row["Fecha Resolución de aprobación del reglamento interno del fondo"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[9]/td').text
        row["Fecha Inicio Operaciones"] = browser.find_element_by_xpath('//*[@id="contenido"]/table/tbody/tr[11]/td').text
        rows.append(row)
    except Exception:
        pass
    print(row)
    browser.back()

browser.close()

# with open('data.json', 'w') as outfile:  
#     json.dump(rows, outfile,indent=4)

