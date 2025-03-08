# PortfolioDadosPRF
Este é o meu primeiro projeto de análise de dados, meus foco aqui foi principalmente medir e aplicar meus conheciemntos adquiridos com meus estudos aqui.
Nele trouxe uma análise dos acidentes registrados na base de dados da PRF do ano de 2024. Para essa ánalise usei Python, Pandas, Excel e Power BI. 

Os dados foram extraídos em arquivos CSV disponiveis na base pública da PRF e trasnformados com Excel e Python, a visualização ficou por conta do Power BI.

## Extração e transformação: 
Na base os arquivos são separados por ano, para esse primeiro projeto optei por trabalhar apenas com o ano de 2024, froam extraídos dois arquivos CSV, no primeiro continham todos os acidentes sem repetição. 
No segundo eram agrupados por pessoa, por tanto tinham várias pessoas para um messmo acidente, como esse arquivo continha mais dados optei por trbalhar somente com ele.
Comecei substituindo dados em branco por "Não informado",retirando colunas que não eram pertinentes para análise tratando alguns pontos especificos, como na coluna de idade onde continham registros como 1000, para todos esses irreais, substitui por 999 
para desconsidera-los na análise. 
Atribui ID's para todos os campos presentes na planilha com base em "tabelas" dimensões que eu criei. Esse processo foi feito com Python. 
Os códigos utilizados estarão no arquivo Códigos.

## Análise: 
Depois da trasnformação, fiz principalmente uma análise descritiva, procurando relacionar os tipos de acidentes com maior indice, a quantidade de acidentes por estado, generos e idade das pessoas que possuem maior taxa de envolvimento de aicdnetes, 
tipos de veículo, condições metereológicas e outras presentes no documento de descrição.
### Resultado da Análise: 
Conforme análise obtida podemos identificar alguns indices em relação aos acidentes, por exemplo  o mês em que masi houve acidentes foi em dezembro, possivelmente por conta das festividades do mês, em relação ao horário foi possível identificar que ocorrem marjoriatariamente no período das 16:00 as 20:00.
Outra Boa métrica tirada, é que o o genero mais envolvido em acidentes é o masculino e quanto ao genero feminino em mais de 50% das vezes era como passageiro.
Todas as métricas podem ser analisadas ao visualizar o dashboard, além disso estão descritas no documento do projeto.

##Dados Coletados:

[Base PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)

Importante ressaltar que essa base é atualizada um a vez ao mês, portanto sua coleta pode ter descrepâncias da minha, em relação a quantidade de dados.
Mesu arquivos CSV também estão disponibilizados na pasta de documentos.







