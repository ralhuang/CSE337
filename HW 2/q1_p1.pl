use strict;
use warnings;

my $file_name = 'collections.csv';
open INPUT, "<$file_name" or die "Can't open '$file_name'$!";

print "Country: ";
my $country = <STDIN>;
chomp $country;
my $count = 0;
while (my $line =<INPUT>) {
    my @fields = split(",", $line);
    if(@fields[2] eq $country) {
        $count++;
    }
}

print $count;