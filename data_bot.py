from selenium import webdriver
import time

driver=webdriver.Chrome()
url1="https://www.msu.edu.tr/"
driver.get(url1)
time.sleep(2)
driver.maximize_window()
url2="https://msu.edu.tr/DaireBaskanliklari/OgrenciIsleri/lisans_programlari_yeni.pdf"
driver.get(url2)
time.sleep(2)
driver.save_screenshot("lisans_programlari-homepage.png")
driver.back() 
time.sleep(1)
driver.close()