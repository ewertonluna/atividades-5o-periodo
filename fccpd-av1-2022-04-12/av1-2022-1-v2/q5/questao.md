# Questão 5 - 1 pt

Vimos em sala que se não tratarmos corretamente a concorrência, nossas soluções podem apresentar resultados indesejados. Vimos também em sala, um exemplo hipotético de um código capaz de efetuar leituras e escritas em um disco magnético que era baseado em 3 operações: seek - para posicionar a cabeça magnética do disco, read - para efetuar a leitura da posição atual da cabeça magnética e write que recebia como argumento o valor a ser sobrescrito na posição atual da cabeça magnética do disco. O pseudocódigo das operações de leitura e escrita está disponível abaixo:
```python
def disk_read(x):
  seek(x)
  v = read()
  return v

def disk_write(x, v):
  seek(x)
  write(v)
  return
```

Admita que o código acima é um código python. Atualize o código disponível na resposta para que ele utilize a classe Lock do pacote threading do python, de forma a evitar que o acesso concorrente resulte em efeitos indesejados. Lembrem que a classe conta com dois métodos: Lock.acquire e Lock.release.


# Resposta
R:
```python
from threading import Lock
lock = Lock()

def disk_read(x):
  lock.acquire()
  seek(x)
  v = read()
  lock.release()
  return v

def disk_write(x, v):
  lock.acquire()
  seek(x)
  write(v)
  lock.release()
  return
```