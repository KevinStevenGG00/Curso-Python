curso_actual = 1.5
curso_min = 2.5
curso_max = 7.0
curso_prom = 4

#Diferencia porcentual de tiempos

dif_porcentual_actual_y_min = 100 - (curso_actual*100/curso_min)
dif_porcentual_actual_y_max = 100 - (curso_actual/curso_max *100)
dif_porcentual_actual_y_prom = 100 - (curso_actual/curso_prom *100)

resultado1 = 100 * 1/2.5
resultado2 = 10000 * 5.5//70/10
resultado3 = 100 * 2.5/4

print("------------------------------------------")
print(f"El curso actual dura {resultado1}% menos que el más rápido")
print(f"El curso actual dura {resultado2}% menos que el más lento")
print(f"El curso actual dura {resultado3}% menos que el promedio")

#porcentaje de tiempo vacío removido

crudo_prom = 5
crudo_actual = 3.5

tiempo_vacio_actual = 100 - (1000*curso_actual//crudo_actual/10)
tiempo_vacio_prom = 100 - (100*curso_prom/crudo_prom)

print("------------------------------------------")
print(f"El curso actual elimina un {tiempo_vacio_actual}% de tiempo vacio")
print(f"El curso promedio elimina un {tiempo_vacio_prom}% de tiempo vacio")

#equivalencia de 10 hrs del curso actual con otros

resultado4 = 100*curso_prom//curso_actual/10
resultado5 = 100*curso_min//curso_actual/10
resultado6 = 100*curso_max//curso_actual/10

print("------------------------------------------")
print(f"Ver 10 hrs de este curso equivale a ver {resultado4} hrs de un curso promedio")
print(f"Ver 10 hrs de este curso equivale a ver {resultado5} hrs de un curso rápido")
print(f"Ver 10 hrs de este curso equivale a ver {resultado6} hrs de un curso lento")

print("------------------------------------------")
print(f"Ver 10 hrs de un curso promedio equivale a ver {100*curso_actual//curso_prom/10} hrs del curso actual")