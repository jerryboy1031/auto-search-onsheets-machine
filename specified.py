

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

# google sheet
import gspread
from google.oauth2.service_account import Credentials

#----------------------------------------------------------------------
# read the search result to google sheets by spreadsheet api
def readSheet():
    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/drive.file']
    
    credentials= Credentials.from_service_account_file("secret_credential.json", scopes=scope)
    client = gspread.authorize(credentials)
    sh = client.open(title='EU_tour')#,folder_id='1CCJ6d-P381whToCFP6V9rb_mkI84GuHIF6z5rqWAzzg') #error--------------
    wks= sh.worksheet("法國")
    
    urls=[]
    for i in range(7,52):
        urls.append(wks.cell(i,2).value)

    return urls
    

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
def specified():
    # Configure Selenium
    driver_path = "/chromedriver_win32/chromedriver.exe" # Path to your ChromeDriver executable
    service = Service(driver_path)  
    options = Options()
    options.headless = True  # Run the browser in headless mode (without GUI)
    driver = webdriver.Chrome(service=service, options=options)

    

    urls=readSheet()
    
    #txt=[]
    for i in range(5,12):        
        # extract the content of the website
        driver.get(f"{urls[i]}")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
       
        print(urls[i])
        #HTML tags
        for i in range(1,7):
            if soup.find("h"+str(i)) != None:
                print("\n h"+str(i)+": ",soup.find("h"+str(i)).get_text())
        '''if soup.find("head") != None:    
            print("head: ",soup.find("head").get_text())
        if soup.find("body") != None:
            print("body: ",soup.find("body").get_text())'''
        if soup.find("p") != None:
            print("\n p: ",soup.find("p").get_text())
        #print("ul: ",soup.find("ul").get_text())
        if soup.find("table") != None:
            print("\n table: ",soup.find("table").get_text())
            
        '''# Save data to text file
        text_file = "google_search_results.txt"
        with open(text_file, "a", encoding="utf-8") as file:
            file.writelines(txt)'''
    
    #save data to sheets
    #saveToSheet(results_data)

    # Close the browser
    driver.quit()

def main():
    specified()# Enter your desired search query
    
if __name__=='__main__':
    main()