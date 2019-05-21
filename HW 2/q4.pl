use strict;
use warnings;
use Cwd;

my $inputFile = $ARGV[0];
open INPUT, "<$inputFile" or die "Can't open file";

my $directory = "features";

unless(-e $directory or mkdir $directory) {
    die "Unable to create $directory\n";
}

$directory .= "\\";
my $file0 = $directory . "\\0-features.txt";
my $file1 = $directory . "\\1-features.txt";
my $file2 = $directory . "\\2-features.txt";
my $file3 = $directory . "\\3-features.txt";
my $file4 = $directory . "\\4-features.txt";
my $file5 = $directory . "\\5-features.txt";
my $file6 = $directory . "\\6-features.txt";
my $file7 = $directory . "\\7-features.txt";
my $file8 = $directory . "\\8-features.txt";
my $file9 = $directory . "\\9-features.txt";

open OUTPUT0, "+>>$file0" or die "Can't open OUTPUT0";
open OUTPUT1, "+>>$file1" or die "Can't open OUTPUT1";
open OUTPUT2, "+>>$file2" or die "Can't open OUTPUT2";
open OUTPUT3, "+>>$file3" or die "Can't open OUTPUT3";
open OUTPUT4, "+>>$file4" or die "Can't open OUTPUT4";
open OUTPUT5, "+>>$file5" or die "Can't open OUTPUT5";
open OUTPUT6, "+>>$file6" or die "Can't open OUTPUT6";
open OUTPUT7, "+>>$file7" or die "Can't open OUTPUT7";
open OUTPUT8, "+>>$file8" or die "Can't open OUTPUT8";
open OUTPUT9, "+>>$file9" or die "Can't open OUTPUT9";

while(my $line = <INPUT>) {
    chomp $line;
    my $n = chop $line;
    chop $line; #remove comma;
    $line = $line . "\n";
    if ($n == 0) {
        print OUTPUT0 $line;
    } elsif ($n == 1) {
        print OUTPUT1 $line;
    } elsif ($n == 2) {
        print OUTPUT2 $line;
    } elsif ($n == 3) {
        print OUTPUT3 $line;
    } elsif ($n == 4) {
        print OUTPUT4 $line;
    } elsif ($n == 5) {
        print OUTPUT5 $line;
    } elsif ($n == 6) {
        print OUTPUT6 $line;
    } elsif ($n == 7) {
        print OUTPUT7 $line;
    } elsif ($n == 8) {
        print OUTPUT8 $line;
    } elsif ($n == 9) {
        print OUTPUT9 $line;
    }
}

print "Files have been created!\n";
print abs_path($file0);
print abs_path($file1);
print abs_path($file2);
print abs_path($file3);
print abs_path($file4);
print abs_path($file5);
print abs_path($file6);
print abs_path($file7);
print abs_path($file8);
print abs_path($file9);


