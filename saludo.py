
class Saludo:
    def __init__(self):
        self.mensaje = "Hola, estoy aquí"
    
    def decir_hola(self):
        return self.mensaje

if __name__ == "__main__":
    saludo = Saludo()
    print(saludo.decir_hola())
    