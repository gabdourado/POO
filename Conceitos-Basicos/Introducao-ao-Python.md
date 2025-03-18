# Conceitos Introdutórios de Python

## 1.0 Sintaxe Básica
### 1.1 Saída de Dados (`print()`)
A função `print()` é usada para exibir informações no terminal.
```python
print("Hello World!")
```

Python oferece várias formas de formatar a saída de dados, observe:
#### 1.1.1 Concatenação simples
Podemos usar o operador `+` para unir strings:
```python
nome = "Felipe"
print("Olá, " + nome + "!")
```

Para concatenarmos strings com números, precisamos converte-lo para string:
```python
nome = "Felipe"
idade = 20
print("Nome: " + nome + "Idade: " + str(idade))
```
#### 1.2.2 Separação por Vírgulas
Podemos usar o caractere `,` para juntar informações:
```python
nome = "Maria"
idade = 19
print("Meu nome é", nome, "e minha idade é", idade)
```

#### 1.1.3 F-Strings (Python 3.6+)
Forma mais moderna e legível de formatação:
```python
nome = "João"
idade = 20
print(f"Meu nome é {nome} e tenho {idade} anos.")
```
### 1. 2 Entrada de Dados (`input()`)

A função `input()` permite que o usuário forneça dados durante a execução do programa e o valor recebido é sempre do tipo **string**.
```python
nome = input("Qual seu nome? ")
print("Bem vindo," + nome + "!")
```

Se precisarmos de um número, devemos converter o valor de entrada:
```python
idade = int(input("Qual a sua idade? "))
altura = float(intput("Qual a sua altura?" ))
print(f"Idade: {idade} e Altura: {altura}")
```

## 2.0 Tipos de Dados e Variáveis

### 2.1 Números
#### 2.1.1 Inteiro
Números inteiros, tanto positivos quanto negativos:
```python
idade = 20
temperatura = -10
```

#### 2.1.2 Float
Números com casas decimais, tanto positivos quanto negativos:
```python
pi = 3.1415
altura = 1.72
```
### 2.2 Strings
São Cadeias de caracteres e podem ser definidas com aspas simples ou duplas:
```python
nome = "Luana"
frase = 'Bom dia, seja bem vindo!'
```
### 2.3 Booleano
Valor que pode ser **True** (verdadeiro) ou **False** (falso):
```python
ligado = True
```
### 2.4 Listas
É uma coleção mutável e ordenada, construida usando colchetes `[]`:
```python
numeros = [1, 2, 3, 4, 5]
nomes = ["Maria", "João", "Thiago", "Pedro"]
```

Podemos modificar listas:
```python
# Adicionando um novo valor usando .append(valor)
numeros.append(6) # [1, 2, 3, 4, 5, 6]

# Removendo um valor específico usando .remove(valor)
numeros.remove(3) # [1, 2, 4, 5, 6]

# Removendo um valor usando .pop(indice)
nomes.pop(1) # ["Maria", "Thiago", "Pedro"]
```

### 2.5 Tuplas
É uma coleção imutável e ordenada, construida usando parênteses `()`:
```python
coordenadas = (10, 20)
```

Tuplas são mais seguras quando queremos garantir que os valores não serão alterados.
### 2.6 Conjuntos
É uma coleção mutável, não ordenada e sem elementos duplicados, construida usando chaves `{}`:
```python
numeros = {1, 2, 3, 3, 4}
print(numeros) # {1, 2, 3, 4}
```

Podemos modificar conjuntos:
```python
# Adicionando um novo valor (caso não esteja no conjunto) usando .add(valor)
numeros.add(5)
print(numeros) # {1, 2, 3, 4, 5}

# Removendo um valor específico usando .remove(valor)
numeros.remove(3)
print(numeros) # {1, 2, 4, 5}

# Removendo um valor usando .discard(valor)
numeros.discard(6) # Não altera pois não tem esse elemento
print(numeros) # {1, 2, 3, 4, 5}
```

### 2.7 Dicionários
Armazenam dados em pares chave-valor, como um "banco de dados" simples.
```python
pessoa = {'nome':'Maria', 'idade':19, 'cidade':'Russas'}
print(pessoa['nome']) # Maria
```

