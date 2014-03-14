from math import*
x = [267.648654956,
267.649734349,
267.650203207,
267.649674697,
267.647492394,
267.648884494,
267.646924116,
267.646039568]
mean = 0
i = 0
while i<8:
  mean += x[i]
  i += 1
mean = mean/8.0
var = 0
i = 0
while i<8:
  var += (mean - x[i])**2
  i += 1
sig = sqrt(var/7.0)
fehl = sig/sqrt(8.0)
print(mean, fehl)
