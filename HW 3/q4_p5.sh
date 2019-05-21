MIN=$1
MAX=$1
for num in "${@}"
  do
     if [[ $num -gt $MAX ]];
     then 
         MAX=$num
     fi
     if [[ $num -lt $MIN ]];
     then
        MIN=$num
     fi
  done

echo "MIN = $MIN"
echo "MAX = $MAX"

arr=( $(printf '%d\n' "${@}" | sort -n ))
let "nel=$#"
if (( $nel % 2 == 1 )); then
    med="${arr[ $(($nel/2)) ]}"
else
    (( j=nel/2 ))
    (( k=j-1 ))
    (( med=(${arr[j]} + ${arr[k]})/2 ))
fi
echo $med
