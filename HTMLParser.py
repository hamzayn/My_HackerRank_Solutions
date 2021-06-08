#!python3
from html.parser import HTMLParser
def read_int(): return int(input())
def read_int_words(): return map(int,input().split())
def pa(a):
    for ai in a:
        (k,v) = ai
        print("->",k.strip(),">",str(v).strip())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag.strip())
        pa(attrs)
    def handle_endtag(self, tag): print("End   :",tag.strip())
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag.strip())
        pa(attrs)
n = int(input())
parser = MyHTMLParser()
for i in range(n): parser.feed(input())


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {0}".format(tag))
        for key, val in attrs:
            print("-> {0} > {1}".format(key, val))
    def handle_endtag(self, tag):
        print("End   : {0}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print("Empty : {0}".format(tag))
        for key, val in attrs:
            print("-> {0} > {1}".format(key, val))
parser = MyHTMLParser()
lines = []
n = int(input())
for i in range(n):
    lines.append(str(input()).strip())
parser.feed(''.join(lines))


import re
import html
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name,value in attrs:
            print("->",name+" >",value)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name,value in attrs:
            print("->",name+" >",value)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n = int(input())
for _ in range(n):
    parser.feed(input())