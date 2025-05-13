# Algumas Estruturas de Dados do Python

## 1.0 Tuplas
Uma tupla é uma estrutura **ordenada**, **imutável** e **permissiva a duplicatas**. Isso significa que:

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
- Permite valores duplicados.
```python
t = (1, 2, 2)
print(t)             # (1, 2, 2)
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

- **Ordenada**:  a ordem dos elementos importa.
```python
l1 = [1, 2, 3]
l2 = [3, 2, 1]
print(l1 == l2)       # False, porque a ordem eh diferente
```
- **Mutável**: pode ser alterada.
```python
l = [1, 2, 3]
l[0] = 10
print(l)             # [10, 2, 3]
```
- **Permissiva a duplicatas**: Permite valores duplicados.
```python
l = [1, 2, 2, 3, 3]
print(l)             # [1, 2, 2, 3, 3]
```

### 2.1 Operações Básicas

#### 2.1.1 Criação
Listas são criadas utilizando parênteses `[]`. Observe:
```python
l1 = [1, 2, 3]                    # Lista com tres elementos
l2 = []                           # Cria uma lista vazia
l3 = [1, "texto", True, (1, 2)]   # Comporta varios tipos de dados
```
#### 2.1.2 Inserção de elementos
Podemos inserir elementos em uma lista utilizando os métodos `append()` e `insert()`:
```python
l = []                       
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
Podemos apagar elementos em uma lista utilizando os métodos `pop()` e `remove()` ou a função `del()`:
```python
l = [0, 1, 2, 3, 4, 5]
l.pop(5)                       # Remove o elemento da posicao cinco (5) da lista e retorna o elemento dessa posicao
del(l[0])                    # Deleta o elemento a posicao zero (0) da lista
l.remove(2)                  # Remove o elemento 2, ja que esta na lista
l.remove(2)                  # Erro: ValueError: list.remove(x): x not in list
```
### 2.2 Métodos Próprios
#### 2.2.1 Método `clear()`
Podemos esvaziar toda a lista usando o método `clear()`:
```python
l = [1, 2, 3, 4]
lista.clear()           # Esvazia a lista
print(l)                # []
```
#### 2.2.2 Métodos `count()` e `index()`
O método `count()` conta a quantidade de um determinado elemento passado como parçametro:
```python
l = [1, 1, 2, 1, 2]
print(l.count(1))       # 3
```
Já o  método `index()` retorna o índice da primeira ocorrência de um **elemento que está na lista**, caso não esteja, dá erro:
```python
l = [1, 2, 3, 2]
print(t.index(2))     # 1
print(t.index(2, 2))  # 3 (Busca a partir do indice 2)
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
#### 2.2.4 Método `copy()`
Podemos cria uma nova lista com os mesmos elementos da original, **sem alterar a original** usando o método `copy()`:
```python
l1 = [1, 2, 3, 4]
l2 = l1.copy()         # Copia os elementos de l1 para l2
l2.append(5)           # Adiciona o elemento cinco (5) em l2
print(l1)              # [1, 2, 3, 4]
print(l2)              # [1, 2, 3, 4, 5]
```

### 2.3 List Comprehension
É uma forma compacta de criar listas usando uma estrutura de repetição e estrutura de condição, se necessário:
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)                                     # [0, 2, 4, 6, 8]
```
## 3.0 Conjuntos
Um conjunto é uma estrutura de dados:

- **Não Ordenada**:  a ordem dos elementos **não** importa.
```python
s1 = {1, 2, 3}
s2 = (3, 2, 1}
print(s1 == s2)       # True, porque nao importa a ordem
```
- **Mutável**: pode ser alterada, porém, não pode ser acessada por índice.
```python
s = {1, 2, 3}
s[0] = 10            # Erro: TypeError: 'set' object does not support item assignment
```
- **Não Permissiva a duplicatas**: Valores repetidos são automaticamente ignorados.
```python
s = {1, 2, 2, 3, 3}
print(s)             # {1, 2, 3}
```
### 3.1 Operações Básicas

