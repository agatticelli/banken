from banks.masterconsultas import MasterConsultas
import os
import re

username = os.environ.get('MASTER_USER')
password = os.environ.get('MASTER_PASS')

mc = MasterConsultas('firefox', username, password)

mc.login()

cards = mc.getCards()

mc.changeToCard(cards[2])

consumptions = mc.getLastConsumptions()

sum_ = 0

for c in consumptions:
    pesos = c['pesos'].replace(' ', '')
    if pesos[-3] == ",":
        pesos = pesos.replace('.', '').replace(',', '.')
    
    sum_ += float(pesos)

print("Total consumido: " + str(round(sum_, 2)))

mc.close()