use strict;
use warnings;

sub numWords {
    my $wordCount = @_[0];
    my @strArray = split(" " , @_[1]);
    my $number = 0;
    foreach my $element (@strArray) {
        $number++;
    }
    if ($number <= $wordCount) {
        return 1;
    } else {
        return 0;
    }
}

my $file_name = 'q2.in';
my $outputFile = 'q2p2.out';
open INPUT, "<$file_name" or die "Can't open '$file_name'$!";
open OUTPUT, ">$outputFile" or die "Can't open '$outputFile'$1";

print "Max number of words per line: ";
my $count = <STDIN>;

my $answer = "";
while(my $line = <INPUT>) {
    if (numWords($count, $line) == 1) {
        $answer = "$answer" . "$line";
    }
}

if ($answer ne "") {
    print OUTPUT $answer;
} else {
    print OUTPUT "Oooh Nooo!";
}