class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamaño(self):
        return len(self.items)

# Lista de dinosaurios
dinosaurios = [
    {
        "nombre": "Tyrannosaurus Rex",
        "especie": "Theropoda",
        "peso": "7000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1902
    },
    {
        "nombre": "Triceratops",
        "especie": "Ceratopsidae",
        "peso": "6000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1889
    },
    {
        "nombre": "Velociraptor",
        "especie": "Dromaeosauridae",
        "peso": "15 kg",
        "descubridor": "Henry Fairfield Osborn",
        "ano_descubrimiento": 1924
    },
    {
        "nombre": "Brachiosaurus",
        "especie": "Sauropoda",
        "peso": "56000 kg",
        "descubridor": "Elmer S. Riggs",
        "ano_descubrimiento": 1903
    },
    {
        "nombre": "Stegosaurus",
        "especie": "Stegosauridae",
        "peso": "5000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Spinosaurus",
        "especie": "Spinosauridae",
        "peso": "10000 kg",
        "descubridor": "Ernst Stromer",
        "ano_descubrimiento": 1912
    },
    {
        "nombre": "Allosaurus",
        "especie": "Theropoda",
        "peso": "2000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Apatosaurus",
        "especie": "Sauropoda",
        "peso": "23000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Diplodocus",
        "especie": "Sauropoda",
        "peso": "15000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1878
    },
    {
        "nombre": "Ankylosaurus",
        "especie": "Ankylosauridae",
        "peso": "6000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1908
    },
    {
        "nombre": "Parasaurolophus",
        "especie": "Hadrosauridae",
        "peso": "2500 kg",
        "descubridor": "William Parks",
        "ano_descubrimiento": 1922
    },
    {
        "nombre": "Carnotaurus",
        "especie": "Theropoda",
        "peso": "1500 kg",
        "descubridor": "José Bonaparte",
        "ano_descubrimiento": 1985
    },
    {
        "nombre": "Styracosaurus",
        "especie": "Ceratopsidae",
        "peso": "2700 kg",
        "descubridor": "Lawrence Lambe",
        "ano_descubrimiento": 1913
    },
    {
        "nombre": "Therizinosaurus",
        "especie": "Therizinosauridae",
        "peso": "5000 kg",
        "descubridor": "Evgeny Maleev",
        "ano_descubrimiento": 1954
    },
    {
        "nombre": "Pteranodon",
        "especie": "Pterosauria",
        "peso": "25 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1876
    },
    {
        "nombre": "Quetzalcoatlus",
        "especie": "Pterosauria",
        "peso": "200 kg",
        "descubridor": "Douglas A. Lawson",
        "ano_descubrimiento": 1971
    },
    {
        "nombre": "Plesiosaurus",
        "especie": "Plesiosauria",
        "peso": "450 kg",
        "descubridor": "Mary Anning",
        "ano_descubrimiento": 1824
    },
    {
        "nombre": "Mosasaurus",
        "especie": "Mosasauridae",
        "peso": "15000 kg",
        "descubridor": "William Conybeare",
        "ano_descubrimiento": 1829
    }
]

pila_dinosaurios = Pila()

for dino in dinosaurios:
    pila_dinosaurios.apilar(dino)

def contar_especies(pila):
    especies = set()
    pila_aux = Pila()

    while not pila.esta_vacia():
        dino = pila.desapilar()
        especies.add(dino["especie"])
        pila_aux.apilar(dino)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return len(especies)

print("cantidad de especies:", contar_especies(pila_dinosaurios))

def contar_descubridores(pila):
    descubridores = set()
    pila_aux = Pila()

    while not pila.esta_vacia():
        dino = pila.desapilar()
        descubridores.add(dino["descubridor"])
        pila_aux.apilar(dino)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return len(descubridores)

print("descubridores:", contar_descubridores(pila_dinosaurios))

def mostrar_dinosaurios_con_t(pila):
    pila_aux = Pila()
    dinos_con_t = []

    while not pila.esta_vacia():
        dino = pila.desapilar()
        if dino["nombre"].startswith('T'):
            dinos_con_t.append(dino["nombre"])
        pila_aux.apilar(dino)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return dinos_con_t

print("los dinosaurios que empiezan con T son  :", mostrar_dinosaurios_con_t(pila_dinosaurios))

def mostrar_dinosaurios_ligeros(pila, peso_max):
    pila_aux = Pila()
    dinos_ligeros = []

    while not pila.esta_vacia():
        dino = pila.desapilar()
        if int(dino["peso"].split()[0]) < peso_max:
            dinos_ligeros.append(dino["nombre"])
        pila_aux.apilar(dino)
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return dinos_ligeros

print("los dinosaurios que pesan menos de 275 kg son:", mostrar_dinosaurios_ligeros(pila_dinosaurios, 275))

def apilar_dinosaurios_con_aqs(pila):
    pila_aux = Pila()
    pila_aqs = Pila()

    while not pila.esta_vacia():
        dino = pila.desapilar()
        if dino["nombre"].startswith(('A', 'Q', 'S')):
            pila_aqs.apilar(dino)
        pila_aux.apilar(dino)
    
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    
    return pila_aqs

pila_dinosaurios = Pila()
for dino in dinosaurios:
    pila_dinosaurios.apilar(dino)

pila_dinos_aqs = apilar_dinosaurios_con_aqs(pila_dinosaurios)

dinos_aqs_list = []
while not pila_dinos_aqs.esta_vacia():
    dinos_aqs_list.append(pila_dinos_aqs.desapilar()["nombre"])

print("losinosaurios que comienzan con A, Q, S en una nueva pila son:", dinos_aqs_list)


