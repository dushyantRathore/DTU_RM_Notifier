from DTU_Results import get_Results
import os
import signal
import gi
import requests
import json
import urllib2
import urllib

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'


def main():

    indicator = appindicator.Indicator.new(APPINDICATOR_ID,
                                           os.path.abspath('/home/dushyant/Desktop/Github/DTU_RM_Results_Notifier/DTU,_Delhi_official_logo.png'),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(rm_menu())
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()


def rm_menu():
    main_menu = gtk.Menu()

    x,y = get_Results()

    exit = gtk.MenuItem("Exit")
    exit.connect('activate', stop)

    for i in range(0,50):
        result_text = gtk.MenuItem(x[i])
        result_text.connect("activate", item_activated, i)
        sep = gtk.SeparatorMenuItem()

        main_menu.append(result_text)
        main_menu.append(sep)

    main_menu.append(exit)

    main_menu.show_all()

    return main_menu


def item_activated(self, i):
    x,y = get_Results()
    print "Item activated : " + str(i)
    path = str(x[i]) + str(".pdf")
    urllib.urlretrieve(y[i], path)



def stop(self):
    gtk.main_quit()

if __name__ == "__main__":
    main()
