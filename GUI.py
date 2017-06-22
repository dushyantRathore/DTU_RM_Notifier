from RM_scraper import get_data
import os
import signal
import gi
import requests
import json

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'


def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                           os.path.abspath('/home/dushyant/Desktop/Github/DTU_Resume_Manager_Notifier/DTU,_Delhi_official_logo.png'),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(rm_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()


def rm_menu():
    main_menu = gtk.Menu()

    x,y = get_data()

    for i in range(0,len(x)):
        company_name = gtk.MenuItem(x[i])
        sep = gtk.SeparatorMenuItem()

        company_body = gtk.Menu()
        company_body.append(gtk.MenuItem(y[i]))

        company_name.set_submenu(company_body)

        main_menu.append(company_name)
        main_menu.append(sep)

    main_menu.show_all()

    return main_menu

if __name__ == "__main__":
    main()
