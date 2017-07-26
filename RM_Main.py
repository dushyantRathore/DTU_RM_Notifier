import os
import signal
import gi
from mechanize import Browser
from bs4 import BeautifulSoup
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import getpass

APPINDICATOR_ID = 'myappindicator'

# Function to scrape the DTU resume manager


def get_data(username, password):

    browser = Browser()
    browser.set_handle_robots(False)
    browser.open("http://tnp.dtu.ac.in/rm_2016-17/")

    browser.select_form(nr=0)

    browser['student_username_rollnumber'] = username
    browser['student_password'] = password

    response = browser.submit()

    content = response.read()
    soup = BeautifulSoup(content, "html.parser")

    li_index = []
    li_heading = []
    li_body= []

    for ul in soup.find_all("ul", attrs={"class": "pagination pagination-sm pull-right"}):
        for a in ul.find_all("a"):
            x = a["href"].split("index/")
            pu = str(x[0])
            li_index.append(x[1])

    end = int(li_index[len(li_index) - 1])

    for i in range(0,end,2):
        url = str(pu) + "index/" + str(i)
        req = browser.open(url)

        c = req.read()
        soup = BeautifulSoup(c, "html.parser")

        for heading in soup.find_all("h4", attrs={"class":"timeline-header"}):
            li_heading.append(heading.text)

        for body in soup.find_all("div", attrs={"class":"timeline-body"}):
            x = body.text
            x = x.replace('.', '.\n')
            li_body.append(x)

    return li_heading,li_body

# Main function for the GUI


def main():

    path = os.path.dirname(os.path.abspath(__file__))
    image_path = path + "/Logo.png"

    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                           os.path.abspath(image_path),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(rm_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()

# Resume Manager main GUI menu


def rm_menu():

    # Get username
    username = raw_input("Enter your username : ")

    # Get password
    password = str(getpass.getpass("Enter your password : "))

    main_menu = gtk.Menu()

    try :

        x,y = get_data(username, password)

        exit = gtk.MenuItem("Exit")
        exit.connect('activate', stop)

        for i in range(0,len(x)):
            company_name = gtk.MenuItem(x[i])
            sep = gtk.SeparatorMenuItem()

            company_body = gtk.Menu()
            company_body.append(gtk.MenuItem(y[i]))

            company_name.set_submenu(company_body)

            main_menu.append(company_name)
            main_menu.append(sep)

        main_menu.append(exit)

        main_menu.show_all()

        return main_menu

    except:

        print "Invalid username/password"


def stop(self):
    gtk.main_quit()

if __name__ == "__main__":
    main()
