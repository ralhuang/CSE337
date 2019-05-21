COUNTER = 0
while [ $COUNTER -lt 10 ]
do
    if [ $(($COUNTER%2)) -eq 0 ]; then
        x=even"$COUNTER"
        touch "$x"
        chmod 554 "$x"
    else
        x=odd"$COUNTER"
        touch "$x"
        chmod 554 "$x"
    fi
    let COUNTER=COUNTER+1
done