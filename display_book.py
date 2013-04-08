import requests
import re

def print_name (text):
    finder = re.compile("title=\"(.*?)\"")
    for i in finder.findall(text):
        print i

def get_books (name, para):
    print "\n\nPrinting the %s\'s %s list\n"%(name, para)
    address ="http://"+para+".douban.com/people/"+name+"/collect"
    r = requests.get(address)
    if r.status_code != 200:
        print "Sorry... there is something wrong with the website."
        print "Check it back later, dud..."
        return 0
    print_name(r.text)
    address = re.findall("rel=\"next\" href=\"(.*?)\"", r.text)
    while address!=[]:
        r = requests.get(address[0])
        print_name(r.text)
        address = re.findall("rel=\"next\" href=\"(.*?)\"", r.text)



def main ():
    get_books("creasywq", "book")
    get_books("creasywq", "movie")
    get_books("creasywq", "music")


if __name__=="__main__":
    main()

