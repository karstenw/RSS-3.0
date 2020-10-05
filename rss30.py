# -*- coding: utf-8 -*-

from __future__ import print_function

"""Python 2/3 library to parse RSS 3.0 feeds."""

# __name__ = "rss30"
__version__ = (0, 0, 1)
__author__ = "Karsten Wolf 2020-10"


import sys
import os
import datetime
import unicodedata

import pdb

import pprint
pp = pprint.pprint

if sys.version_info[0] == 3:
    # Py3
    basestring = str
    from io import StringIO
else:
    # Py2
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

import email.parser
Parser = email.parser.Parser


def makeunicode(s, srcencoding="utf-8", normalizer="NFC"):
    """Create a canonical unicode string from a string;
    """
    try:
        if type(s) not in (unicode, str):
            s = str( s )
        s = unicode(s, srcencoding)
    except TypeError:
        print( "makeunicode type conversion error" )
        print( "FAILED converting", type(s), "to unicode" )
    s = unicodedata.normalize(normalizer, s)
    return s


def printdict( d, order=None ):
    if order != None:
        keys = order
    else:
        keys = d.keys()
    
    for key in keys:
        val = d.get(key, None)
        if val == None:
            continue
        print( key.encode("utf-8") )
        print( "    " + val.encode("utf-8") )
        print()


class RSS3(object):
    """A minimal, quick and dirty rss30 parser."""

    basetags = (
        'title', 'description', 'link', 'generator', 'errorsto', 'creator',
        'created', 'last-modified', 'language', 'rights', 'license', 'guid'
        'uri', 'subject')
    extensions = (
        'enclosure-type', 'enclosure-length', 'enclosure-uri',
        'enclosure-episode', 'enclosure-season', 'enclosure-explicit',
        'enclosure-duration', 'enclosure-tags')
    alltags = list(basetags)
    alltags.extend(extensions)
    alltags = tuple(alltags)

    def __init__(self, url):
        self.url = url
        rss = self.load()
        header, entries = self.fromString( rss )
        self.header = header
        self.entries = entries
    
    def load(self):
        # replace this with open from feedparser
        f = open( self.url, 'r' )
        s = f.read()
        f.close()
        return s

    def prnt(self):
        # pretty print a feed
        print("#" * 10)
        printdict( self.header, order=RSS3.alltags )
        print("#" * 10)
        for entry in self.entries:
            printdict( entry, order=RSS3.alltags )
            print("   -" * 5)


    def fromString(self, s):
        """Parse a rss30 string; item 0 is header, remaining are entries."""
        allEntries = []

        # it should use these heuristics
        lineenders = dict(
            mac="\r\r",
            win="\r\n\r\n",
            unx="\n\n")
        titles = s.lower().count("title")
        
        mac = s.count( "\r\r" )
        win = s.count( "\r\n\r\n" )
        unx = s.count( "\n\n" )
        
        # for now improvising
        s = makeunicode( s )
        items = s.split( u"\n\n" )
        
        for item in items:
            p = Parser()
            m = p.parsestr( item )
            allEntries.append( dict(m) )
        
        if len(allEntries) == 0:
            return {},[]
        if len(allEntries) == 1:
            return allEntries[0], []
        else:
            return allEntries[0], allEntries[1:]


if __name__ == '__main__':

    # pdb.set_trace()

    for f in sys.argv[1:]:
        r = RSS3( f )
        r.prnt()
        print( '-'*40 )
