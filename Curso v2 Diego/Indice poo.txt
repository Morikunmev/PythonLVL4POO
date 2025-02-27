INDICE POO

------------Declaracion de una clase y creacion de objetos------------
n1: crear una clase persona, que tiene como atributo(variable) su nombre y dos metodos(funciones),
uno de dichos metodos iniciliziara el atributo nombre el otro metodo mostrara en la pantalla el
contenido del mismo.

n2: Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota.
Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si esta regular
(nota mayor o igual a 4)

n3: confeccionar una clase que permita cargar el nombre y la edad de una persona.
mostrar los datos cargados. imprimir un mensaje si es mayor de edad (edad>=18)

n4: desarrollar un programa que carge los lados de un triangulo por teclado e implemente los siguientes metodos:
inicializar los atributos, imprimir el valor del lado mayor y otro metodo que
muestre si es equilatero o no. El nombre de la clase llamarla Triangulo


------------Metodo __init__ de la clase------------
n1: crear una clase empleado, atributo: nombre, sueldo. en el metodo init cargar los atributos por
teclado y luego en otro metodo imprimir sus datos y por ultimo uno que imrprima un mensaje
si debe pagar impuesto (si el sueldo supera a 3000)

n2: desarrollar una clase que represente un punto en el plano y tenga los siguientes metodos:
inicializar los valores x e y que llegan como parametros, imprimir en que cuadrante se encuentra dicho punto
(concepto matematico, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc)

n3:desarrollar una clase que represente un cuadrado y tenga los siguientes metodos:
inicializar el valor del lado llegando como parametro al metodo __init__ (definir un atributo llamado lado),
imprimir su perimetro y su superficie

n4: implemente la clase Operaciones. Se deben cargar dos valores enteror por teclado en el metodo __init__.
calcular su suma, resta, multiplicacion y division, cada una en un metodo, imprimir dichos resultados.


------------Llamada de metodos desde otro metodo de la misma clase------------
n1: Plantear una clase Operaciones que solicite en el metodo __init__ la carga de dos enteros y
muestre su suma, resta, multiplicacion y division.
Hacer cada operacion en otro metodo de la clase operacion y llamarlos desde el mismo metodo __init__

n2: Plantear una clase que administre dos listas de 5 nombres y sus notas. Mostrar un menu de opciones que permita:
1.Cargar alumnos
2.listar alumnos
3.Mostrar alumnos con notas mayores o iguales a 7
4. Finalizar el programa

n3: Confeccionar una clase que administre una agenda personal. se debe almacenar el nombre de la persona,
telefono y mail.
debe mostrar un menu con las siguientes opciones:
1. Carga de un contacto en la agenda
2. Listado completo en la agenda
3. Consulta ingresando el nombre de la persona
4. Modificacion de su telefono y mail
5. Finalizar el programa

------------Colaboracion de clases------------
n1: Un banco tiene 3 clientes que pueden hacer depositos y extracciones.
Tambien el banco requiere que al final del dia calcula la cantidad de dinero que hay depositado.
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Cliente y la clase banco

n2: Plantear un programa que permita jugar a los dados. Las reglas de juego son:
se tiran 3 dados si los 3 sales con el mismo valor monstrar un mensaje que "gano", sino "perdio"
Podemos identificar la clase Dado y la clase JuegoDeDados

n3: Plantear una clase club y otra clase Socio.
La clase socio debe tener los siguientes atributos: Nombre y la antiguedad en el club (en años)
en el metodo __ini__ de la clase Socio pedir la carga por teclado del nombre y su antiguedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antiguedad en el club.

------------Herencia------------
n1: [NUEVO]: declaracion de una clase padre, una clase hija, uso de super
n2: [NUEVO]: sin uso de super, declaracion de una clase padre o base llamada "operacion"
y dos subclases "sumar" y "restar", sin uso de super
n3: [NUEVO]: Uso de super con uso de parametros en el constructor base, y uso de super en otros
metodos de la clase hija, ademas de llamadas de metodos dentro de un metodo

------------Variables de clase------------
Uso de variables de clase en general

------------Metodo Especial str------------
[NUEVO]: llamada de str tanto de print como str en el bloque principal
n2 [NUEVO]: Uso del metodo join para concatenar por comas

------------Redefinicion de los operadores matematicos con objetos------------
n1: [NUEVO]: usamos el metodo de operador matematico especial para poo "add", que nos devuelve la suma de
objetos, lo llamamos mendiante el print
n2: [NUEVO]: Combinacion de todos los operadores matematicos en aplicado en poo

------------Redefinicion de los operadores relacionales con objetos------------
n1 [NUEVO]: Uso de todos los operadores relacionales aplicados a poo, los llamamos por medio de funciones
para tener todos los registros guardados
