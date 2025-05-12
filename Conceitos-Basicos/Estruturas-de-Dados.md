# Algumas Estruturas de Dados do Python

## 1.0 Tuplas
Uma tupla é uma estrutura **ordenada** e **imutável**. Isso significa que:

- A ordem dos elementos importa.
```python
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(t1 == t2)       # False, porque a ordem eh diferente
```
- Os valores não podem ser alterados depois de criados.
```python
t = (1, 2, 3)
t[0] = 10             # Erro: 'tuple' object does not support item assignment
```

### 1.1 Operações Básicas

#### 1.1.1 Criação
Tuplas são criadas utilizando parênteses `()`. Observe:
```python
t1 = (1, 2, 3)        # tupla com 3 elementos
t2 = ()               # tupla vazia
t3 = (5,)             # tupla de um unico elemento (vírgula eh obrigatoria)
```
#### 1.1.2 Acesso
Podemos acessar o elemento de uma tupla de forma semelhante a uma lista:
```python
t = (1, 2, 3)
print(t[0])           # 1
print(t[-1])          # 3 (ultimo)
```

#### 1.1.3 Desempacomento (unpacking)
Tuplas podem ser desempacotadas facilmente: 
```python
ponto = (-1, 2)
x, y = ponto
print(x, y)           # -1 2
```
### 1.2 Métodos Próprios
Tuplas têm apenas dois métodos embutidos:

#### 1.2.1 Método `count()`
O método `count()` conta a quantidade de um determinado elemento passado como parçametro:
```python
t = (1, 2, 2, 3, 2)
print(t.count(2))     # 3
```
#### 1.2.2 Método `index()`
O método `index()` retorna o índice da primeira ocorrência de um **elemento que está na tupla**, caso não esteja, dá erro:
```python
t = (10, 20, 30, 20)
print(t.index(20))     # 1
print(t.index(20, 2))  # 3 (busca a partir do indice 2)
print(t.index(40))     # Erro: ValueError: tuple.index(x): x not in tuple
```
## 2.0 Listas
Uma tupla é uma estrutura de dados:

- Ordenada:  a ordem dos elementos importa
```python
l1 = [1, 2, 3]
l2 = [3, 2, 1]
print(l1 == l2)       # False, porque a ordem eh diferente
```
- Mutável: pode ser alterada
```python
l = [1, 2, 3]
l[0] = 10
print(l)             # [10, 2, 3]
```
- Permite valores duplicados
```python
l = [1, 2, 2, 3, 3]
print(l)             # [1, 2, 2, 3, 3]
```

### 2.1 Operações Básicas

#### 2.1.1 Criação
Listas são criadas utilizando parênteses `[]`. Observe:
```python
l1 = [1, 2, 3]                    # Lista com tres elementos
l2 = []                           # lista vazia
l3 = [1, "texto", True, (1, 2)]   # Comporta varios tipos de dados
```
#### 2.1.2 Inserção de elementos
Podemos inserir elementos em uma lista utilizando os métodos `append()` e `insert()`:
```python
l = []                       # Cria uma lista vazia
l.append(1)                  # Insere o elemento no fim da lista
l.append(2)                  # Insere o elemento no fim da lista
l.insert(0, 0)               # Insere o elemento na posicao zero (0)
print(l)                     # [0, 1, 2]
```
#### 2.1.2 Alterar elementos
Podemos alterar o valor de uma lista usando o índice de uma determinada posição:
```python
l = [1, 2, 3, 4]
l[0] = 10                    # Aletar o elemento da posicao zero (0)
print(l)                     # [10, 2, 3, 4]
```
#### 2.1.3 Apagar elementos
Podemos apagar elementos em uma lista utilizando os métodos `pop()`, `remove()` e `del()`:
```python
l = [0, 1, 2, 3, 4, 5]
pop(5)                       # Remove o elemento da posicao cinco (5) da lista e retorna o elemento dessa posicao
del(l[0])                    # Deleta o elemento a posicao zero (0) da lista
l.remove(2)                  # Remove o elemento 2, ja que esta na lista
l.remove(2)                  # Erro: ValueError: list.remove(x): x not in list
```
### 2.2 Métodos Próprios
#### 2.2.1 Método `clear()`
Podemos esvaziar toda a lista usando o método `clear()`:
```python
l = [1, 2, 3, 4]
lista.clear()           # esvazia a lista
print(l)                # []
```

#### 2.2.2 Métodos `index()` e `count()`
O método `count()` conta a quantidade de um determinado elemento passado como parçametro:
```python
t = [1, 1, 2, 1, 2]
print(l.count(1))       # 3
```
Já o  método `index()` retorna o índice da primeira ocorrência de um **elemento que está na lista**, caso não esteja, dá erro:
```python
l = [1, 2, 3, 2]
print(t.index(2))     # 1
print(t.index(2, 2))  # 3 (busca a partir do indice 2)
print(t.index(4))     # Erro: ValueError: 4 is not in list
```
#### 2.2.3 Método `sort()`
Podemos ordenar uma lista usando o método `sort()`:
```python
l = [9, 2, 5, 1]
l.sort()              # Ordena em ordem crescente
print(l)              # [1, 2, 5, 9]

l.sort(reverse=True)  # Ordena em ordem decrescente
print(l)              # [9, 5, 2, 1]
```
### 2.3 List Comprehension
É uma forma compacta de criar listas usando uma estrutura de repetição e estrutura de condição, se necessário:
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)                                     # [0, 2, 4, 6, 8]
```
