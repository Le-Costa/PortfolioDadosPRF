# Acidentes nas Rodovias Federais (PRF) — 2024

Análise dos acidentes registrados nas rodovias federais brasileiras em 2024, a partir dos dados abertos da Polícia Rodoviária Federal (PRF). O projeto cobre o ciclo completo: extração dos dados, tratamento com Python, análise descritiva e visualização em Power BI.

📊 **[Acessar o dashboard no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMmYxZjhmODYtM2U3Mi00NTBiLTgxN2YtYTJjYmI3YzhjZmY3IiwidCI6ImFiNmE4ZjI0LTBhNGQtNDljYy1iYzBlLWJmODRkMjEzYjY1OSJ9)**

**Ferramentas:** Python · pandas · Excel · Power BI

> 🌎 **English summary:** Analysis of accidents on Brazilian federal highways in 2024 using open data from the Federal Highway Police (PRF). Data was extracted from public CSV files, cleaned and modeled with Python (pandas), and visualized in a Power BI dashboard. Key findings: December had the highest number of accidents, most occurred between 4 p.m. and 8 p.m., men were the most involved, and women were passengers in more than half of the cases.

---

## 📥 Extração e transformação

Os dados da PRF são disponibilizados em arquivos separados por ano. Trabalhei com o ano de 2024, que tem dois arquivos CSV:

- um com todos os acidentes, sem repetição;
- outro agrupado por pessoa, com várias pessoas para um mesmo acidente.

Escolhi o arquivo agrupado por pessoa, por ter mais informações. O tratamento, feito em Python, incluiu:

- substituição de campos em branco por "Não informado";
- remoção de colunas que não eram relevantes para a análise;
- tratamento de valores irreais, como idades de 1000 anos, substituídas por 999 para serem desconsideradas na análise;
- criação de IDs para os campos com base em tabelas de dimensão criadas por mim.

O código está disponível em [`CodigosProjetoPRF.py`](CodigosProjetoPRF.py).

## 🔎 Análise

Fiz principalmente uma análise descritiva, relacionando:

- tipos de acidente com maior ocorrência;
- quantidade de acidentes por estado;
- gênero e idade das pessoas com maior envolvimento em acidentes;
- tipos de veículo, condições meteorológicas e outras variáveis descritas no documento do projeto.

## 📌 Principais resultados

- **Dezembro** foi o mês com mais acidentes, possivelmente por causa das festividades de fim de ano.
- A maior parte dos acidentes ocorreu **entre 16h e 20h**.
- O gênero **masculino** foi o mais envolvido em acidentes; no gênero feminino, em **mais de 50% dos casos a pessoa era passageira**.

Todas as métricas podem ser exploradas no dashboard e estão descritas no [documento do projeto](Descri%C3%A7%C3%A3o%20do%20projeto.pdf).

## 📂 Dados

- Fonte: [Dados abertos da PRF](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf)
- Os arquivos CSV usados estão disponíveis neste repositório (`acidentes2024.zip`).

> A base da PRF é atualizada mensalmente, então uma nova coleta pode ter uma quantidade de registros diferente da utilizada aqui.
