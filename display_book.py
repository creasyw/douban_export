import requests

def get_books (name):
    prefix = "http://book.douban.com/people/"
    suffix = "/collect"
    print r.status_code
    if r.status_code != 200:
        print "Sorry... there is something wrong with the website."
        print "Check it back later, dud..."
        return 0
    print len(r.text)
    


def main ():
    get_books("creasywq")


if __name__=="__main__":
    main()

