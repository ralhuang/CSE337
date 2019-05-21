use strict;
use warnings;

my $file_name1 = 'collections.csv';
my $file_name2 = 'm1.csv';
my $file_name3 = 'm2.csv';
my $output_file = 'exhibition.csv';
open INPUT1, "<$file_name1" or die "Can't open '$file_name1'$!";
open INPUT2, "<$file_name2" or die "Can't open '$file_name2'$!";
open INPUT3, "<$file_name3" or die "Can't open '$file_name3'$!";
open OUTPUT, ">$output_file" or die "Can't open '$output_file'$!";

my $line1 = <INPUT1>;
my $line2 = <INPUT2>;
my $line3 = <INPUT3>;

print OUTPUT $line1;

$line1 = <INPUT1>;
$line2 = <INPUT2>;
$line3 = <INPUT3>;

while(defined $line1 || defined $line2 || defined $line3) {
    my @fields1 = (30000000000, 3000);
    if (defined $line1) {
        @fields1 = split(",", $line1);
    }

    my @fields2 = (30000000000, 30000);
    if(defined $line2) {
        @fields2 = split(",", $line2);
    }    

    my @fields3 = (30000000000, 300);
    if (defined $line3) {
        @fields3 = split(",", $line3);
    }

    if ((@fields1[0] < @fields2[0]) && (@fields1[0] < @fields3[0])) {
        chomp $line1;
        $line1 = "$line1" . "\n";
        print OUTPUT $line1;
        $line1 = <INPUT1>;
    } elsif ((@fields2[0] < @fields1[0]) && (@fields2[0] < @fields3[0])) {
        chomp $line2;
        $line2 = "$line2" . "\n";
        print OUTPUT $line2;
        $line2 = <INPUT2>;
    } elsif ((@fields3[0] < @fields1[0]) && (@fields3[0] < @fields2[0])) {
        chomp $line3;
        $line3 = "$line3" . "\n";
        print OUTPUT $line3;
        $line3 = <INPUT3>;
    } else {
        last;
    }
}




