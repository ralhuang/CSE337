use strict;
use warnings;

my $filename = $ARGV[0];

open INPUT, "<$filename" or die "Can't open file";

my $count0 = 0;
my $count1 = 0;
my $count2 = 0;
my $count3 = 0;
my $count4 = 0;
my $count5 = 0;
my $count6 = 0;
my $count7 = 0;
my $count8 = 0;
my $count9 = 0;


while (my $line = <INPUT>) {

    my @lineArr = split(" ", $line);
    chomp $line;
    my $countCount = chop($line);
    my $wordCount = 0;
    foreach my $element (@lineArr) {
        $wordCount++;
    }
    if($countCount == 0) {
        $count0 += $wordCount;
    } elsif ($countCount == 1) {
        $count1 += $wordCount;
    } elsif ($countCount == 2) {
        $count2 += $wordCount;
    } elsif ($countCount == 3) {
        $count3 += $wordCount;
    } elsif ($countCount == 4) {
        $count4 += $wordCount;
    } elsif ($countCount == 5) {
        $count5 += $wordCount;
    } elsif ($countCount == 6) {
        $count6 += $wordCount;
    } elsif ($countCount == 7) {
        $count7 += $wordCount;
    } elsif ($countCount == 8) {
        $count8 += $wordCount;
    } elsif ($countCount == 9) {
        $count9 += $wordCount;
    }
}

print "$count0\n";
print "$count1\n";
print "$count2\n";
print "$count3\n";
print "$count4\n";
print "$count5\n";
print "$count6\n";
print "$count7\n";
print "$count8\n";
print "$count9\n";
