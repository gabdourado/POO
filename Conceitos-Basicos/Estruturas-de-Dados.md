# Algumas Estruturas de Dados do Python

## 1.0 Tuplas
Uma tupla é uma estrutura **ordenada** e **imutável**. Isso significa que:

- A ordem dos elementos importa.
```python
t1 = (1, 2, 3)
t2 = (3, 2, 1)
print(t1 == t2)       # False, porque a ordem é diferente
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
t3 = (5,)             # tupla de um único elemento (vírgula é obrigatória)
```
#### 1.1.2 Acesso
Podemos acessar o elemento de uma tupla de forma semelhante a uma lista:
```python
t = (1, 2, 3)
print(t[0])           # 1
print(t[-1])          # 3 (último)
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

#### 1.2.1 Método `count`
O método `count` conta a quantidade de um determinado elemento passado como parçametro:
```python
t = (1, 2, 2, 3, 2)
print(t.count(2))     # 3
```
#### 1.2.2 Método `index`
O método `index` retorna o índice da primeira ocorrência de um **elemento que está na tupla**, caso não esteja, dá erro:
```python
t = (10, 20, 30, 20)
print(t.index(20))     # 1
print(t.index(20, 2))  # 3 (busca a partir do índice 2)
print(t.index(40))     # Erro: ValueError: tuple.index(x): x not in tuple
```
