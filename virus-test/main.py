import random # para sortear valores

# Inicializa gerador (vai gerar SEMPRE a mesma sequência)
random.seed(42)

# Use este trecho de programa para sortear os
# valores necessários DENTRO da repetição

# MAS NÃO ALTERE NENHUMA DAS LINHAS ABAIXO!
totalPositivos = 0
totalNegativos = 0

contaminadosNegativos = 0
contaminadosPositivos = 0

naoContaminadosTesteNegativos = 0
naoContaminadosTestePositivos = 0

totalMulheres = 0
contaminadosNegativosFeminino = 0
contaminadosPositivosFeminino = 0

totalHomens = 0
contaminadosNegativosMasculino = 0
contaminadosPositivosMasculino = 0

totalAdolescentes = 0
contaminadosNegativosAdolescentes = 0
contaminadosPositivosAdolescentes = 0

totalJovens = 0
contaminadosNegativosJovens = 0
contaminadosPositivosJovens = 0

totalAdulto = 0
contaminadosNegativosAdulto = 0
contaminadosPositivosAdulto = 0

totalIdosos = 0
contaminadosNegativosIdosos = 0
contaminadosPositivosIdosos = 0

totalSenhores = 0
contaminadosNegativosSenhores = 0
contaminadosPositivosSenhores = 0

for x in range(10000):

  prob = random.gauss(90,10)

  genero = random.choice(["m","f"])

  idade = int(random.lognormvariate(0, 0.25) / 2.5952152896850245 * 100)

  if prob < 85:
    resultado = "p"
    correto = random.gauss(90,10)
  else:
    resultado = "n"
    correto = random.gauss(85,10)

  if correto > 65:
    estaCorreto = True
  else:
    estaCorreto = False
  
  #Resultados

  if resultado == "p":
    totalPositivos= totalPositivos+1
  else:
    totalNegativos=totalNegativos+1

    
  #Total de Contaminados - sensibilidade

  if (resultado == "p") and (estaCorreto == True):
    contaminadosPositivos = contaminadosPositivos + 1
  if (resultado == "n") and (estaCorreto == False):
    contaminadosNegativos = contaminadosNegativos + 1

  #Não contaminados - especificidade

  if (resultado == "p") and (estaCorreto == False):
    naoContaminadosTestePositivos = naoContaminadosTestePositivos + 1
  if (resultado == "n") and (estaCorreto == True):
    naoContaminadosTesteNegativos = naoContaminadosTesteNegativos + 1

  #Prevalencia por genero

  if genero == "f":

    totalMulheres = totalMulheres+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosFeminino = contaminadosPositivosFeminino + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosFeminino = contaminadosNegativosFeminino + 1

  else:

    totalHomens = totalHomens+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosMasculino = contaminadosPositivosMasculino + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosMasculino = contaminadosNegativosMasculino + 1

  #Prevalencia por idade
  if idade < 21:

    totalAdolescentes = totalAdolescentes+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosAdolescentes = contaminadosPositivosAdolescentes + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosAdolescentes = contaminadosNegativosAdolescentes + 1

  elif idade < 41:

    totalJovens = totalJovens+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosJovens = contaminadosPositivosJovens + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosJovens = contaminadosNegativosJovens + 1
  
  elif idade < 61:

    totalAdulto = totalAdulto+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosAdulto = contaminadosPositivosAdulto + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosAdulto = contaminadosNegativosAdulto + 1

  elif idade < 81:

    totalIdosos = totalIdosos+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosIdosos = contaminadosPositivosIdosos + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosIdosos = contaminadosNegativosIdosos + 1

  else:
    totalSenhores = totalSenhores+1

    if (resultado == "p") and (estaCorreto == True):
      contaminadosPositivosSenhores = contaminadosPositivosSenhores + 1
    if (resultado == "n") and (estaCorreto == False):
      contaminadosNegativosSenhores = contaminadosNegativosSenhores + 1
  

#Fim do loop