#### 3.1.1 Criação
Conjuntos são criados utilizando a função `set()` ou `{}` contendo elementos. Observe:
```python
s1 = {1, 2, 2, 3, 3, 4}    # Elementos duplicados são descartados
s2 = set()                 # Cria um conjunto vazio
s3 = {}                    # Atencao: {} cria um dicionario, nao um set
print(s1)                  # {1, 2, 3, 4}
```
#### 3.1.2 Inserção de elementos
Podemos inserir elementos em um conjunto utilizando os métodos `add()` e `update()`:
```python
s = {1, 2, 3}
s.add(4)                   # Adiciona o elemento quatro (4) no conjunto
s.update([5, 6])           # Adiciona os elementos cinco e seis [5, 6] no conjunto 
print(s)                   # {1, 2, 3, 4, 5}
```
#### 3.1.3 Apagar elementos
Podemos apagar elementos em um conjunto utilizando os métodos `discard()` e `remove()`:
```python
s = {0, 1, 2, 3, 4, 5}
s.discard(2)                 # Remove o item dois (2) do conjunto, sem erro se nao existir
s.remove(3)                  # Remove o item tres (3) do conjunto, com erro se nao existir
s.remove(2)                  # Erro: KeyError: 2
```
### 3.2 Métodos Próprios
#### 3.2.1 Método `union()`
Podemos unir dois ou mais conjuntos usando o método `union()`:
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)           # Uniao dos conjuntos s1 e s2, podemos usar s1 | s2
print(s3)                   # {1, 2, 3, 4, 5}
```
#### 3.2.2 Método `intersection()`
Podemos pegar os elementos comuns entre dois ou mais conjuntos usando o método `intersection()`:
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)    # Interseccão dos conjuntos s1 e s2, podemos usar s1 & s2
print(s3)                   # {3, 4}
```
#### 3.2.3 Método `difference()`
Podemos calcular a diferença entre dois ou mais conjuntos usando o método `difference()`:
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s3 = s1.difference(s2)      # Diferenca dos conjuntos s1 e s2, podemos usar s1 - s2
print(s3)                   # {1, 2}
```
#### 3.2.4 Método `symmetric_difference()`
Podemos calcular a diferença simétrica entre dois ou mais conjuntos usando o método `symmetric_difference()`:
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)    # Diferenca simetrica dos conjuntos s1 e s2, podemos usar s1 ^ s2
print(s3)                           # {1, 2, 5}
```
#### 3.2.5 Método `issubset()`
Podemos verificar se um conjunto é subconjunto de outro (está conjuto em outro) usando o método `issubset()`:
```python
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2))             # True, pois s1 eh um subconjunto de s2 (está contido), podemos usar s1 <= s2
```
#### 3.2.6 Método `issuperset()`
Podemos verificar se um conjunto é superconjunto de outro (contém o outro conjuto) usando o método `issuperset()`:
```python
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issuperset(s2))             # False, pois s1 nao contem s2, podemos usar s1 >= s2
print(s2.issuperset(s1))             # True, pois s2 contem s1, podemos usar s2 >= s1
```
#### 3.2.7 Método `isdisjoint()`
Podemos verificar se dois conjuntos não têm elementos em comum usando o método `isdisjoint()`:
```python
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))             # True, pois s1 e s2 nao contem elementos em comum
```
## 4.0 Dicionários
Um dicionário é uma estrutura de dados **mutável**, **ordenada** (ou não) e que mapeia pares **chave → valor**.

### 4.1 Operações Básicas
#### 4.1.1 Criação
Dicionários são criados utilizando a função `dict()` ou `{}` contendo pares chave → valor. Observe:
```python
d1 = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72}  # Cria um dicionario com seus pares chave → valor
d2 = dict()                                            # Cria um dicionario vazio, podemos usar também {}              
```
#### 4.1.2 Inserção de chaves
Podemos inserir novas chaves em um dicionário já criado:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72}
d['sexo'] = 'M'                                       # Adiciona uma nova chave em d
print(d)                                              # {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72, 'sexo': 'M'}
```
#### 4.1.3 Alterar elementos
Podemos alterar um valor em um dicionário já criado:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72}
d['nome'] = 'Thiago'                                  # Modifica o valor do campo 'nome' em d
print(d)                                              # {'nome': 'Thiago', 'idade': 20, 'altura': 1.72}
```
#### 4.1.4 Apagar elementos
Podemos apagar elementos em um conjunto utilizando os métodos `pop()` ou a função `del()`:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.pop('altura')                                        # Remove a chave 'altura', com erro se nao existir         
del (d['idade'])                                       # Remove a chave 'altura', com erro se nao existir
print(d)                                               # {'nome': 'Gabriel'}
```
### 4.2 Métodos Próprios
#### 4.2.1 Método `clear()`
Remove todos os pares do dicionário, esvaziando-o:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.clear()                                             # Limpa o dicionario
print(d)                                              # {}
```
#### 4.2.2 Método `get()`
Retorna o valor da chave se ela existir, se não, retorna , retorna `None` (ou o valor padrão fornecido):
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
print(d.get('sexo'))                                   # None
print(d.get('sexo', 0))                                # 0
```
#### 4.2.1 Método `update()`
Modifica um dicionário, adicionando ou atualizando pares chave → valor:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.update(idade = 30, cidade = 'Fortaleza')            # Atualiza 'idade' e adiciona 'cidade'
print(d)                                              # {'nome': 'Gabriel', 'idade': 30, 'altura': 1.72, 'cidade': 'Fortaleza'}
```
#### 4.2.3 Método `keys()`
Retorna um iterável com todas as chaves do dicionário:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.keys()                                               # dict_keys(['nome', 'idade', 'altura'])
```
#### 4.2.4 Método `values()`
Retorna um iterável com todos os valores do dicionário:
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.values()                                              # dict_values(['Gabriel', 20, 1.72])
```
#### 4.2.4 Método `items()`
 Retorna um iterável com tuplas (chave, valor):
```python
d = {'nome': 'Gabriel', 'idade': 20, 'altura': 1.72} 
d.items()                                              # dict_items([('nome', 'Gabriel'), ('idade', 20), ('altura', 1.72)])
```
