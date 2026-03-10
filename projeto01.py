import math
import random
import datetime
import statistics
import locale

#Monetário
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#inicial
capital = float(input("Digite o capital inicial (R$): "))
aporte = float(input("Digite o aporte mensal (R$): "))
meses = int(input("Prazo mensal: "))
cdi_anual = float(input("CDI anual (%): "))/100
perc_cdb = float(input("Percentual do CDI (%)"))/100
perc_lci = float(input("Percentual do LCI (%)"))/100
taxa_fii = float(input("Porcentalidade mensal FII (%): "))/100
meta = float(input("Meta financeira (R$): "))

#CDI
cdi_mensal = math.pow((1+cdi_anual),1/12) - 1
total_investido = capital + (aporte*meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb), meses) + (aporte * meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses) + (aporte * meses))

#Poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1+taxa_poupanca), meses) + (aporte * meses))

#FII - Simulações
montante_fii = (capital * math.pow((1+ taxa_fii), meses) + (aporte * meses))
sim_fii1 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii2 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii3 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii4 = montante_fii * (1 + random.uniform (-0.03,0.03))
sim_fii5 = montante_fii * (1 + random.uniform (-0.03,0.03))

lista_fii = (sim_fii1, sim_fii2, sim_fii3, sim_fii4, sim_fii5)

media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)


#Data de resgate
data_atual = datetime.datetime.now()
data_final = data_atual + datetime.timedelta(days = meses * 30)

#Relatório final