Podemos modificar dicionários:
```python
# Inserindo um novo par chave-valor
pessoa['curso'] = 'EP'
print(pessoa) # {'nome':'Maria', 'idade':19, 'cidade':'Russas', 'curso':'EP'}

# Atualiza um valor existente
pessoa['idade'] = 20
print(pessoa) # {'nome':'Maria', 'idade':20, 'cidade':'Russas', 'curso':'EP'}

# Removendo um elemento usando .pop(chave)
pessoa.pop(cidade)
print(pessoa) # {'nome':'Maria', 'idade':20, 'curso':'EP'}
```

Podemos modificar ou adicionar múltiplos valores ao mesmo tempo:
```python
# Atualizando múltiplos valores usando .update()
pessoa.update({'idade': 20, 'cidade': 'Aracati'})  # Atualiza idade e cidade
print(pesssoa) # {'nome':'Maria', 'idade':20, 'cidade':'Aracati'}
```

Podemos ainda esvaziar e deletar um dicionário:
```python
# Esvaziando dicionário usando .clear()
pessoa.clear()
print(pessoa) # {}

# Deletando dicionário usando del
del pessoa
```
## 3.0 Estruturas Condicionais

### 3.1 Operadores Relacionais e Lógicos

#### 3.1.1 Operadores Relacionais 

Os operadores **relacionais** são usados para comparar valores.

| **Operador** | **Descrição**  | **Exemplo** |    **Resultado**     |
| :----------: | :------------: | :---------: | :------------------: |
|     `>`      |   Maior que    |   `5 > 3`   | Verdadeiro (`true`)  |
|     `<`      |   Menor que    |   `4 > 2`   |   False (`false`)    |
|     `>=`     | Maior ou igual |  `5 >= 5`   | Verdadeiro (`true`)  |
|     `<=`     | Menor ou igual |  `3 <= 2`   |   Falso (`false`)    |
|     `==`     |     Igual      |  `5 == 5`   | Verdadeiro (`false`) |
|     `!=`     |   Diferente    |  `5 != 5`   |   Falso (`false`)    |

#### 3.1.2 Operadores Lógicos 

Os operadores **lógicos** combinam múltiplas condições.

| **Operador** |                           **Descrição**                           |
| :----------: | :---------------------------------------------------------------: |
|    `and`     | E -  Será `True`somente se ambas as condições forem verdadeiras.  |
|     `or`     | OU - Será `True` se ao menos uma das condições forem verdadeiras. |
|    `not`     |           NÃO - Inverte o valor lógico de uma condição            |

### 3.1 Estrutura `if`

O `if` testa uma condição. Se for verdadeira (`True`), executa um bloco de código.
```python
ehNoite = True
if (ehNoite):
	print("É noite!")
```
### 3.2 Estrutura `elif`

O `elif` é usado para verificar **outras condições**.
```python
diaSemana = 4
if diaSemana == 1:
	print("Domingo")
elif idade == 2:
	print("Segunda-feira")
elif idade === 3:
	print("Terça-feira")
# ...
```
### 3.3 Estrutura `else`

O `else` é o **caso padrão**, que executa se nenhuma das condições anteriores for atendida.
```python
idade = 20
if idade < 18:
	print("Você é menor de idade.")
elif idade == 18:
	print("Você tem exatamente 18 anos.")
else:
	print("Você é maior de idade.")
```

### 3.4 Estrutura `match-case`

A partir do Python 3.10, podemos usar `match-case`, similar ao `switch` em outras linguagens.
```python
diaSemana = 4

match opcao:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira)
    # ...
    case _:
        print("Opção inválida.")
```
## 4.0 Estruturas de Repetição

### 4.1 Estrutura `for`

O `for` é usado para **percorrer elementos iteráveis** (listas, tuplas, strings, etc.).
```python
frutas = ["maçã", "banana", "uva", "melancia"]

for fruta in frutas:
	print(fruta)
```

