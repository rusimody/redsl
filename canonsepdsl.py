#!/usr/bin/python
# Symbology into a separated into file: "symbologydsl.txt"
# As of now file name hardwired and needs to be in same directory as this script

from sys import argv
import re

try:
    # TODO Following needs to be added to dsl file
    # (?=^.{1,}$)			 # There better be something >=1

    dslfile = "symbologydsl.txt"
    rexp    = open(dslfile, "rU").read()
    string  = argv[1]
except IOError as ie:
    if ie.errno == 2:  # File not found
        print ("No dsl file: %s" % ie.filename)
    else:
        print ("IOError: %s: %s" %  (ie.strerror, ie.filename))
    exit()
except IndexError:
    print ("No arg given")
    exit()

seriesmap = {'.':"Plain",    '-':"Preferred",   '+':"Warrant"}
    
m = re.search(rexp, string, re.VERBOSE)
if m:
    g = m.group
    
    # DSL -> Python
    scrip, serchar, series, issuedc = g('scrip'), g('serchar'), g('series'), g('issuedc')

    # Postprocessing: series, scrip are left as is
    sertype   = seriesmap[serchar] if serchar else "No Series Type"
    issued    = issuedc == '#'
    print("scrip:\t%s\ntype:\t%s\nseries:\t%s\nissued:\t%s"   %
             (scrip, sertype, series, issued))
else:
    print ("match failed")
