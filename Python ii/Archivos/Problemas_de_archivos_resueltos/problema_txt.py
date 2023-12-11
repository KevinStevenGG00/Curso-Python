##dos listas una con nombres y otra con apellidos
nombres = ["Kevin","Clara","Kemi","Cesar","Christopher"]
apellidos = ["Godoy","Goicochea","Godoy","Godoy","Godoy"]

##registrar esta información en un txt de forma óptima

with open("archivos\\Problemas_de_archivos_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines(" * Los datos son: *\n\n")
    ##for en una sola línea
    [arch.writelines(f"- Nombre: {n}\n- Apellido: {a}\n-------------------\n") for n,a in zip(nombres,apellidos)]

##for normal
#for n,a in zip(nombres,apellidos):
#    arch.writelines(f"- Nombre: {n}\n- Apellido: {a}\n-------------------\n")