Podemos usar a função `range()` para gerar uma sequência de números:
```python
for i in range(5):
	print(i) # 0, 1, 2, 3, 4 (de 0 até 4)

for i in range(1, 5):
	print(i) # 1, 2, 3, 4 (De 1 até 4)

for i in range(1, 10, 2):
	print(i) # 1, 3, 5, 7, 9 (De 1 até 9 pulando de 2 em 2)
```

E ainda podemos iterar sobre uma string:
```python
palavra = "Python"

for letra in palavra:
	print(letra) # P y t h o n
```
### 4.2 Estrutura `while`

O `while` executa um bloco de código **enquanto uma condição for verdadeira**.
```python
contador = 0
print ("Contagem:")
while contador <= 5:
	print(contador)
	contador += 1

# Saída: 0, 1, 2, 3, 4, 5
```

### 4.3 Comandos `break` e `continue`

Os comandos `break` e `continue` controlam o fluxo do laço.

#### 4.3.1 Comando `break`
O comando `break` interrompe o laço:
```python
for i in range(10):
	if i == 5:
		break # Para o loop quando o i for 5
	print(i)

# Saída: 0, 1, 2, 3, 4
```

#### 4.3.2 Comando `continue`
O comando `continue` pula uma iteração:
```python
for i in range(10):
	if i % 2 == 0:
		continue # Pula todos os pares
	print(i)

# Saída: 1, 3, 5, 7, 9
```
## 5.0 Funções 

As **funções** são blocos de código reutilizáveis que realizam uma **tarefa específica**. Elas ajudam a organizar o código, evitar repetições e tornam a manutenção mais fácil.

### 5.1 Criando funções

Uma função é definida usando a palavra-chave `def`, seguida do nome da função e parênteses `()`.

```python
def saudacao():
	print("Olá! Seja bem vindo!")

# Chamando a função
saudacao()
```

Podemos passar parâmetros e retornar um resultado:
```python
def soma(a, b):
	return a+b

# Chamando a função
resultado = soma(2, 3)
print(resultado)
```

Podemos definir valores padrão para os parâmetros:
```python
def mensagem(texto='Olá!'):
	print(texto())

# Chamando a função
mensagem() # Usa o valor padrão
mensagem('Bem-vindo à Aula de POO!') # Sobrescreve o padrão 
```

Ainda podemos criar funções lambda para facilitar a programação, basta seguir a sintaxe:
```python
nomeDaFuncao = lambda argumentos:expressao
```

Veja alguns exemplos de funções lambda:
```python
# Função em uma linha que calcula o dobro de um número
dobro = lambda var:var*2

# Chamando a função lambda
print(dobro(5))
```
## 6.0 Módulos e Pacotes

Python permite organizar e reutilizar código através de **módulos** e **pacotes**.

### 6.1 Módulos

Um **módulo** é simplesmente um arquivo `.py` que pode ser importado e reutilizado em outros programas.

Por exemplo, vamos criar um módulo chamado de `calculadora.py` com as seguintes funções:
```python
def soma(a, b):
	return a+b;

def sub(a,b):
	return a-b;

def mul(a,b):
	return a*b;

def div(a,b):
	return a/b;
```

Podemos importar e usar esse módulo em outro script Python:
```python
import calculadora as c

resultado = c.soma(2,3)
print(resultado) # Saída: 5
```

Podemos fazer uma importação específica:
```python
from calculadora import mul

resultado = mul(3, 4)
print(resultado) # Saída: 12
```

Ou importar tudo também:
```python
from calculadora import *

resultado = div(6, 2)
print(resultado) # Saída: 3
```

### 6.2 Pacotes
Um **pacote** é uma pasta que contém módulos e um arquivo especial `__init__.py`.

 Por exemplo, podemos criar um diretório chamado `utilidades.py` e dentro desse diretório ter arquivos como `calculadora.py`, `conversor.py` e o arquivo `__init__.py`:
```shell
 utilidades/  
│── __init__.py  
│── calculadora.py  
│── conversor.py  
```

Podemos importar do pacote `utilidades` os módulos `calculadora` e `conversor`:
```python
from utilidades import calculadora as cal

resultado = cal.soma(5,2)

from utilidades import conversor as con

conversao = con.Celcius_to_Fahrenheit(32)
print(conversao)
```
