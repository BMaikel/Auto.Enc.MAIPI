import time
import random
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
chromedriver_path = "C:/Users/Maicol/.wdm/drivers/chromedriver/win64/131.0.6778.85/chromedriver.exe"

def _login(driver, MAIL, PASS):
    driver.get("https://maipi.lamolina.edu.pe/")
    driver.find_element(By.CLASS_NAME, value = 'correo').click()
    driver.find_element(By.NAME, value = "identifier").send_keys(MAIL)
    driver.find_element(By.NAME, value="identifier").send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.NAME, value = "Passwd").send_keys(PASS)
    driver.find_element(By.NAME, value = "Passwd").send_keys(Keys.RETURN)
    time.sleep(60) #Completar con tu celular si es necesario

def complete_survey(driver):
    try:
        for i in range(22):
            if i < 20:
                question_name = f"respuesta[{i}].opcion.id"
                options = driver.find_elements(By.NAME, question_name)

                if options:
                    selected_option = options[random.choice([3, 4])]
                    selected_option.click()
                    print(f"Pregunta {i + 1}: Respuesta seleccionada ({selected_option.get_attribute('value')}).")
            
            elif i >= 20 and i < 22:
                text_area = driver.find_element(By.XPATH, f"//form[@id='tab-{i}']//textarea[@required]")
                random_text = COM1 #Ingresar Respuesta
                text_area.send_keys(random_text)
                print(f"Pregunta {i + 1}: Respuesta de texto ingresada ({random_text}).")

            if i < 21:
                next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Siguiente')]")
                next_button.click()
                print(f"Se hizo clic en el botón 'Siguiente' después de la pregunta {i + 1}.")
                time.sleep(1.5)

        finalizar_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Finalizar Encuesta')]")
        finalizar_button.click()
        print("Se hizo clic en el botón 'Finalizar Encuesta'.")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Aceptar')]").click()

        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]").click()

        for i in range(6):
            if i < 5: 
                question_form = driver.find_element(By.ID, f"tab-curso{i}")
                buttons = question_form.find_elements(By.CLASS_NAME, "btn-n")

                if buttons:
                    selected_button = random.choice(buttons)
                    selected_button.click()
                    print(f"Pregunta {i + 1}: Respuesta seleccionada ({selected_button.text}).")

                if i < 5:  
                    next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Siguiente')]")
                    next_button.click()
                    print(f"Se hizo clic en el botón 'Siguiente' después de la pregunta {i + 1}.")
                    time.sleep(1.5) 

            elif i == 5:
                question_form = driver.find_element(By.ID, f"tab-curso{i}")
                text_area = question_form.find_element(By.TAG_NAME, "textarea")

                random_text = COM2 #Respuesta Parte 2
                text_area.send_keys(random_text)
                print(f"Pregunta {i + 1}: Respuesta de texto ingresada ({random_text}).")

        finalizar_button_2 = driver.find_element(By.XPATH, "(//button[contains(text(), 'Finalizar Encuesta')])[2]")
        finalizar_button_2.click()
        print("Se hizo clic en el botón 'Finalizar Encuesta'.")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[contains(text(), 'Aceptar')]").click()
        print("Se hizo clic en el botón 'Aceptar'.")
        time.sleep(1)

    except Exception as e:
        print(f"Error al completar la encuesta: {e}")

def _interact_with_surveys(driver):
    while True:
        try:
            survey_link = driver.find_element(By.XPATH, "//a[@title='Encuestar']")
            print("Se encontró una encuesta. Resolviéndola...")
            survey_link.click()
            time.sleep(3)

            complete_survey(driver)

            driver.back()
            time.sleep(6)

        except Exception as e:
            print(f"Error: {e}")
            print("No quedan encuestas por resolver o ocurrió un problema.")
            break

def main():
    service = Service(chromedriver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1240,720")
    options.add_argument("--disable-notifications")
    options.binary_location = brave_path
    driver = Chrome(service = service, options = options)

    #Loggin MAIPI
    _login(driver, MAIL, PASS)

    #Resolviendo Encuestas
    _interact_with_surveys(driver)
    driver.quit()

if __name__ == "__main__":
    MAIL = "Correo"
    PASS = "Contraseña"
    COM1 = "Todo bien, me gustó la clase"
    COM2 = "Me gustó tanto el curso que lo voy a llevar otra vez"
    main()