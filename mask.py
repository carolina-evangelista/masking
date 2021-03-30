import math

tipo=int(input('Digite 1 para mascaramento de via aérea e 2 para mascaramento de via óssea: '))
freq=int(input('Digite a frequência a ser mascarada: '))
limiar=int(input('Insira o limiar do paciente: '))
limiarcontr=int(input('Insira o limiar da orelha contrária: '))

def sim(resposta):
    return resposta in ['s','S','y','Y','sim','SIM']

def nao(resposta):
    return resposta in ['n','N','nao','NAO','NÃO','não']


def def_aten():
    if (freq>=250 and freq<=1000):
        atenuacao = 40
    elif (freq>=2000 and freq<=3000):
        atenuacao = 45
    else:
        atenuacao = 50
    return atenuacao

def mask ():
    atenuacao = def_aten()

    if (limiar-atenuacao>limiarcontr-10):
        print('Precisa mascarar!')
        mask=limiar-atenuacao-limiarcontr+10+10+limiarcontr
        maskmax=limiar-15+atenuacao
        supermax=limiar-10+atenuacao
        print('O mascaramento mínimo para', freq, 'Hz é:', mask)
        print('O mascaramento máximo para', freq, 'Hz é:', maskmax)
        print('O supermascaramento para', freq, 'Hz é:', supermax)
    else:
        print('Não precisa mascarar!')
    return mask, supermax

def ossea():
    viaossea=int(input('Insira o limiar de via óssea da orelha testada: '))
    atenuacao = def_aten()

    maskossea=limiarcontr+10
    maskosseamax=viaossea-5+atenuacao
    maskosseasuper=viaossea+atenuacao
    print('O mascaramento mínimo para', freq, 'Hz é:', maskossea)
    print('O mascaramento máximo para', freq, 'Hz é:', maskosseamax)
    print('O supermascaramento para', freq, 'Hz é:', maskosseasuper)

    return maskossea, maskosseasuper

if (tipo==1):
    ruido_min, super_ruido = mask()
elif (tipo==2):
    ruido_min, super_ruido = ossea()

resposta=str(input("O paciente respondeu? Responda n para não e s para sim: "))

while nao(resposta):
    print("\nAumente 5dB de tom puro na orelha testada!\nSe ele responder, aumente 5dB de ruído")
    limiar=limiar+5
    ruido_min += 5
    resposta=str(input("O paciente respondeu? Responda n para não e s para sim: "))
    if sim(resposta):
        print("O mascaramento foi suficiente!")
    if (limiar>=super_ruido):
        print("ATENÇÃO! Não é mais possivel aumentar o mascaramento")
        resposta = 's'
        continue
print("O limiar final foi", limiar)
print("O mascaramento final foi", ruido_min)