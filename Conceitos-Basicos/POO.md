# Programação Orientada a Objetos

## 1.0 Classes e Objetos
Uma classe é uma estrutura que organiza dados e funcionalidades, servindo como um "**molde"** para a criação de novos objetos.

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
Além de atributos, uma classe possui métodos, que podemos definir usando a palavra reservada `def`:
```python
class Person:
  def __init__(self, name: str, age: int):
    self.name = name
    self.age = age

  def introduce(self):
    print(f"Hello, my name is {self.name}!")
```

### 1.4 Instância de uma classe 
Para criarmos uma instância de uma classe, o que chamamos de **objeto**, usamos a notação de função:
```python
person1 = Person('Bob', 17)
```
Para acessar os atributos ou métodos de uma classe usamos o operador `.` após o nome do objeto criado:
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

1. **Públicos** (`+`): Acessíveis de qualquer lugar, permitindo alterações.
```python
class Tree:
   def __init__(self, height: float):
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
2. **Protegidos** (`#`): Mais reservados, sendo acessíveis dentro do mesmo módulo ou por sub-classes.

Definimos uma atributo ou método como protegido usando o `_`:
```python
class Tree:
   def __init__(self, height: float):
       self._height = height
```
Porém, o atributo ainda pode ser modificado no contexto abaixo, levando a comportamentos indesejados em certos contextos:
```python
pine = Tree(10)
pine._height = 'sooo big'
print(pine._height) # 'sooo big'
```

3. **Privados** (`-`): Acessíveis apenas dentro da classe, sendo mais restritivos.

Definimos uma atributo ou método como privado usando o `__` (duplo sublinhado):
```python
class Tree:
   def __init__(self, height: float):
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
Vamos agora discutir relações envolvendo classes, tendo um foco em duas: **Composição** e **Agregação**

### 3.1 Composição
Nessa relação, a _parte não existe sem o todo_, ou seja, existe uma relação de morte.
```python
class Account:
  def __init__(self, number: int, balance: float, bound: float):
    self.__number = number
    self.__balance = balance
    self.__bound = bound

  def get_values(self):
    return self.__number, self.__balance, self.__bound

class Client:
  def __init__(self, cpf: str, name: str, address: str, account: Account):
    self.__cpf = cpf
    self.__name = name
    self.__address = address
    self.__account = account
    
  def extrato(self):
    _, balance, bound = self.__account.get_values()
    print("====== EXTRATO ======")
    print(f"Nome: {self.__name}")
    print(f"Saldo: R$ {balance}")
    print(f"Limite: R$ {bound}")
```
A classe `Client` possui uma `Account`, mas não faz sentido a conta existir se o cliente for **deletado**, essa e a relação de morte.
```python
client1 = Client(
    '111-222-333-44', 
    'Gabriel Dourado', 
    'Rua A - nº 0',
    Account(1, 100.0, 700.0) 
    )
```
Vamos usar o método `extrato` de `Client` para acessar os valores de sua conta:
```python
client1.extrato()
```
Saída:
```shell
====== EXTRATO ======
Nome: Gabriel Dourado
Saldo: R$ 100.0
Limite: R$ 700.0
```

### 3.2 Agregação
Já a relação de Agregação, implica que a _parte é compartilhada por outros_, não implica relação de morte.
```python
class Developer:
  def __init__(self, name: str, languages: list, salary: float):
    self.__name = name
    self.__languages = languages
    self.__salary = salary

  def info_dev(self):
    print(f"Nome: {self.__name}")
    print(f"Linguagens: ")
    for language in self.__languages:
      print(f"  {language}")
    print(f"Salário: {self.__salary}")
  
class Team:
  def __init__(self, project: str, developers: list[Developer]):
    self.__project = project
    self.__developers = developers

  def info_team(self):
    print(f"Projeto: {self.__project}")
    for dev in self.__developers:
      print(f"\nDesenvolvedor:")
      dev.info_dev()
```
Note que um desenvolvedor existe independente de estar ou não em um time.
```python
dev1 = Developer('João Victor', ['Python', 'Java'], 1500)
dev2 = Developer('Júlia Silva', ['Java', 'JavaScript'], 1500)

