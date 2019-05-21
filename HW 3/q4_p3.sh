echo "Enter a sentence: "
read sentence
COUNTER=0
for (( i=0; i<${#sentence}; i++ )); do
    if [ "${sentence:$i:1}" = "k"  ]; then
        let COUNTER=COUNTER+1
    fi
done
echo "$COUNTER"