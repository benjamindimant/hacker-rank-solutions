read -r n
for i in $(seq 1 $n)
do
    read -r x
    sum=$((sum + x))
done
printf "%.3f" $(echo "$sum / $n" | bc -l)