print("Testes positivos: ", totalPositivos)
print("Testes negativos: ", totalNegativos) 

print("\nTestes verdadeiro positivo: ", contaminadosPositivos)
print("Testes falso positivo: ", naoContaminadosTestePositivos)
print("Testes verdadeiro negativo: ", naoContaminadosTesteNegativos) 
print("Testes falso negativo: ", contaminadosNegativos) 


totalContaminados = contaminadosNegativos + contaminadosPositivos 
    
#Sensibilidade
sensibilidade = contaminadosPositivos/totalContaminados
porcentagemSensibilidade = sensibilidade*100
print("\nSensibilidade do teste: ",round(porcentagemSensibilidade,2),"%")


totalNaoContaminados = naoContaminadosTesteNegativos + naoContaminadosTestePositivos

#Especificidade
especificidade = naoContaminadosTesteNegativos/totalNaoContaminados
porcentagemEspecificidade = especificidade*100
print("Especificidade do teste: ",round(porcentagemEspecificidade,2),"%")

#Prevalencia Total
prevalencia = totalContaminados/10000
porcentagemPrevalencia = prevalencia*100
print("\nPrevalencia do teste: ",round(porcentagemPrevalencia,2),"%")

#Prevalencia Feminina
mulheresContaminadas = contaminadosNegativosFeminino + contaminadosPositivosFeminino
prevalenciaFeminina = mulheresContaminadas/totalMulheres
porcentagemPrevalenciaFeminina = prevalenciaFeminina*100
print("\nPrevalencia feminina do teste: ",round(porcentagemPrevalenciaFeminina,2),"%")

#Prevalencia Masculina
homensContaminados = contaminadosNegativosMasculino + contaminadosPositivosMasculino
prevalenciaMasculina = homensContaminados/totalHomens
porcentagemPrevalenciaMasculina = prevalenciaMasculina*100
print("Prevalencia masculina do teste: ",round(porcentagemPrevalenciaMasculina,2),"%")

#Prevalencia por faixa etária
print("\nPREVALENCIA POR FAIXA ETÁRIA")

#0-20   Adolescentes
adolescentesContaminados = contaminadosNegativosAdolescentes + contaminadosPositivosAdolescentes
prevalenciaAdolescentes = adolescentesContaminados/totalAdolescentes
porcentagemPrevalenciaAdolescentes = prevalenciaAdolescentes*100
print("Prevalencia de 0-20 anos do teste: ",round(porcentagemPrevalenciaAdolescentes,2),"%")

#21-40 Jovens
jovensContaminados = contaminadosNegativosJovens + contaminadosPositivosJovens
prevalenciaJovens = jovensContaminados/totalJovens
porcentagemPrevalenciaJovens = prevalenciaJovens*100
print("Prevalencia de 21-40 anos do teste: ",round(porcentagemPrevalenciaJovens,2),"%")

#41-60 Adulto
adultoContaminados = contaminadosNegativosAdulto + contaminadosPositivosAdulto
prevalenciaAdulto = adultoContaminados/totalAdulto
porcentagemPrevalenciaAdulto = prevalenciaAdulto*100
print("Prevalencia de 41-60 anos do teste: ",round(porcentagemPrevalenciaAdulto,2),"%")

#61-80 Idosos
idososContaminados = contaminadosNegativosIdosos + contaminadosPositivosIdosos
prevalenciaIdosos = idososContaminados/totalIdosos
porcentagemPrevalenciaIdosos = prevalenciaIdosos*100
print("Prevalencia de 61-80 anos do teste: ",round(porcentagemPrevalenciaIdosos,2),"%")

#acima de 80 Senhores
senhoresContaminados = contaminadosNegativosSenhores + contaminadosPositivosSenhores
prevalenciaSenhores = senhoresContaminados/totalSenhores
porcentagemPrevalenciaSenhores = prevalenciaSenhores*100
print("Prevalencia acima de 80 anos do teste: ",round(porcentagemPrevalenciaSenhores,2),"%")