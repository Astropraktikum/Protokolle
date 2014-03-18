#!/usr/bin/env python2
from __future__ import print_function
import sys
import numpy
sys.argv
finname="cross_sun.rad"
foutname="cross_sun.plot"
fin=open(finname)
finstr=fin.read()
fin.close()
out=[]
temp=5284
flist=finstr.splitlines()
freq=0
for (nummer, eintrag) in enumerate(flist):
    if eintrag.startswith("*"):
        elevation=eintrag.split()[7]
        azimut=eintrag.split()[6]
        mean=numpy.mean(map(float,flist[nummer+1].split()[-56:-8]))
        stderr=numpy.std(map(float,flist[nummer+1].split()[-56:-8]))
        out.append(elevation + "\t" + azimut + "\t" + str(mean-temp) + "\t" + str (stderr))
fout=open(foutname, "w")
print(*out, file=fout, sep="\n")
fout.close()
