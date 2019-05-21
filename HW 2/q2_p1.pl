use strict;
use warnings;

sub strSwap {
    @_[2] =~ s/@_[0]/@_[1]/g;
    return @_[2];
}

my $file_name = 'q2.in';
my $outputFile = 'q2p1.out';
open INPUT, "<$file_name" or die "Can't open '$file_name'$!";
open OUTPUT, ">$outputFile" or die "Can't open '$outputFile'$1";

print "What do you want to replace?";
my $argSearch = <STDIN>;

print "Replace $argSearch with: ";
my $argSwap = <STDIN>;

while(my $line = <INPUT>) {
    chomp $argSearch;
    chomp $argSwap;
    print OUTPUT strSwap($argSearch, $argSwap, $line);
}


