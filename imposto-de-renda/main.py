
salario = float (input("Informe o seu salário atual: "))
impostoDeRenda = 0.00

if salario <= 1903.98:
  impostoDeRenda = 0  
elif salario <= 2826.65:
  impostoDeRenda = (salario-1903.98)*0.075
elif salario <= 3751.05:
  impostoDeRenda = (922.66*0.075)+((salario - 2826.65)*0.15)
elif salario <= 4664.68:
  impostoDeRenda = (922.66*0.075)+(924.39*0.15)+((salario-3751.05)*0.225)
else:
  impostoDeRenda = (922.66*0.075)+(924.39*0.15)+(913.62*0.225)+((salario-4664.68)*0.275)

if impostoDeRenda > 0:
  print("Fr$ ", round(impostoDeRenda,2))
else:
  print('Isento')