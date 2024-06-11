def lista_inversa(lista):
    if len(lista)==0:
        return "la lista está vacía"
    else:
        lista_inversa(lista[1:])
        print(lista[0])

lista_de_animales=["gato","perro","cabra","leon"]
print ("la lista de animales es:", lista_de_animales)
print ("al inverso, queda:")
lista_inversa(lista_de_animales)
