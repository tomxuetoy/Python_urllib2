#!/usr/bin/env python
import urllib2
try:
    url = urllib2.urlopen("http://www.164.com")
except urllib2.URLError, (err):
    print "URL error(%s)" % (err)
