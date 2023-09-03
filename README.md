# Excel Structure Validator

## Descrição

O Excel Structure Validator é um projeto Python destinado a validar a estrutura de arquivos Excel. Ele compara arquivos Excel recebidos com um modelo pré-definido para assegurar que os dados cumpram com os padrões estabelecidos. O projeto é ideal para cenários onde a qualidade e a consistência dos dados são críticas para análises subsequentes, como importações para o Power BI, análises de dados, entre outros.

Antes de iniciar avalie os arquivos em excel dentro da pasta data/input e data/modelo para entender o comportamento do projeto. Para facilitar, criei arquivos simples com 4 até 6 colunas e poucas linhas, porém o conceito se aplica a qualquer modelo e/ou quantidade de colunas/linhas.

### Antes de rodar o script

![Antes](./static/pic/antes.png)

### Depois de rodar o script e com o resultado da auditoria

![Depois](./static/pic/depois.png)

## Requisitos

* Python 3.x
* Pandas
* Loguru
* Poetry (opcional)

## Instalação

### Usando pip

1. Clone este repositório
    
2. Navegue até o diretório do projeto e instale as dependências usando pip:
    
    ```bash
    pip install -r requirements.txt
    ```
    

### Usando Poetry (Opcional)

1. Clone este repositório
    
2. Navegue até o diretório do projeto e instale as dependências usando poetry:
    
    ```bash
    poetry install
    ```
    

Para ativar o ambiente virtual do projeto:

```go
```bash
poetry shell
```
```

## Estrutura do Projeto

```lua
ExcelStructureValidator/
|-- app/
|   |-- pipeline.py
|   |-- validacoes/
|   |   |-- __init__.py
|   |   |-- quantidade_de_linhas.py
|   |   |-- existem_colunas_a_mais.py
|   |   |-- ...
|   |-- config.py
|-- data/
|   |-- modelo/
|   |   |-- excel_modelo.xlsx
|   |-- input/
|   |-- output_corretos/
|   |-- output_revisar/
|-- pyproject.toml (se você estiver usando Poetry)
|-- requirements.txt
|-- README.md
```

## Uso

1. Coloque o arquivo modelo Excel em `data/modelo/`
    
2. Coloque os arquivos Excel que você deseja validar em `data/input/`
    
3. Execute o script `pipeline.py` para iniciar o processo de validação:
    
    ```bash
    python app/pipeline.py
    ```
    
4. Verifique os logs e os arquivos Excel movidos para os diretórios `output_corretos` ou `output_revisar`.
    

## Funcionalidades

* Valida a quantidade de linhas
* Verifica a existência de colunas a mais ou a menos
* Compara a ordem das colunas com o arquivo modelo
* Valida os tipos de dados das colunas

## Logs

Os logs são gerados para cada arquivo e são armazenados no mesmo diretório de destino dos arquivos Excel (`output_corretos` ou `output_revisar`), dependendo do resultado da validação.

## Contato

Sinta-se à vontade para entrar em contato comigo se você tiver alguma dúvida ou sugestão sobre o projeto.
email: lvgalvaofilho@gmail.com