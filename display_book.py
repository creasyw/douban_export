import requests
import re

def print_name (text):
    finder = re.compile("title=\"(.*?)\"")
    for i in finder.findall(text):
        print i

def get_books (name):
    prefix = "http://book.douban.com/people/"
    suffix = "/collect"
    r = requests.get(prefix+name+suffix)
    if r.status_code != 200:
        print "Sorry... there is something wrong with the website."
        print "Check it back later, dud..."
        return 0
    print_name(r.text)


def main ():
    get_books("creasywq")


if __name__=="__main__":
    main()

