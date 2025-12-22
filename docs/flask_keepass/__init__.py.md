# Documentação: flask_keepass/**init**.py

## Propósito

Este arquivo implementa a classe `KeepassManager`, responsável por integrar o PyKeePass ao Flask, facilitando o gerenciamento de arquivos KeePass em aplicações Flask. Fornece métodos para inicialização, configuração e busca de entradas no banco de dados KeePass, além de garantir integração como extensão Flask.

## Classes

### KeePassConfig

`TypedDict` que define as configurações necessárias para inicializar o gerenciador KeePass:

- app: Instância do Flask
- filename: Caminho do arquivo KeePass
- password: Senha do banco
- keyfile: Caminho do arquivo de chave (opcional)
- transformed_key: Chave transformada (opcional)
- decrypt: Booleano para descriptografia

### KeepassManager

Classe principal que herda de `PyKeePass` e gerencia a integração com Flask.

#### Principais métodos

```python
def __init__(self, **kwargs: Unpack[KeePassConfig]) -> None:
    """
    Inicialize o gerenciador KeePass com as configurações fornecidas.

    Args:
        **kwargs (KeePassConfig): Configurações para inicialização.
    """
    # ...
```

```python
def load_config(self, kwargs: KeePassConfig) -> KeePassConfig:
    """
    Carregue e normalize as configurações do KeePass a partir do Flask ou kwargs.

    Args:
        kwargs (KeePassConfig): Configurações recebidas.

    Returns:
        KeePassConfig: Configuração normalizada.
    """
    # ...
```

```python
def init_app(self, **kwargs: Unpack[KeePassConfig]) -> None:
    """
    Inicialize a extensão no contexto do Flask.

    Args:
        **kwargs (KeePassConfig): Configurações para inicialização.

    Raises:
        AppRequiredError: Se o app Flask não for fornecido.
    """
    # ...
```

```python
def find_entries(self, **kwargs: Unpack[FindEntriesKwargs]) -> ReturnFindEntries:
    """
    Busque entradas no banco KeePass conforme critérios.

    Args:
        **kwargs (FindEntriesKwargs): Critérios de busca.

    Returns:
        ReturnFindEntries: Lista de entradas encontradas.
    """
    # ...
```

## Exemplo de uso

```python
from flask import Flask
from flask_keepass import KeepassManager

app = Flask(__name__)
app.config["KEEPASS_FILENAME"] = "meu_banco.kdbx"
app.config["KEEPASS_PASSWORD"] = "senha"

keepass = KeepassManager(app=app)
keepass.init_app(app=app)

entradas = keepass.find_entries(title="Exemplo")
```

## Eventos

Não há eventos definidos neste arquivo.
