# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:29:22 2023

@author: User
"""
# extract website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time 
# google sheet
import gspread
from google.oauth2.service_account import Credentials

#----------------------------------------------------------------------
# save the search result to google sheets by spreadsheet api
def saveToSheet(data):
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']
    
    credentials= Credentials.from_service_account_file("secret_credential.json", scopes=scope)
    client = gspread.authorize(credentials)
    sh = client.open(title='EU_tour')#,folder_id='1CCJ6d-P381whToCFP6V9rb_mkI84GuHIF6z5rqWAzzg') #error--------------
    wks= sh.worksheet("法國")
    for each in data:
        wks.insert_row(each,index=7)
    #print(wks.get_values())
    
#----------------------------------------------------------------------    
# search by google search engine(Chrome) and extract the search result 
def extract_website(string):
    # Configure Selenium
    driver_path = "/chromedriver_win32/chromedriver.exe" # Path to your ChromeDriver executable
    service = Service(driver_path)  
    options = Options()
    options.headless = True  # Run the browser in headless mode (without GUI)
    driver = webdriver.Chrome(service=service, options=options)

    # Define search query
    search_query = string  

    # extend the pages (or the search results will only the first page)
    search_results = []
    for page in range(1, 3):  # Scrape results from the first 3 pages (change as needed)
        url = f"https://www.google.com/search?q={search_query}&start={page * 10}"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Find search result elements
        search_results.extend(soup.find_all("div", class_="yuRUbf"))
        time.sleep(5)


    # Extract data from search results
    results_data = [] # [ each[],...]
    print(search_results[0])
    for result in search_results[:20]:
        each=[] # every search each[title, url, spot1,spot2...]
        title = result.find("h3").get_text()
        url = result.find("a")["href"]
        #snippet_element = result.find("span", class_="aCOpRe")
        #snippet = snippet_element.get_text() if snippet_element else ""
        print("\n title: ",title)
        print("\n url: ",url)
        each.append(title)
        each.append(url)
        
        # append results to the array
        results_data.append(each)
        
        '''# extract the content of the website
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
       
        #HTML tags
        print("title: ",title)
        print("h1: ",soup.find("h1").get_text())
        print("h2: ",soup.find("h2").get_text())
        print("h3: ",soup.find("h3").get_text())
        print("h4: ",soup.find("h4").get_text())
        #print("h5: ",soup.find("h5").get_text())
        #print("h6: ",soup.find("h6").get_text())
        #print("body: ",soup.find("body").get_text())
        print("p: ",soup.find("p").get_text())
        #print("ul: ",soup.find("ul").get_text())
        print("table: ",soup.find("table").get_text())
  
        content_arr = soup.find_all("h3")
        
        for content in content_arr:
            if content.get_text() != "":
                each.append(content.get_text())
            else: 
                break'''  
             
        
        
    #save data to sheets
    #saveToSheet(results_data)

    # Close the browser
    driver.quit()

def main():
    extract_website("france touris spots")# Enter your desired search query
    
if __name__=='__main__':
    main()