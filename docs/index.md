## Descrição

O Excel Structure Validator é um projeto Python destinado a validar a estrutura de arquivos Excel. Ele compara arquivos Excel recebidos com um modelo pré-definido para assegurar que os dados cumpram com os padrões estabelecidos. 

## Fluxo

```mermaid
flowchart LR 
    A[Folder: Input] <-->|Compara Schema| B(Folder: Modelo)
    B --> C{Validator}
    C -->|Arquivo correto| D[Folder: Output Correto] 
    C -->|Log com detalhes| D[Folder: Output Correto] 
    C -->|Arquivo incorreto| E[Folder: Output Incorreto]
    C -->|Log com detalhes| E[Folder: Output Incorreto] 
```

## Aplicação

O projeto é ideal para cenários onde a qualidade e a consistência dos dados são críticas para análises subsequentes, como importações para o Power BI, análises de dados, entre outros.

Antes de iniciar avalie os arquivos em excel dentro da pasta data/input e data/modelo para entender o comportamento do projeto. Para facilitar, criei arquivos simples com 4 até 6 colunas e poucas linhas, porém o conceito se aplica a qualquer modelo e/ou quantidade de colunas/linhas.

## Tabela modelo

É uma tabela simples, 5 colunas e todas com o dataType do tipo inteiro.

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E |
| -------- | -------- | -------- | -------- | -------- |
| int      | int      | int      | int      | int      |

## Validações

São 6 validações que o nosso projeto está configurado

::: app.validacoes.colunas_estao_presentes_na_mesma_ordem.validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem

::: app.validacoes.colunas_estao_presentes.validar_se_todas_as_colunas_estao_presentes

::: app.validacoes.existem_colunas_a_mais.validar_se_existem_colunas_a_mais

::: app.validacoes.existem_colunas_a_menos.validar_se_existem_colunas_a_menos

::: app.validacoes.quantidade_de_linhas.validar_quantidade_de_linhas

::: app.validacoes.tipos_dados.validar_tipos_dados

Caso qualquer validação seja identificada como invalido, ele marca o arquivo como invalido.
