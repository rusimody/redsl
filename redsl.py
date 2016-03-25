#!/usr/bin/python
"""Utility to make have re in a file
And then post process the matched groups"""

from collections import defaultdict

def redsl(rexp, ppers):
    import re
    def redslcurried(string):
        rec = re.compile(rexp, re.VERBOSE)
        groups = set(rec.groupindex)  # index nos of no interest; discard
        m = rec.search(string)
        if m is None:     return None
        # Match succeeded at this point
        # DSL -> Python
        mapped_d = {gname : m.group(gname) for gname in groups}
        # Run postprocessors
        mapped_dpp = {k : ppers[k](mapped_d[k])  for k in mapped_d}
        return mapped_dpp
    return redslcurried

def identity(x) : return x

def callableize(f_or_d):
    """f_or_d is either a function or a dict,
functions are returned as is for dicts their get method is returned so that they become callable
TODO Need to errorcheck types"""
    return f_or_d.get if isinstance(f_or_d,dict) else f_or_d

###################### DSL instance start ####################
seriesmap = defaultdict(lambda : "No series type",
                        {'.':"Plain", '-':"Preferred", '+':"Warrant"})
ppers = {'issued' : bool, 'sertype': seriesmap, 'rights':bool}
###################### DSL instance end ######################

# 1. Set default ppers to identity
# 2. Make the dicts callable
ppers = defaultdict(lambda : identity,
                    {k : callableize(ppers[k]) for k in ppers})

#################### Script Stuff ############################

def main():
    args = cmdline_parse()
    dslfile, string  = args.file, args.string
    try:
        with open(dslfile, "rU") as f:   rexp = f.read()
    except IOError as ie:
        print("IOError: %s: %s" %  (ie.strerror, ie.filename))
        return 1
    trymatch = redsl(rexp, ppers)(string)
    print(trymatch if trymatch else "Match failed")

def cmdline_parse():
    from argparse import ArgumentParser
    parser = ArgumentParser(
        description='A DSL-ifier of the language of res with named groups')
    parser.add_argument("-f",  "--file", default='redsl.txt',   help='The file containing re')
    parser.add_argument("string", help="The string to be matched")
    ofgroup = parser.add_mutually_exclusive_group()    # Only one output format
    ofgroup.add_argument("-J",  "--json", action='store_true',  help='Json output')
    ofgroup.add_argument("-Y",  "--yaml", action='store_true',  help='Yaml output')
    return parser.parse_args()
    
if __name__ == "__main__":   main()
