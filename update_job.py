import time
import requests
import requests_cache
from bs4 import BeautifulSoup, element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create key
key = "data"

# create cache
requests_cache.install_cache("cache", backend="sqlite", expire_after= -1)


# read file
file = open("web_page_job.txt", "r")
link_web_page = file.readlines()
# make clear link 
for i in range(len(link_web_page)):
      link_web_page[i] =  link_web_page[i].rstrip()


# ge infor job on web page vlance 
def update_job_vlance(link):
      url = link + key
      drive = webdriver.Chrome(executable_path="./chromedriver_linux")
      drive.get(url)
      
      try:
            element = WebDriverWait(drive, 10).until(
                  EC.presence_of_all_elements_located((By.ID, "layered-footer results-paging"))
            )
      finally:
            drive.quit()
      
if __name__ == "__main__":
      url = link_web_page[0] + key
      driver = webdriver.Chrome(executable_path="./chromedriver_linux")
      #driver.get("file:////home/lav/OneDrive/Vu/myProject/update_job/test.html")
      driver.get(url)
      #elements = driver.find_element_by_css_selector("p.content.halo")
      element = driver.find_element_by_css_selector("p.layered-footer.results-paging")
      print(element)
      #print(elements)
      #page_source = drive.page_source



