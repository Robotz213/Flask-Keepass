# Flask-Keepass

Gerencie bancos de dados KeePass em aplicações Flask de forma simples e segura, utilizando PyKeePass como backend.

## Propósito

Este projeto fornece uma extensão Flask para integração com arquivos KeePass, facilitando operações como leitura e busca de entradas diretamente do seu app Flask.

## Instalação

```bash
pip install flask-keepass

# ou

pip install "git+https://github.com/Robotz213/Flask-Keepass.git"

```

## Configuração

Adicione as configurações necessárias no seu app Flask:

```python
app.config["KEEPASS_FILENAME"] = "meu_banco.kdbx"
app.config["KEEPASS_PASSWORD"] = "minha_senha"
# app.config["KEEPASS_KEYFILE"] = "caminho/para/keyfile.key"  # Opcional
# app.config["KEEPASS_TRANSFORMED_KEY"] = "chave_transformada"  # Opcional
# app.config["KEEPASS_DECRYPT"] = True  # Opcional
```

## Uso Básico

```python
from flask import Flask
from flask_keepass import KeepassManager

app = Flask(__name__)
app.config["KEEPASS_FILENAME"] = "meu_banco.kdbx"
app.config["KEEPASS_PASSWORD"] = "senha"

keepass = KeepassManager(app=app)
keepass.init_app(app=app)

# Buscar entradas por título
entradas = keepass.find_entries(title="Exemplo")
for entry in entradas:
    print(entry.username, entry.password)
```

## Principais Recursos

- Inicialização automática via config do Flask
- Busca de entradas por critérios flexíveis
- Integração como extensão Flask
- Baseado em PyKeePass

## API

Consulte a documentação dos módulos para detalhes sobre métodos e parâmetros.

## Contribuição

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue primeiro para discutir o que você gostaria de modificar.

## Licença

Licença [MIT](./LICENSE)
