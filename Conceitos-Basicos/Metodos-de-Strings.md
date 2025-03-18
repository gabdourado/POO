# Métodos de Strings em Python

#### 1. Método `capitalize()`

O método `capitalize()` retorna uma cópia da string com o primeiro caractere em maiúsculo e os demais em minúsculo.
```python
texto = "exEMPLO de STRING"
print(texto.capitalize())
```

Saída:
```python
Exemplo de string
```

#### 2. Método `title()`
 O método `title()` retorna uma cópia da string onde a primeira letra de cada palavra é maiúscula e todas as outras letras são minúsculas.
```python
texto = "exEMPLO de STRING"
print(texto.capitalize())
```

Saída:
```python
Exemplo De String
```
#### 3. Métodos `casefold()` e `lower()`

Os métodos `casefold()` e `lower()` retornam uma cópia da string com todos os caracteres em minúsculo, sendo o método `casefold()` mais "agressivo" que o `lower()`.
```python
texto = "EXEMPLO DE STRING"
print(texto.casefold())
print(texto.lower())
```

Saída:
```python
exemplo de string
exemplo de string
```

#### 4. Método `upper()`

O método `upper()` retorna uma cópia da string com todos os caracteres em maiúsculo.
```python
texto = "exemplo de string"
print(texto.upper())
```

Saída:
```python
EXEMPLO de STRING
```
#### 5. Método `center()`

O método `center()` retorna uma nova string centralizada dentro de um espaço de comprimento especificado, preenchendo com espaços ou um caractere opcional.
```python
texto = "Exemplo de Título"
print(texto.center(32))
print(texto.center(32, '-'))
```

Saída:
```python
				Exemplo de Título
--------------------------------Exemplo de Título--------------------------------		
```
#### 6. Método `count()`

O método `count()` retorna o número de ocorrências de um substring dentro de uma string.
```python
texto = "hoje é um belo dia, porque hoje o sol brilha."
print(texto.count("hoje"))
print(texto.count("hoje",0,18)) # Passando o início e o fim da busca
```

Saída:
```python
2
1
```

#### 7. Método `find()`

O método `find()` retorna a posição da primeira ocorrência de uma substring dentro de uma string, caso não encontre a substring, retorna `-1`.
```python
texto = "hoje é um belo dia, porque hoje o sol brilha."
print(texto.find("dia"))
print(texto.find("sol",0,18)) # Passando o início e o fim da busca
```

Saída:
```python
15
-1
```

#### 8. Método `index()`

O método `index()`, assim como o `find()`, também retorna a posição da primeira ocorrência de uma substring dentro de uma string, porém,caso não encontre a substring, lança uma exceção `ValeuError`  .
```python
texto = "hoje é um belo dia, porque hoje o sol brilha."
print(texto.index("dia"))
print(texto.index("sol",0,18)) # Passando o início e o fim da busca
```

Saída:
```python
15
ValueError
```

#### 9. Método `isdigit()`

O método `isdigit()` verifica se todos os caracteres da string são dígitos numéricos.
```python
texto = "12345"
print(texto.isdigit())

texto2 = "12a45"
print(texto2.isdigit())
```

Saída:
```python
True
False
```

#### 10. Método `isnumeric()`

O método `isnumeric()` verifica se todos os caracteres da string são números.
```python
texto = "12345"
print(texto.isnumeric())

texto2 = "Ⅻ"  # Número romano
print(texto2.isnumeric()) 
```

Saída:
```python
True
True
```

#### 11. Métodos `islower()` e `isupper()`

Os métodos `islower()` e `isupper()` retornam, respectivamente, `True` se todos os caracteres forem minúsculos e `True` se todos os caracteres forem maiúsculos.

```python
texto1 = "EXEMPLO DE STRING MAIÚSCULA"
print(texto.islower())
print(texto.isupper())

texto2 = "exemplo de string minúscula"
print(texto.islower())
print(texto.isupper())
```

Saída:
```python
False
True
True
False
```

#### 12. Método `partition()`

O método `partition()` divide a string em uma tupla de três elementos: parte antes do separador, o separador e parte depois. Caso não encontre o separador, o primeiro elemento da tupla será a string inteira, e os outros dois serão strings vazias.
```python
texto = "Exemplo de String"
print(texto.partition("de"))
print(texto.partition("Python")) # Não está dentro da string
```

Saída:
```python
('Exemplo ', 'de', ' String')
('Exemplo de String', '', '')
```

#### 13. Método `replace()`
O método `replace()` substitui todas as ocorrências de uma substring por outra.
```python
texto = "Exemplo de String"
print(texto.replace("String", "Código"))
```

Saída:
```python
Exemplo de Código
```

#### 14. Método `split()`

O método `split()` divide a string em uma lista de substrings com base no separador.
```python
texto = "Exemplo de String"
print(texto.split(" "))
```

Saída:
```python
['Exemplo', 'de', 'String']
```

#### 15. Método `swapcase()`

O método `swapcase()`troca a capitalização de cada letra, ou seja, maiúscula para minúscula e vice-versa.
```python
texto = "Exemplo de String"
print(texto.swapcase())
```

Saída:
```python
eXEMPLO DE sTRING
```
