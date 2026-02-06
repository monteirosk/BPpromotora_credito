# Otimizado Scraper para ScrapeThisSite.com

## Introdução

Identifiquei que o site [ScrapeThisSite.com](https://www.scrapeithissite.com/) usava
JavaScript/AJAX para carregar dados dinâmicos (`?ajax=true&year=2015`), mas mantinha a lista de anos em HTML estático. Em vez de
Selenium (lento e pesado em servidores Linux), usei o Chrome DevTools (Network tab) para capturar o request exato durante interações reais, identificando headers e parâmetros precisos.

## Funcionamento

O scraper otimizado possui separação inteligente de responsabilidades:

### get_years()

BeautifulSoup na página inicial para extrair links estáticos dos anos.

### get_data(year)

Requests HTTP puras replicando o endpoint AJAX com headers autênticos (User-Agent Chrome, Referer correto).

## Resultado

JSON direto sem rendering de browser – 100x mais rápido, zero dependências de GUI/drivers, perfeito para VPS/Docker em produção. Demonstra reverse engineering de APIs + pensamento em escala para ETL/SaaS.


## INSTALAÇÃO

# Para instalar e executar o sistema FastAPI usando o arquivo docker-compose.yml, siga as instruções abaixo:

1. Abra o terminal na pasta raiz do projeto.
2. Execute o comando `docker-compose up --build` para construir e executar os contêineres Docker.
3. Aguarde até que o processo de construção seja concluído e os contêineres estejam em execução.
4. Abra o navegador e acesse `http://localhost:8000/` para visualizar a documentação da API.
5. Experimente as rotas e os recursos fornecidos pela API.

# Lembre-se de que o arquivo docker-compose.yml é responsável por definir a configuração do ambiente Docker e executar os serviços definidos. Certifique-se de que o arquivo esteja na pasta raiz do projeto.
