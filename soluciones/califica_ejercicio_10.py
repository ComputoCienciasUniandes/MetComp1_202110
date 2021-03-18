import ejercicio_10 as e


c = e.covarianza(0.5, 0.1, 10)
print(c, -0.5*0.1*10)
c = e.covarianza(0.1, 0.8, 20)
print(c, -0.1*0.8*20)
c = e.covarianza(0.3, 0.3, 50)
print(c, -0.3*0.3*50)
