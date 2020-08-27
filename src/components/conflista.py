class Bot:
    def __init__(self, Lista):
        self.Lista = Lista

    def conferirLista(self, Lista):

        self.Lista = Lista

        l = [

        ]

        for i in Lista:
            valor = i.strip()
            if valor not in l:
                l.append(valor)
            else:
                # logica que avisa quantos valores repetidos
                pass

        l.sort()

        self.Lista = l

        conf = True
        
        return self.Lista
