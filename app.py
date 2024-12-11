from abc import ABC, abstractmethod

# Componente base - Figura (classe abstrata)
class Figura(ABC):
    @abstractmethod
    def desenhar(self):
        pass

# Classe Círculo - Figura individual (folha)
class Circulo(Figura):
    def __init__(self, raio: float):
        self.raio = raio

    def desenhar(self):
        print(f"Desenhando um Círculo com raio {self.raio}")

# Classe Quadrado - Figura individual (folha)
class Quadrado(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def desenhar(self):
        print(f"Desenhando um Quadrado com lado {self.lado}")

# Classe Grupo de Figuras - Nó composto
class GrupoFigura(Figura):
    def __init__(self):
        self.figuras = []

    def adicionar_figura(self, figura: Figura):
        self.figuras.append(figura)

    def remover_figura(self, figura: Figura):
        self.figuras.remove(figura)

    def desenhar(self):
        print("Desenhando Grupo de Figuras:")
        for figura in self.figuras:
            figura.desenhar()

# Exemplo de uso
if __name__ == "__main__":
    # Criando figuras individuais
    circulo1 = Circulo(5)
    quadrado1 = Quadrado(3)

    # Criando um grupo de figuras
    grupo1 = GrupoFigura()
    grupo1.adicionar_figura(circulo1)
    grupo1.adicionar_figura(quadrado1)

    # Criando um grupo maior que contém outros grupos
    grupo2 = GrupoFigura()
    grupo2.adicionar_figura(grupo1)
    
    # Criando mais figuras para o grupo maior
    circulo2 = Circulo(10)
    grupo2.adicionar_figura(circulo2)

    # Desenhando tudo
    print("Desenhando grupo maior (grupo2):")
    grupo2.desenhar()
