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
### 2.2 Funções built-in com a função `lambda`
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
São funções utilizadas para gerar **iteradores**. Sendo uma ferramenta poderosa para economia de **espaço** e **tempo**.

#### 2.3.1 Como criar um objeto gerador?
Para criar um objeto gerador, a sintaxe é semelhante a uma _list comprehension_:
```python
(expression for item in iterable)
```
Por exemplo, código abaixo gera um objeto gerador que gera uma sequência de inteiros de `0` até `9`.
```python
generator = (x for x in range(10))

print(next(generator))
print(next(generator))
print(next(generator))
```
Saída:
```python
0
1
2
```
#### 2.3.2 Funções geradoras e `yield`
Podemos criar uma função que "retorna" um gerador, para isso usamos a palavra reservada `yield`.
```python
def generator(size):
  for x in range(size):
    yield x**2
```
A função acima retorna um gerador que produz os quadrados de `0` até `size - 1`.
```python
squares = generator(5)

for value in squares:
  print(value)
```
Saída:
```python
0
1
4
9
16
```
### 2.4 Callback
São funções que recebem outras funções como parâmetros.
```python
def say_hello(name):
  print(f"Hello, {name}!")

def process_name(other_function):
  name = input("What's your name? ")
  other_function(name)
  return name
```
A função `process_name` recebe como parâmetro outra função, vamos passar a função `say_hello`.
```python
name = process_name(say_hello)
```
Entrada:
```python
Gabriel
```
Saída:
```python
Hello, Gabriel!
```
### 2.5 Funções de ordem superior
Funções de ordem superior são estruturas que podem retornar funções e/ou receber funções como parâmetros.
```python
def calculator(op):
  match(op):
    case '+':
      def sum(num1, num2):
        return num1 + num2
      return sum
    case '-':
      def sub(num1, num2):
        return num1 - num2
      return sub
    case '*':
      def mul(num1, num2):
        return num1 * num2
      return mul
    case '/':
      def div(num1, num2):
        return num1 / num2
      return div
```
A função `calculator` recebe uma operação (`+`, `-`, `*` e `/`) e retorna uma função que executa essa operação.
```python
sum = calculator('+')
mul = calculator('*')

print(sum(2, 3))
print(mul(4, 6))
```
Saída:
```python
5
24
```
### 2.6 Decoradores
São funções que recebem outra função como parâmetro e retornam uma nova função mais aprimorada.
```python
def clear_string(string):
  bad_char = ('.', ',', ':', ';', '/', '?', '!', '@')
  for char in string:
    if char in bad_char:
      string = string.replace(char, '')
  return string
```
A função `clear_string` inicialmente limpa uma string de caracteres indesejados.
```python
def format_string(func_string):
  def tratament(string):
    string = func_string(string)
    string = string.upper()
    return string
  return tratament

@format_string
def clear_string(string):
  bad_char = ('.', ',', ':', ';', '/', '?', '!', '@')
  for char in string:
    if char in bad_char:
      string = string.replace(char, '')
  return string
```
Ao usar a função decoradora `format_string`, a função `clear_string` agora também converte cada palavra para maiúscula.

## 3.0 Boas práticas

### 3.1 Doc-strings

### 3.2 Type Hints 









