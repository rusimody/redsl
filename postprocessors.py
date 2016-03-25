from collections import defaultdict
seriesmap = defaultdict(lambda : "No series type",
                        {'.':"Plain", '-':"Preferred", '+':"Warrant"})
ppers = {'issued' : bool, 'sertype': seriesmap, 'rights':bool}

