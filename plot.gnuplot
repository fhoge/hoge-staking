set terminal svg size 768,480 enhanced background rgb 'white' name "hoge_staking"
set output 'staked.svg'

set border 1+2 back

set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%Y-%m-%d"
set xtics 86400
set xtics rotate

set grid ytics
set grid xtics
set tics nomirror out scale 0.75

set ylabel 'hoge'

set datafile separator ','
plot 'staked.csv' using 1:2 smooth unique lw 2 lt rgb "#ffa600" title ""
