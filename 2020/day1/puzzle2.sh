for i in $(cat input_sorted) 
do
    echo "checking $i"
    for j in $(cat input_sorted)
    do
        for k in $(cat input_sorted)
        do
            sum=$(( $i + $j + $k ))
            if [[ sum -eq 2020 ]]; then
                product=$(( $i * $j * $k ))
                echo "$i + $j + $k = $sum, $i * $j * $k = $product"
                exit
            fi
        done
    done
done