driver.get('https://yoparticipo.oep.org.bo/')
 
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id = 'documento']").send_keys("12510613")
 
time.sleep(2)
 
 
#driver.find_element(By.XPATH, "").click()
 
driver.find_element(By.XPATH, "//select[@aria-label='Select month']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@aria-label='Select month']//option[@value = '1']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//select[@aria-label='Select year']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//select[@aria-label='Select year']//option[@value = '2003']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@aria-label='31-1-2003']").click()
time.sleep(2)
 
driver.find_element(By.XPATH, "//button[text()='Consultar']").click()
time.sleep(10)