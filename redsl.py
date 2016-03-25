#!/usr/bin/python
"""Utility to make have re in a file
And then post process the matched groups"""

try: 
    from postprocessors import ppers
except ImportError:
    ppers = {}

def redsl(rexp, ppers):
    import re
    from collections import defaultdict

    def matcher(string):
        """Should be search-er by python terminology"""
        rec = re.compile(rexp, re.VERBOSE)
        groups = set(rec.groupindex)  # index nos of no interest; discard
        m = rec.search(string)
        if m is None:     return None
        # Match succeeded at this point
        # match-data -> Python
        mapped_d = {gname : m.group(gname) for gname in groups}
        # postprocess and done!
        return {k : ppers[k](mapped_d[k])  for k in mapped_d}

    # Set up postprocessing... ie
    # <1> Set default ppers to identity function <2> Make the (sub)dicts callable
    ppers = defaultdict(lambda : identity,
                        {k : callableize(ppers[k]) for k in ppers})

    return matcher

def callableize(f_or_d):
    """f_or_d is either a function or a dict,
functions are returned as is for dicts their get method is returned so that they become callable
TODO Need to errorcheck types"""
    return f_or_d.get if isinstance(f_or_d,dict) else f_or_d

def identity(x) : return x

#################### Output formats ##########################
# TODO

#################### Script Stuff ############################

def main():
    from postprocessors import ppers
    args = cmdline_parse()
    dslfile, string, ppersfile  = args.re, args.string, args.postprocessors
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
    parser.add_argument("-r",  "--re", default='redsl.txt',   help='File containing re')
    parser.add_argument("-p",  "--postprocessors", default='postprocessors.py',
                        help='Python file containing postprocessors')
    parser.add_argument("string", help="The string to be matched")
    ofgroup = parser.add_mutually_exclusive_group()    # Only one output format
    ofgroup.add_argument("-J",  "--json", action='store_true',  help='Json output')
    ofgroup.add_argument("-Y",  "--yaml", action='store_true',  help='Yaml output')
    return parser.parse_args()
    
if __name__ == "__main__":   main()
