use strict;
use warnings;

my $file_name = 'collections.csv';
open INPUT, "<$file_name" or die "Can't open '$file_name'$!";

my $oldest;
my $newest;
my $idOldest = 0;
my $idNewest = 0;
my $linecount = 0;
while (my $line = <INPUT>) {
    my @fields = split(",", $line);
    chomp @fields[3];
    if($linecount == 1) {
        $oldest = @fields[3];
        $newest = @fields[3];
        $idOldest = @fields[0];
        $idNewest = @fields[0];
    } else {
        if(@fields[3] > $newest) {
            $newest = (@fields[3]);
            $idNewest = @fields[0];
        }
        if(@fields[3] < $oldest) {
           $oldest = (@fields[3]);
           $idOldest = @fields[0];
        }
    }
    $linecount++;
    print "$line";
}
print "$idOldest\n$idNewest";

