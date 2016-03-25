#!/usr/bin/perl

$string = $ARGV[0];

$string =~ /([A-Z]*)([.+-])?([A-Z]?)(#?)/;

%seriesmap = ('.' => "Plain",
              '-' => "Preferred",
              '+' => "Warrant"
);

print "(";
print "$1" . ", ";
print maybeize($2 , $seriesmap{$2}) . ", ";
print maybeize($3 , $3) . ", ";
print ((($4 =~ /#/) ? "True" : "False") . ")\n");


sub maybeize ($inp, $out) {
	my ($inp, $out) = @_;
	return (($inp eq "") ? "None" : ("Ok." . $out));
}
 

