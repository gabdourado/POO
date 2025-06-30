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



