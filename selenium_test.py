from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def test_home():
    # please input the value it needed for your own local webdriver
    driver = webdriver.Firefox()
    driver.get("http://162.246.157.128:8000")
    elem = driver.find_element_by_id("name")    
    elema = driver.find_element_by_id("about")
    eleme = driver.find_element_by_id("education")
    elems = driver.find_element_by_id("skills")
    elemw = driver.find_element_by_id("work")    
    elemc = driver.find_element_by_id("contact")
    assert elem != None  
    assert elema != None 
    assert eleme != None 
    assert elems != None 
    assert elemw != None 
    assert elemc != None     

test_home()