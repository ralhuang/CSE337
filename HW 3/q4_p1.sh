cd "$1"

printf "Current shell is: %s\n" $SHELL
printf "Current directory is : %s\n " $PWD
printf "Home directory is : %s\n" $HOME
printf "\n"
printf "— 5 most recently modified non-empty subdirectories—\n"

find $PWD -mindepth 1 -maxdepth 1 -not -empty -type d -printf "%M %1n %-1u %-1g %1s %Tx %.8TX %p\n" | head -5

printf "\n"
printf "— Files in last 45 minutes—"
echo "$( find . -mmin -45 -size +1000c )"
printf "\n"
printf "%.s=" {1..70}
printf "\n"


