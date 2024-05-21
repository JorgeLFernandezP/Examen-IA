# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:45:38 2024

@author: USUARIO
"""

from kanren import Relation, facts, run, var, lall, conde

padre = Relation()
madre = Relation()
facts(padre, ("Zac", "Jorge"),
               ("Zac", "Fabiola"),
               ("Zac", "Viviana"),
               ("Gabino",  "Zac"),
               ("Gabino",  "Ismael"),
               ("Eduardo", "Gregoria"),
               ("Eduardo", "Ramon"),
               ("Ramon", "Maria"),
               ("Ramon", "Carlos"))

facts(madre, ("Luisa", "Zac"),
                ("Luisa", "Ismael"),
                ("Rafaela", "Gregoria"),
                ("Rafaela", "Ramon"),
                ("Gregoria", "Fabiola"),
                ("Gregoria", "Jorge"),
                ("Gregoria", "Viviana"),
                ("Corsina", "Maria"),
                ("Corsina", "Carlos"))

x = var()

def abuelosP(x, z):
     y = var()
     return lall(padre(x, y), padre(y, z), madre(x,y), madre(y,z))
 
def abuelosM(x, z):
     y = var()
     return lall(madre(x, y), madre(y, z))
 
def abuelos(x, z):
    y = var()
    return conde((padre(x, y), padre(y, z)) , (madre(x, y), padre(y, z)), (madre(x, y), madre(y, z)), (padre(x, y), madre(y, z)))

# Definir la relación de hijo
def hijo(p, q):
    return conde((padre(p, q),), (madre(p, q),))
    
# Definir la relación de hermano
def hermano(p, q):
    x = var()
    y = var()
    return conde((madre(x, p), madre(x, q)), 
                 (padre(y, p), padre(y, q)))
    
def hermanos(nombre):
    x = var()
    # Ejecutar la consulta y guardar los resultados en la lista
    resultado = list(set(run(0,x, hermano(nombre, x))))
    
    if nombre in resultado:
        resultado.remove(nombre)
    if not resultado:
        return 0
    
    return resultado
   

def tio(nombre):
    # Obtener los padres de la persona
    pa = run(0, x, padre(x, nombre))
    ma = run(0, x, madre(x, nombre))
    
    # Obtener los hermanos de cada padre
    rp = hermanos(pa[0])
    rm = hermanos(ma[0])
    
    if rp ==0:
        resultado = rm
    if rm == 0:
        resultado = rp
    
    # Combinar ambas listas de hermanos
    if (rp!=0 and rm !=0):
        resultado = rp + rm
    
    # Devolver la longitud de la lista combinada
    return resultado

def primos(nombre):
    t = tio(nombre)
    
    for i in range(len(t)):
        h = run(0, x, hijo(t[i],x))
    
    return h


print("DEPENDENCIA DE ABUELOS Y NIETOS:")
print(run(0, x, abuelos(x, 'Fabiola')))
print(run(0, x, abuelos(x, 'Maria')))

print(run(0, x, abuelos("Eduardo", x)))

print("------------------------------------------\n")

print("DEPENDENCIA DE PADRES E HIJOS:")
print(run(0, x, padre(x, "Jorge")))

print(run(0, x, madre(x, "Jorge")))

print(run(0, x, hijo("Gregoria",x)))
print("------------------------------------------\n")

print("DEPENDENCIA DE HERMANOS:")
print(hermanos("Jorge"))
print("------------------------------------------\n")

print("DEPENDENCIA DE TIOS:")
print(tio("Jorge"))
print("------------------------------------------\n")

print("DEPENDENCIA DE PRIMOS:")
print(primos("Jorge"))



