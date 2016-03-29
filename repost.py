"""dsl input for redsl
Should have available for importing these two names
- 'rexp' for regular exp
- 'postprocessors' for dict of postprocessors
need to be exactly those names; rest (eg seriesmap) is just helpers for 
those two
"""

# RE for describing NYSE symbology
# From https://www.nyse.com/publicdocs/nyse/markets/amex-options/ArcaDirectAPISpecVersion4_1.pdf
# Symbology table pg 12

rexp = r"""

(?=^.+$)				# There better be something >=1
^					# From beginning
(?P<scrip>		[A-Z]*)		# The base scrip
(?P<sertype>		[.+-])?		# Series type char
(?P<series>		[A-QS-Z])?	# Series
(?P<rights>		[R])?		# Rights (special case)
(?P<issued>		[#])?		# issued char indicator
$					# Thats all (there should be!)
"""

# Postprocessors for above
from collections import defaultdict
seriesmap = defaultdict(lambda : "No series type",
                        {'.':"Plain", '-':"Preferred", '+':"Warrant"})
postprocessors = {'issued' : bool, 'sertype': seriesmap, 'rights':bool}
