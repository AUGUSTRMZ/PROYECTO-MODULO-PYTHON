"""
es una fila como la del supermercado

usan la metodologia de FIFO First in first out
el primero que llega es el primero que se va

supongamos que tenemos una fila de supermercado con 5 personas
la que se va atender y 4 en espera
si nosotros quisieramos agregar una nueva persona en la fila se agrega al final
tambien si la persona que seguia ya fue atendida todas las demas personas avanzan

"""


from collections import deque
fila_personas = [1, 2, 3, 4]

"""por el momento podemos trabajar con 4 elementos pero como bien el primer oque se va vendria siendo
primero el 1, el 2,3,4 deberian correrse hacia la izquierda y asi sucesivamente, con 4 elementos no pasa nada
pero que pasaria si yo hiciera una lista con 100,000,000 de elementos
"""

fila_personas = list(range(100000000))

"""Aqui el rendimiento empezaria abajar para nuestra computadora o servidor por lo que no seria el metodo mas eficiente
afortunadamente hay una forma mas simple de hacerlo

importamos una libreria o modulo

una libreria o modulo es codigo que ya escribio alguien mas y lo mandas a llamar para hacer las operacione smas faciles
si lo quieren ver asi es como jalar funciones ya creadas por alguien mas que automatizan tareas que hacer desde cero seria complicadas


"""
# deque es una clase, lo veremos mas adelante no se preocupen por eso
fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)

# funcion para hacer pop del elemento a la izquierda
fila.popleft()
print(fila)

if not fila:
    print("fila vacia")
