use strict;
# use warnings;

my %monthRevenue = (Jan => 4840, Feb => 4340, Mar => 3900,
 Apr => 4330, May => 3090, Jun => 3660, Jul => 3520, Aug => 3280,
 Sep => 4130, Oct => 3690, Nov => 4260, Dec => 4800);

my @keys = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);

print "Enter the initial month: ";
my $iniMonth = <STDIN>;
chomp $iniMonth;
my $match = lc($iniMonth);

$match = ucfirst($match);
my $isValid = 0;
my $iniIndex = 0;
for my $index (0 .. scalar @keys) {
    my $value = @keys[$index];
    if ($match eq $value) {
        $iniMonth = $match;
        $isValid = 1;
        $iniIndex = $index;
    }
}

while ($isValid == 0) {
    print "Please enter only the three initials letters of a valid month.";
    print "Re-enter the initial month: ";

    $match = <STDIN>;
    chomp $match;
    $match = lc($match);
    $match = ucfirst($match);

    for my $index (0 .. scalar @keys) {
        my $value = @keys[$index];
        if ($match eq $value) {
            $iniMonth = $match;
            $isValid = 1;
            $iniIndex = $index;
        }
    }
}

print "Enter the final month: ";
my $finMonth = <STDIN>;

$match = lc($finMonth);
chomp $match;
$match = ucfirst($match);
$isValid = 0;
my $finIndex = 0;

for my $index (0 .. scalar @keys) {
    my $value = @keys[$index];
    if ($match eq $value) {
        if ($index >= $iniIndex) {
            $finMonth = $match;
            $isValid = 1;
            $finIndex = $index;
        }
    }
}

while ($isValid == 0) {
    print "Please enter only the three initials letters of a valid month.\n";
    print "Re-enter the initial month: ";

    $match = <STDIN>;
    chomp $match;
    $match = lc($match);
    $match = ucfirst($match);

    for my $index (0 .. scalar @keys) {
        my $value = @keys[$index];
        if ($match eq $value) {
            if ($index >= $iniIndex) {
                $finMonth = $match;
                $isValid = 1;
                $finIndex = $index;
            }
        }
    }
}

my $cumRev = 0;

for my $index ($iniIndex .. $finIndex) {
    $cumRev += $monthRevenue{@keys[$index]};
}

print "The cumulative revenue is: ";
print $cumRev;