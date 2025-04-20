"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Josep Esquerrà Bayo

    Clase Vector que implementa operacions com el producte de Hadamard,
    la multiplicació per escalar, el producte escalar, i la descomposició d'un vector en
    components paral·lela i normal segons un altre vector

    La prueba unitaria consistirá en comprobar que, dados 
        v1 = Vector([1, 2, 3]) 
        v2 = Vector([4, 5, 6])
    La multiplicación de v1 por 2 es:
        v3 = Vector([2, 4, 6])
    El producto de Hadamard de v1 por v2 es: 
        v4 = Vector([4, 10, 18]).
    La prueba unitaria consistirá en comprobar que el producto escalar de los 
    dos vectores v1 y v2 del apartado anterior es igual a r1 = 32.

    En este caso, las pruebas unitarias consistirán en comprobar que, 
    dados los vectores:
        v12 = Vector([2, 1, 2]) 
        v22 = Vector([0.5, 1, 0.5])
    La componente de v1 paralela a v2 es:
        v32 = Vector([1.0, 2.0, 1.0])
    La componente perpendicular es:
        v42 = Vector([1.0, -1.0, 1.0])

"""
import unittest

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua
    
    def __eq__(self, other):
        """r
        Comprova dos Vectors iguals
        """
        if not isinstance(other, Vector):  # Ensure the other object is also a Vector
            return False
        return self.vector == other.vector

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])
    
    def __mul__(self, other):
        """
        Multiplica un numero con el vector o dos vectores
        self  --> el propi vector
        other --> numero real o vector
        return--> resultat de la multiplicació depenent del valor other
        """
        if isinstance(other,(int,float)):
            return Vector([a * other for a in self.vector])
        elif isinstance(other,Vector):
            return Vector([a * b for a, b in zip(self.vector, other.vector)])
        else:
            return TypeError("Operación denegada")
    
    def __rmul__(self,other):
        """
        Operació Multiplicació en posicions inverses
        return-->operació __mul__
        """
        return self * other
    
    def __matmul__(self, other):
        """
        Producte escalar entre dos vectors.
        self  --> el propi vector
        other --> altre vector
        return--> El producte dels dos
        """
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.vector, other.vector))
        else:
            return TypeError("Operació no suportada")
        
    def __rmatmul__(self,other):
        """
        Operació escalar si els vectors estan en posicions de la operació canviades
        """
        return self @ other
    
    def norma2(self):
        """
        Retorna la norma quadrada del vector.
        self  --> el propi vector
        return --> suma de les arrels quadratiques de les components del vector
        """
        return sum(x * x for x in self.vector)

    def __floordiv__(self, other):
        """
        Component paral·lela del vector  a un altre vector.
        self  --> el propi vector
        other --> altre vector
        return--> compomponts del facto junt amb el vector donat
        """
        if isinstance(other, Vector):
            factor = (self @ other) / other.norma2()
            return factor * other
        else:
            return TypeError("Operació no suportada")
        
    def __rfloordiv__(self, other):
        """
        El mateix que la Component paral·lela
        """
        if isinstance(other, (int, float)):
            return Vector([other // x for x in self.components])
        else:
            return TypeError("Unsupported operation with this type")

    def __mod__(self, other):
        """
        Componente normal (perpendicular) respecte a un altre vector.
        self  --> el propi vector
        other --> altre vector
        return--> compompont normal del propi vector junt amb el vector donat
        """
        return self - (self // other)
    
    def __rmod__(self,other):
        """
        El materix que la component perpenticular, pero amb els arguments canviats
        """
        return other - (other // self)

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
class TestVector(unittest.TestCase):
    """
    unittest: defineix funcions pera testestejar i comparar el resultat de les
    operacions amb les funcions generades gràcies a self.assertEqual()
    """
    def test_scalar_multiplication(self):
        v1 = Vector([1, 2, 3])
        self.assertEqual(v1 * 2, Vector([2, 4, 6]))
        self.assertEqual(2 * v1, Vector([2, 4, 6]))

    def test_hadamard_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 * v2, Vector([4, 10, 18]))

    def test_dot_product(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        self.assertEqual(v1 @ v2, 32)

    def test_parallel_component(self):
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])
        self.assertEqual(v1 // v2, Vector([1.0, 2.0, 1.0]))

    def test_normal_component(self):
        v1 = Vector([2, 1, 2])
        v2 = Vector([0.5, 1, 0.5])
        self.assertEqual(v1 % v2, Vector([1.0, -1.0, 1.0]))

if __name__ == "__main__":
    """
    defineix el nivell de explicació
    """
    unittest.main(verbosity=2)