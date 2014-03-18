set terminal png
set output "sun_azimut.png"
f(x) = a*exp(-(x-d)**2/b)+c
#a=31000
#b=11
#c=1
#d=-5
fit f(x) "sun_azimut" using 1:3 via a, b, c, d
set xlabel "angepasstes Azimut in °"
set ylabel "Intensität in K"
set grid
set key
set xrange [-20:10]
set yrange [-5000:36000]
plot f(x) title "Fit", "sun_azimut" using 1:3:4 with yerrorbars title "Messung"
