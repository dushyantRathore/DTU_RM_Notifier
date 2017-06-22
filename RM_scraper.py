from mechanize import Browser
from bs4 import BeautifulSoup


def get_data():

    browser = Browser()
    browser.set_handle_robots(False)
    browser.open("http://tnp.dtu.ac.in/rm_2016-17/intern/intern_login")

    browser.select_form(nr=0)

    browser['intern_student_username_rollnumber'] = "2K14/SE/029"
    browser['intern_student_password'] = "iit2011130"

    response = browser.submit()

    content = response.read()
    soup = BeautifulSoup(content, "html.parser")

    li_heading = []

    for heading in soup.find_all("h4", attrs={"class":"timeline-header"}):
        li_heading.append(heading.text)

    li_body = []

    for body in soup.find_all("div", attrs={"class":"timeline-body"}):
        x = body.text
        x = x.replace('.', '.\n')
        li_body.append(x)

    # li_heading = map(lambda s:s.strip(), li_heading)
    # li_body = map(lambda s: s.strip(), li_body)

    # print len(li_heading)
    # print len(li_body)

    #print li_heading[0]
    #print li_body[0]

    # print li_body[0]

    return li_heading, li_body
