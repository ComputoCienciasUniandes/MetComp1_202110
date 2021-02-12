def angulo_sol(time):
    hour =  float(time[0:2])
    minute = float(time[3:])
    if hour<6 or (hour==18 and minute > 0) or hour>19:
        return "No hay sol"
    else:
        angle = 15*(hour-6)+(15/60)*minute
        return float(angle)
              
print(angulo_sol("12:30"))
print(angulo_sol("07:00"))
print(angulo_sol("05:55"))