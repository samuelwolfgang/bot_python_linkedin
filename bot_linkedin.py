#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Selenium
from selenium import webdriver

class Linkedin:
    navegador = webdriver.Chrome()
    navegador.get("https://www.linkedin.com")
   
    navegador.find_element("xpath", '//*[@id="session_key"]').send_keys("your_email")
    navegador.find_element("xpath", '//*[@id="session_password"]').send_keys("your_password")
    
    navegador.find_element("xpath", '//*[@id="main-content"]/section[1]/div/div/form/button').click()
    

    


# In[ ]:




