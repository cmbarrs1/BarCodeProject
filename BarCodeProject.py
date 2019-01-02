#!/usr/bin/python3
import re
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def Beautiful(strBarCode):
    url = 'http://www.barcodelookup.com%2F'+strBarCode
    session = HTMLSession()
    page = session.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    productdetails = soup.find(class_="col-md-6 product-details")
    title = productdetails.find('h4')
    print (title.contents[0].strip())
    details = productdetails.find(text=re.compile('Author:'))
    detailsLoc = details.parent
    author = detailsLoc.find('span')
    print(author.contents[0].strip())


def Spreadsheet():
    #https://gspread.readthedocs.io%2Fen%2Flatest%2F
    scope = ['http://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('PersonalBookCatalog-8e947f455e67.json', scope)
    gc = gspread.authorize(credentials)
#    wks = gc.open("Test_Sheet").sheet1
#    print (wks.cell(1,1).value)
#    gc.create('A new spreadsheet')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/F1PL11FOGQ0SAPUfkuiE8rF8yEDwkiQFNUD3IV1hZpbt8/edit#gid=1202682562')
    wks = sh.sheet1
    print (wks.cell(1,1).value)

if __name__ == "__main__":
#    Beautiful('9780465097678')
    Spreadsheet()

