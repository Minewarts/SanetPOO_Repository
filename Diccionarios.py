estudiantes={
    "Lucia":[4.5,3.8,4.2],
    "Mateo":[3.0,3.5,4.0,4.2],
    "Sofia":[5.0,4.8,4.9],
}
promedios={}
for nombre, notas in estudiantes.items():
    prom=sum(notas)/len(notas)
    print (f'Promedio de {nombre}: {prom:.2f}')
    promedios[nombre]=prom

mayorPromedio= max(promedios, key=promedios.get)