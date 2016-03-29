from collections import defaultdict
"""dsl input for redsl
The names
'rexp' for regular exp
and 'postprocessors' for dict of postprocessors
need to be exactly those names; rest (eg seriesmap) is just helpers for 
those two
"""

seriesmap = defaultdict(lambda : "No series type",
                        {'.':"Plain", '-':"Preferred", '+':"Warrant"})
postprocessors = {'issued' : bool, 'sertype': seriesmap, 'rights':bool}

rexp = r"""
# DSL (instantiation) for describing NYSE symbology
# From https://www.nyse.com/publicdocs/nyse/markets/amex-options/ArcaDirectAPISpecVersion4_1.pdf
# Symbology table pg 12

(?=^.+$)				# There better be something >=1
^					# From beginning
(?P<scrip>		[A-Z]*)		# The base scrip
(?P<sertype>		[.+-])?		# Series type char
(?P<series>		[A-QS-Z])?	# Series
(?P<rights>		[R])?		# Series
(?P<issued>		[#])?		# issued char indicator
$					# Thats all (there should be!)
"""
