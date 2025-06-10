# Funções em Python
## 1.0 Conceitos de Funções no Geral
Funções são blocos de código reutilizáveis criados para executar uma tarefa específica e bem definida.
```python
def say_hello():
  print("Hello World!")
```
Por exemplo, a função acima mostra `"Hello World!"` na tela, quando chamada.
```python
say_hello()
```
Saída:
```python
Hello World!
```
### 1.1 Criação e chamada de funções
Para criar uma função usa-se a palavra reservada `def`, seguida do nome e seus parâmetros entre parênteses `()`.
```python
def greeting(name):
  print(f"Hello {name}!")
```
Para chamar a função, basta escrever o seu nome e passar os parâmetos necessários para o seu funcionamento.
```python
greeting("Maria")
```
Saída:
```python
Hello Maria!
```
### 1.2 Parâmetros de funções
#### 1.2.1 O que são parâmetros?
Parâmetros são valores que você fornece a uma função para que ela possa realizar sua tarefa.
```python
def sum(num1, num2):
  print(f"A soma é {num1 + num2}")
```
Nesse exemplo, a função precisa de dois números para calcular a soma, assim, `num1` e `num2` são os seus parâmetros.

#### 1.2.2 Parâmetros Padrão (_Default_)
São parâmetros que já vêm com um valor pré-definido no momento em que a função é criada.
```python
def greeting(name = "Friend"):
  print(f"Hello {name}!")
```
Aqui, o parâmetro `name` tem o valor padrão `"Friend"`. Observe o seu comportamento:
```python
greeting()
greeting('João')
```
Saída:
```python
Hello Friend!
Hello João!
```
Sem argumento, a função imprimiu `"Hello Friend!"`. Passado `"João"` como parâmetro, ela imprimiu `"Hello João!"`.
### 1.3 Retorno de funções
#### 1.3.1 Retorno de um único valor
Funções podem devolver um resultado para o lugar onde foram chamadas, basta usar a palavra reservada `return`.
```python
def mul(num1, num2):
  return num1*num2
```
A função acima **retorna** a multiplicação de dois número, `num1` e `num2`.
```python
result = mul(2, 5)
print(result)
```
Saída:
```python
10
```
#### 1.3.2 Retorno de múltiplos valores
Podemos ainda retornar múltiplos resultados usando tuplas.
```python
def min_and_max(_list):
  _min = min(_list)
  _max = max(_list)
  return _min, _max
```
A função acima retorna uma tupla com os valores `_min` e `_max` de uma lista, assim, precisamos desempacotar.
```python
_list = [2, 5, 1, 3, 7, 6, 4]
min_value, max_value = min_and_max(_list)
print(f"Min: {min_value}")
print(f"Max: {max_value}")
```
Saída:
```python
Min: 1
Max: 7
```
### 1.4 Parâmetros especiais
#### 1.4.1 Parâmetros `*args` (argumentos posicionais variáveis)

#### 1.4.1 Parâmetros `**kwargs` (argumentos nomeados variáveis)

## 2.0 Tipos especiais de funções
### 2.1 Funções `lambda`
Funções `lambda` são funções anônimas, criadas seguindo a seguinte sintaxe:
```python
 lambda arguments : expression
```
Uma função `lambda` pode receber um número indefinido argumentos, mas só pode ter uma expressão.
```python
 square_number =  lambda x : x**2
```
Essa função rebece um valor (`x`) e retorna o seu quadrado.
```python
 print(square_number(5))
```
Saída:
```python
25
```
### 2.2 Funções built-in com funções`lambda`
Podemos usar funções `lambda` juntamente com algumas funções embutidas do python.
#### 2.2.1 Função `map`
A função `map` possui a seguinte sintaxe:
```python
map(function, iterable)
```
Ela aplica uma determinada funções em cada elemento de um iterável (`list`, `dict`, `set`, etc).
```python
_list = [2.3, 3.14, 1.5, 0.4, 4.0]
list_int = list(map(int, _list))
print(list_int)
```
Saída:
```python
[2, 3, 1, 0, 4]
```
Assim, podemos definir uma função anônima (`lambda`) e aplicar em um iterável usando `map`.
```python
list_numbers = [2, 3, 1, 5, 7]
list_squares = list(map(lambda x: x**2, list_numbers))
print(list_squares)
```
Saída:
```python
[4, 9, 1, 25, 49]
```
#### 2.2.1 Função `filter`
A função `filter` segue a seguinte sintaxe:
```python
filter(function, iterable)
```
Ela filtra elementos de um iterável com base em uma condição (`True` e `False`).
```python
_list = [3, 2, 1, 0, 4, 5]
list_even = list(filter(lambda x: x % 2 == 0, _list))
print(list_even)
```
Saída:
```python
[2, 0, 4]
```
#### 2.2.1 Função `sorted`
A função `sorted` possui a seguinte sintaxe:
```python
sorted(iterable, key=key, reverse=reverse)
```
Ela ordena um iterável e o parâmetro `key` pode receber uma função como critério de ordenção.
```python
users = {'Amanda': 20, 'Caio': 19, 'Beatriz': 18, 'Davi': 21}
users = dict(sorted(users.items(), key = lambda user: user[1]))
print(users)
```
Saída:
```python
{'Beatriz': 18, 'Caio': 19, 'Amanda': 20, 'Davi': 21}
```
### 2.3 Geradores

### 2.4 Funções de ordem superior

### 2.5 Callback

### 2.6 Modificadores

### 2.7 Funções recursivas

## 3.0 Boas práticas

### 3.1 Doc-strings

### 3.2 Type Hints 