team = Team('Contrução de Sistema de Revervas', [dev1, dev2])
```
Vamos mostrar as informações desse time usando o método `info_team` de `Team`:
```python
team.info_team()
```
Saída:
```shell
Projeto: Contrução de Sistema de Revervas

Desenvolvedor:
Nome: João Victor
Linguagens: 
  Python
  Java
Salário: 1500

Desenvolvedor:
Nome: Júlia Silva
Linguagens: 
  Java
  JavaScript
Salário: 1500
```
## 4.0 Herança
É quando uma classe filha (sub-classe) herda atributos e métodos de uma classe mãe (super-classe). Observe as classes abaixo:
```python
class Employee:
  def __init__(self, name: str, cpf: str, salary: float):
    self.__name = name
    self.__cpf = cpf
    self.__salary = salary

class Manager:
  def __init__(self, name: str, cpf: str, salary: float, monthly_goal: float, bonuses: float):
    self.__name = name
    self.__cpf = cpf
    self.__salary = salary
    self.__monthly_goal = monthly_goal
    self.__bonuses = bonuses
```
Perceba que `Manager` é um tipo de funcionário, porém com mais atribututos. Podemos então fazer o seguinte:
```python
class Employee:
  def __init__(self, name: str, cpf: str, salary: float):
    self.__name = name
    self.__cpf = cpf
    self.__salary = salary

class Manager(Employee):
  def __init__(self, name: str, cpf: str, salary: float, monthly_goal: float, bonuses: float):
    super().__init__(name, cpf, salary)
    self.__monthly_goal = monthly_goal
    self.__bonuses = bonuses
```
Usamos a função `super()` para que a classe filha herde os atributos e métodos da classe mãe.
```python
class Employee:
  def __init__(self, name: str, cpf: str, salary: float):
      self.__name = name
      self.__cpf = cpf
      self.__salary = salary

  def info_employee(self):
    print(f"Nome: {self.__name}")
    print(f"CPF: {self.__cpf}")
    print(f"Salário: {self.__salary}")

class Manager(Employee):
  def __init__(self, name: str, cpf: str, salary: float, monthly_goal: float, bonuses: float):
        super().__init__(name, cpf, salary)
        self.__monthly_goal = monthly_goal
        self.__bonuses = bonuses

  def info_manager(self):
    self.info_employee()
    print(f"Meta mensal: {self.__monthly_goal}")
    print(f"Bônus: {self.__bonuses}")
```
Podemos agora usar os métodos de `Employee` dentro de `Manager`, como pode ser visto acima com o método `info_manager`.

## 5.0 Funções `hasattr()` e `callable()`
São funções que podemos utilizar para analisar atributos e métodos de objetos.

### 5.1 Função `hasattr()`
Podemos usar essa função pora saber se um objeto possui ou não determinando atributo ou método. Seguindo a seguinte sintaxe:
```python
hasattr(object, attribute_name)
```
Antes de usarmos a função, vamos definir a classe `Dog`:
```python
class Dog:
  def __init__(self, name: str, breed: str):
    self.name = name
    self.breed = breed

  def bark(self):
    return "Woof!"
```
Agora, definindo um objeto para testarmos:
```python
my_dog = Dog('Bob', 'Golden Retriever')
```
 Vamos verificar a existência ou não de alguns atributos e métodos do objeto criado:
 ```python
print(hasattr(my_dog, 'name'))
print(hasattr(my_dog, 'age'))
print(hasattr(my_dog, 'bark'))
```
Saída:
```shell
True  # a classe Dog tem atributo 'name'
False # a classe Dog NÃO tem atributo 'age'
True  # a classe Dog tem o atributo (método) 'bark'
```

### 5.2 Função `callable()`
Essa função nos diz se um determinado atributo - que existe - é chamável como uma função. Segue a seguinte sintaxe:
```python
callable(object)
```
Ainda usando a classe `Dog`, vamos analisar se seus atributos são chamáveis (ou seja, se são métodos):
```python
print(callable(my_dog.bark))
print(callable(my_dog.name))
```
Saída:
```shell
True  # 'bark' é um método da Classe Dog
False # 'name' é uma string e não um método da classe Dog
```
