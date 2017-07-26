from mechanize import Browser
from bs4 import BeautifulSoup
import pickle
import sys
import os
import urllib2

def get_data():

    browser = Browser()
    browser.set_handle_robots(False)
    browser.open("http://tnp.dtu.ac.in/rm_2016-17/")

    browser.select_form(nr=0)

    path = os.path.dirname(os.path.abspath(__file__))

    fileobject1 =open(path + '/username.txt', 'r')
    username = pickle.load(fileobject1)

    fileobject2 = open(path + '/password.txt', 'r')
    password = pickle.load(fileobject2)

    browser['student_username_rollnumber'] = username
    browser['student_password'] = password

    response = browser.submit()

    content = response.read()
    soup = BeautifulSoup(content, "html.parser")

    li_index = []
    li_heading = []
    li_body= []

    for ul in soup.find_all("ul", attrs= {"class" : "pagination pagination-sm pull-right"}):
        for a in ul.find_all("a"):
            x = a["href"].split("index/")
            pu = str(x[0])
            li_index.append(x[1])

    end = int(li_index[len(li_index) - 1])

    print pu

    for i in range(0,end,2):
        url = str(pu) + "index/" + str(i)
        req = browser.open(url)

        c = req.read()
        soup = BeautifulSoup(c, "html.parser")

        for heading in soup.find_all("h4", attrs={"class": "timeline-header"}):
            li_heading.append(heading.text)

        for body in soup.find_all("div", attrs={"class": "timeline-body"}):
            x = body.text
            x = x.replace('.', '.\n')
            li_body.append(x)


    return li_heading,li_body

