# Programação Orientada a Objetos

## 1.0 Classes e Objetos
Uma classe é uma estrutura que organiza dados e funcionalidades, servindo como um "**molde"** para criar novos objetos.

### 1.1 Definição de uma Classe
Para definirmos uma nova classe, usamos a palavra reservada `class`:
```python
class ClassName:
  <statement-1>
  .
  .
  .
  <statement-N>
```
### 1.2 Método construtor de uma Classe
Podemos usar a função construtura `__init__` para inicializarmos os atributos de um objeto assim que o criamos:
```python
class Person:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
```
Observe a presença do parâmetro `self`, ele é uma referência à instância atual da classe.

### 1.3 Métodos de uma Classe
Além de atriburtos, uma classe possui métodos, que podemos definir usando a palavra reservada `def`:
```python
class Person:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def introduce(self):
    print(f"Hello, my name is {self.name}!")
```

### 1.4 Instância de uma classe 
Para criarmos uma instância de uma classe, o que chamamos de objeto, usamos a notação de função:
```python
person1 = Person('Bob', 17)
```
Para acessar os atributos ou métodos de uma classe usamos o operador `.` após o seu nome do objeto criado:
```python
print(person1.name)
person1.introduce()
```
Saída:
```shell
Bob
Hello, my name is Bob!
```

## 2.0 Encapsulamento
Podemos proteger classes contra alterações ou exclusões acidentais, categorizando seus atributos e métodos em:

1. **Públicos** (`+`): Acessível de qualquer lugar, permitindo alterações.
```python
class Tree:
   def __init__(self, height):
       self.height = height
```
Definimos a classe `Tree` e podemos criar uma instância dessa classe:
```python
pine = Tree(10)
print(pine.height) # 10
```
Observe que podemos manipular o valor de altura (`height`), podendo provocar acontecimentos inesperados:
```python
pine.height = -10
print(pine.height) # -10
```
2. **Protegidos** (`#`): Ainda permitindo alterações, sendo acessível dentro do mesmo módulo ou por sub-classes.

Definimos uma atributo ou método como protegido usando o `_`:
```python
class Tree:
   def __init__(self, height):
       self._height = height
```
Porém, o atributo ainda pode ser modificado no contexto abaixo, levando a comportamntos indesejados em certos contextos:
```python
pine = Tree(10)
pine._height = 'sooo big'
print(pine._height) # 'sooo big'
```

3. **Privados** (`-`): Acessível apenas dentro da classe, sendo mais restritivo.

Definimos uma atributo ou método como privado usando o `__` (duplo sublinhado):
```python
class Tree:
   def __init__(self, height):
       self.__height = height
```
Dessa forma, não podemos fazer alterações indevídas nos atributos de uma classe:
```python
pine = Tree(20)
print(pine.__height)
```
Saída:
```shell
AttributeError: 'Tree' object has no attribute '__height'
```
## 3.0 Composição e Agregação

## 4.0 Herança
