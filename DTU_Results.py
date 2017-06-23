from bs4 import BeautifulSoup
import urllib2
import requests


def get_Results():
    url = "http://www.exam.dtu.ac.in/result.htm"
    result_file = urllib2.urlopen(url)
    result_html = result_file.read()
    result_file.close()

    soup = BeautifulSoup(result_html, "html.parser")

    li_text = []
    li_link = []

    for a in soup.find_all("a"):
        li_text.append(a.text)

    for table in soup.find_all("table", attrs= {"id" : "AutoNumber1"}):
        for tr in table.find_all("tr"):
            for a in tr.find_all("a"):
                li_link.append("http://exam.dtu.ac.in/" + a['href'])

    li = map(lambda s: s.strip(), li_text)

    final_li_text = []

    for i in range(12, len(li)):
        final_li_text.append(li_text[i])

    del final_li_text[len(final_li_text) - 1]

    print "\n"

    #for i in final_li:
    #    print "-->  " + str(i)

    del li_link[0]

    return final_li_text,li_link

if __name__ == "__main__":
    get_Results()