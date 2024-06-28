# Projeto Flask Básico

Este projeto é um exemplo básico de uma aplicação web usando Flask. Ele demonstra como criar rotas, renderizar templates HTML, processar formulários, utilizar sessões e adicionar estilos CSS.

## Estrutura do Projeto

- **jogoteca.py**: Arquivo principal da aplicação Flask, contendo as rotas e lógica da aplicação.
- **templates/**: Pasta contendo os arquivos HTML usados para renderizar as páginas.
- **static/**: Pasta para armazenar arquivos estáticos como CSS, JavaScript e imagens.

## Funcionalidades Implementadas

1. **Rotas e Renderização de Templates**:
   - `@app.route` define as rotas da aplicação.
   - `render_template` renderiza o conteúdo dos arquivos HTML da pasta `templates`.

2. **Processamento de Formulários**:
   - `request.form['variavel']` é usado para acessar dados enviados via método POST de um formulário HTML.

3. **Uso de Sessões**:
   - `session` é utilizado para armazenar e acessar informações do usuário nos cookies do navegador.

4. **Paradigma de Orientação a Objetos**:
   - Utilização do paradigma OOP para estruturar a lógica da aplicação de forma modular.

5. **Debugger**:
   - Utilização do debugger do Flask para depuração e aceleração do desenvolvimento.

6. **Estilo com CSS**:
   - Arquivos CSS são adicionados na pasta `static` e vinculados aos templates para estilização das páginas.

7. **Herança em HTML**:
   - Uso de herança de templates HTML para evitar duplicação de código e promover a reutilização.

8. **Dinamização de URLs**:
   - Uso da função `url_for` para gerar URLs dinâmicas dentro da aplicação.

## Executando a Aplicação

Para executar a aplicação:

1. Certifique-se de ter Python e Flask instalados.
2. Clone este repositório.
3. Navegue até o diretório do projeto.
4. Execute `python jogoteca.py` para iniciar o servidor Flask.
5. Abra seu navegador e vá para `http://localhost:5000` para ver a aplicação em execução.

