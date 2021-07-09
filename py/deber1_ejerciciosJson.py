# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:52:00 2021

@author: aguil
"""
"""
import couchdb
couch = couchdb.Server('http://EFighterf18:bmxextremo17@127.0.0.1:5984')
# db=couch.create('test')#crear
db=couch["ejercicio1"]#referenciar
doc={"nombre":"William","apellido": "Shakespeare"}
doc1={"nombre":"Dave","apellido":"Mustain"}
doc2={"nombre":"Eddi", "apellido":"Vedder"}

# db.save(doc)
# db.save(doc1)
# db.save(doc2)
# for id in range(1000):
#     db.save(doc)
#     db=couch["quito"]
#     print(id)
# for id in db:
#     print(type(id))
# if id in db:
#     print(id["doc"])
    
# db1 = couch.create("pilotos")
# db1 = couch.create("ProyectoArduino")
db1 = couch["pilotos"]
doc={"nombre":"Erick", "apellido":"Andrade", "rango":"Veterano", "horasVuerlo":10000}
doc1={"nombre":"Erick", "nick":"Maverick"}

db1.save(doc)
db1.save(doc1)

print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
for docid in db.view("_all_docs"):
    id=docid["id"]
    doc=db[id]
    print(doc)
for docid in db1.view("_all_docs"):
    id=docid["id"]
    doc=db1[id]
    print(doc)

# db = couch.create("ejericio1")
# db = couch["ejercicio1"]

lista = ["Rosita", "Hugo", "Paco", "Luis"]
for i in lista:
    print(i)
    db1.save
import numpy as np
arra_test1 = np.random.randint(10000,1000000000)
print(arra_test1)
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10))
print(np.random.randint(10, size=10))
#testD
import numpy as np
num = int(np.random.rand()*1000000000)
init = str(np.random.randint(0,2))+str(np.random.randint(1,10))
print(init)
cedula=init+str(num)
print(cedula)

array1 = np.random.randint(1000, 1000000000)
array2 = np.random.randint(1000, 1000000000)
print("Array [1]:", array1)
print("Array [2]:", array1)

array3 = array1 + array2
# array4 = array2.app
# print("Array [3]:", array3)
# print("Array [4]:", array4)



# print(np.random.rand(5,5) * 100)
"""
import couchdb
import numpy as np
print("Ejercicio 1:")
couch = couchdb.Server('http://EFighterf18:bmxextremo17@127.0.0.1:5984')
# db=couch.create('tarea100ejer')#crear
db = couch["tarea100ejer"]

lista = ["Rosita", "Hugo", "Paco", "Luis"]
for i in range(len(lista)):
    doc = {'nombre_1': lista[i]}
    db.save(doc)    
    print("Ejer_1: ",doc)
    
    


print("Ejercicio 2:")
for i in range(101):
    doc = {'numero_Aleatorio': np.random.randint(0,1000000000)}
    db.save(doc)
    print("Ejer_2: ","i=",i,doc)
    
    

print("Ejercicio 3:")

from random import choice

listName =['David', 'Jack', 'Erick', 'Michael', 'Diana', 'Gabriela', 'Belen', 'Anastasio', 'Justin', 'Dennis']
listLastName = ['Fraga', 'Tuquerres', 'Bieber', ' Narvaes', 'Tana', 'Almeida', 'Catota', 'Hurtado', 'Ennarson', 'Thanos']
print(choice(listName))
print(choice(listLastName))

for i in range(101):
    num = int(np.random.rand()*100000000) #incluimos casteo para pasar a int el float
    num2 = str(np.random.randint(0,2)) + str(np.random.randint(1,10))
    #el recorrido se realiza desde (inicial, final) y str concatena como string
    cedula = num2 + str(num)
    doc = {'nombre': choice(listName), 'apellido': choice(listLastName), 'cedula': cedula}
    db.save(doc)
    print("Ejer_3:","i=",i,doc)
    














