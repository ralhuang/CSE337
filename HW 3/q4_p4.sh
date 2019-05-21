# Write a shell script that counts the number of 
# directories under a directory provided as a 
# command line parameter, without using the ls 
# command, then prints the number to the screen.

echo "$(find ${1/*} -maxdepth 0 -type d | wc -l)"