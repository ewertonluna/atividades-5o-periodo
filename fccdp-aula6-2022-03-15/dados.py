import data_pb2 as data
from msilib.schema import File
file = open("data_proto.txt","w")

dados = data.Person()
people_list = list()

p1 = data.Person()
p1.id = 100000001
p1.name = "Luz Canto Bonito"
people_list.append(p1)

p2 = data.Person()
p2.id = 100000002
p2.name = "Vitória Cortês Vigário"
people_list.append(p2)

p3 = data.Person()
p3.id = 100000003
p3.name = "Esperança Carvalho Dinis"
people_list.append(p3)

p4 = data.Person()
p4.id = 100000004
p4.name = "Nikita Berenguer Barbalho"
people_list.append(p4)

p5 = data.Person()
p5.id = 100000005
p5.name = "Ícaro Narvais Salazar"
people_list.append(p5)

p6 = data.Person()
p6.id = 100000006
p6.name = "Angélico Peseiro Varela"
people_list.append(p6)

p7 = data.Person()
p7.id = 100000007
p7.name = "Elisama Caetano Cardim"
people_list.append(p7)

p8 = data.Person()
p8.id = 100000008
p8.name = "Kevyn Adarga Breia"
people_list.append(p8)

p9 = data.Person()
p9.id = 100000009
p9.name = "Keyla Castilhos Ribeiro"
people_list.append(p9)

p10 = data.Person()
p10.id = 100000010
p10.name = "Samoa Cerveira Rufino"
people_list.append(p10)

p11 = data.Person()
p11.id = 100000011
p11.name = "Yi Ponte Parente"
people_list.append(p11)

p12 = data.Person()
p12.id = 100000012
p12.name = "Anderson Matos Chainho"
people_list.append(p12)

p13 = data.Person()
p13.id = 100000013
p13.name = "Jorge Teles Rebelo"
people_list.append(p13)

p14 = data.Person()
p14.id = 100000014
p14.name = "Humberto Areosa Rabelo"
people_list.append(p14)

p15 = data.Person()
p15.id = 100000015
p15.name = "Lília Amado Fontes"
people_list.append(p15)

p16 = data.Person()
p16.id = 100000016
p16.name = "Máximo Mariz Frajuca"
people_list.append(p16)

p17 = data.Person()
p17.id = 100000017
p17.name = "Valdemar Caeiro Proença"
people_list.append(p17)

p18 = data.Person()
p18.id = 100000018
p18.name = "Gaia Boga Esparteiro"
people_list.append(p18)

p19 = data.Person()
p19.id = 100000019
p19.name = "Benjamin Freire Portugal"
people_list.append(p19)

p20 = data.Person()
p20.id = 100000020
p20.name = "Tobias Bezerril Lagos"
people_list.append(p20)

p21 = data.Person()
p21.id = 100000021
p21.name = "Neide Saldanha Aguiar"
people_list.append(p21)

p22 = data.Person()
p22.id = 100000022
p22.name = "Diogo Frajuca Valadim"
people_list.append(p22)

p23 = data.Person()
p23.id = 100000023
p23.name = "Louis Fialho Assis"
people_list.append(p23)

p24 = data.Person()
p24.id = 100000024
p24.name = "Adelaide Figueiredo Azenha"
people_list.append(p24)

p25 = data.Person()
p25.id = 100000025
p25.name = "Yaroslav Escobar Amarante"
people_list.append(p25)

p26 = data.Person()
p26.id = 100000026
p26.name = "Eduardo Galvão Grilo"
people_list.append(p26)

p27 = data.Person()
p27.id = 100000027
p27.name = "Nicolau Pestana Raminhos"
people_list.append(p27)

p28 = data.Person()
p28.id = 100000028
p28.name = "Piedade Machado Vieira"
people_list.append(p28)

register = data.Register()
register.peoplelist.extend(people_list)


print(register)

file.write(register.__str__())
file.close()

