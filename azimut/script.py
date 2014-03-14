from math import*

def stunde(stunde, minu, sec):
  result = stunde + minu/60.0 + sec/3600.
  return(result)
  
def rest(a, b):
  while a >= b:
    a -= b
  return(a)  
  
def hmin(stunden,i):
  y = 1.0
  if(stunden < 0):
    y = -1.0
    stunden = - stunden
  result = [0,0,0]
  result[0] = (stunden - rest(stunden,1))
  result[2] = rest(60.*(stunden - result[0]), 1)*60.
  result[1] = (rest(stunden, 1)*60-result[2]/60.0)
  return(y*result[i])
  
def azimut(unitime, turm, sonne):
  sternzeit_gr = stunde(12, 05, 27.5731) # sternzeit in Greenwich 0 Uhr TT
  pos_B = stunde(0, 43, 33.5) #Bamberg in Stundenwinkel
  tt = unitime + stunde(0, 0, 66.0) #Umrechnung in TT 
  alpha_0 = stunde(0,11,54.63)/12.0*pi # alpha zu Beginn des Tages
  alpha_1 = stunde(0,15,33.08) /12.0*pi # alpha zu Beginn des Folgetages
  delta_0 = stunde(1, 17,24.3)/180.0*pi # delta zu Beginn des Tages
  delta_1 = stunde(1, 41, 1.2) /180.0*pi # delta zu Beginn des Folgetages
  alpha = alpha_0 + (alpha_1 - alpha_0)*(tt/24.0) # interpoliert
  delta = delta_0 + (delta_1 - delta_0)*(tt/24.0) # interpoliert
  Phi = stunde(49, 53, 9)/180.0*pi # breitengrad bamberg
 
  theta_Bam = sternzeit_gr + pos_B + unitime*1.002738 # lokale sternzeit
  
  tau_sol = theta_Bam/12.*pi - alpha # stundenwinkel sonne
  M = atan(tan(delta)/cos(tau_sol)) 

  az = atan((cos(M)*tan(tau_sol))/(sin(Phi-M))) # azimut
  if(az < 0):
    az = 2*pi + az
  #print("alpha = ", hmin(alpha*12./pi,0), hmin(alpha*12./pi,1), hmin(alpha*12./pi,2) )
  #print("delta = ",  hmin(delta*180./pi,0), hmin(delta*180./pi,1), hmin(delta*180./pi,2) )
  #print("theta_Bam =", hmin(theta_Bam,0), hmin(theta_Bam,1), hmin(theta_Bam,2) )
  #print("Tau_Sonne = ", hmin(tau_sol*12.0/pi,0), hmin(tau_sol*12.0/pi,1), hmin(tau_sol*12.0/pi,2) )
  #print("M = ", hmin(M*180/pi,0), hmin(M*180/pi,1), hmin(M*180/pi,2) )
  #print("a_Sonne = ", hmin(az*180/pi, 0), hmin(az*180/pi, 1), hmin(az*180/pi, 2))
  delta_az = (turm - sonne)
  az = az*180/pi
  az_turm = az + delta_az 
  print(az)

azimut(stunde(9,50,8.91), stunde(117, 40, 23.125), stunde(180, 13, 54))
azimut(stunde(9,57,37.19), stunde(117, 40, 23.125), stunde(182, 29, 1))
azimut(stunde(10,1,22.56), stunde(117, 40, 23.125), stunde(183, 37, 44))
azimut(stunde(10, 5, 18.025), stunde(117, 40, 23.125), stunde(184, 50, 8))
azimut(stunde(10, 18, 47.44), stunde(117, 40, 23.125), stunde(189, 3, 4))
azimut(stunde(10, 22, 30.915), stunde(117, 40, 23.125), stunde(190, 13, 49))
azimut(stunde(10, 27, 19.18), stunde(117, 40, 23.125), stunde(191, 45, 55))
azimut(stunde(10, 31, 34.13), stunde(117, 40, 23.125), stunde(193, 7, 52))
