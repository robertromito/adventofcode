for i in $(cat input_sorted) 
do
    for j in $(cat input_sorted)
    do
        sum=$(( $i + $j ))
        if [[ sum -eq 2020 ]]; then
            product=$(( $i * $j ))
            echo "$i + $j = $sum, $i * $j = $product"
            break
        fi
    done
done