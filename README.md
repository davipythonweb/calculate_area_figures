# calculate_area_figures
Calcular areas de Poligonos e Paralelogramos com flask e python

# API Geometria - Documentação da Arquitetura

## Visão Geral

API REST desenvolvida em Flask para cálculo de áreas de figuras geométricas.

O projeto foi estruturado utilizando **Blueprints**, separando responsabilidades em camadas para facilitar manutenção, escalabilidade e reutilização de código.

---

## Arquitetura do Projeto

```text
api_geometria/
│
├── app.py
│
├── routes/
│   ├── __init__.py
│   ├── home.py
│   ├── poligonos.py
│   └── paralelogramos.py
│
├── services/
│   ├── __init__.py
│   └── calculos.py
│
├── utils/
│   ├── __init__.py
│   └── validacoes.py
│
└── requirements.txt
```

---

## Responsabilidade de Cada Camada

### main.py

Ponto de entrada da aplicação.

Responsável por:

* Criar a instância do Flask
* Registrar os Blueprints
* Inicializar o servidor

---

### routes/

Contém os endpoints da API.

Responsável por:

* Receber requisições HTTP
* Ler os dados enviados pelo cliente
* Chamar validações
* Acionar os serviços de cálculo
* Retornar respostas JSON

Arquivos:

* home.py
* poligonos.py
* paralelogramos.py

---

### services/

Contém as regras de negócio.

Responsável por:

* Realizar cálculos matemáticos
* Centralizar a lógica da aplicação
* Evitar código de negócio dentro das rotas

Arquivo:

* calculos.py

---

### utils/

Contém funções auxiliares reutilizáveis.

Responsável por:

* Validar dados recebidos
* Evitar repetição de código
* Fornecer mensagens de erro padronizadas

Arquivo:

* validacoes.py

---

## Fluxo da Requisição

Exemplo:

POST /poligonos/triangulo

### 1. Cliente envia a requisição

```json
{
  "base": 10,
  "altura": 5
}
```

### 2. A rota recebe os dados

Arquivo:

```text
routes/poligonos.py
```

### 3. A validação é executada

Arquivo:

```text
utils/validacoes.py
```

Verifica:

* JSON válido
* Campos obrigatórios
* Valores numéricos
* Valores maiores que zero

### 4. O serviço é chamado

Arquivo:

```text
services/calculos.py
```

Função:

```python
area_triangulo(base, altura)
```

### 5. O resultado é retornado

```json
{
  "figura": "triangulo",
  "base": 10,
  "altura": 5,
  "area": 25.0
}
```

---

## Fluxo Simplificado

```text
Cliente
   │
   ▼
Route (Blueprint)
   │
   ▼
Validação (utils)
   │
   ▼
Serviço (services)
   │
   ▼
Resposta JSON
```

---

## Endpoints Disponíveis

### Home

GET /

Retorna informações da API.

---

### Triângulo

POST /poligonos/triangulo

Campos:

```json
{
  "base": 10,
  "altura": 5
}
```

---

### Trapézio

POST /poligonos/trapezio

Campos:

```json
{
  "base_maior": 10,
  "base_menor": 6,
  "altura": 4
}
```

---

### Retângulo

POST /paralelogramos/retangulo

Campos:

```json
{
  "base": 10,
  "altura": 5
}
```

---

### Losango

POST /paralelogramos/losango

Campos:

```json
{
  "diagonal_maior": 10,
  "diagonal_menor": 5
}
```

---

## Tecnologias Utilizadas

* Python 3
* Flask
* Blueprint (Flask)
* JSON

---

## Benefícios da Estrutura

* Separação de responsabilidades
* Código mais organizado
* Facilidade de manutenção
* Facilidade de testes
* Escalabilidade para novos módulos
* Reutilização de código
* Melhor legibilidade do projeto

- usage:
<!-- 
Exemplo com curl para o triângulo:
bashcurl -X POST http://127.0.0.1:5000/poligonos/triangulo \
  -H "Content-Type: application/json" \
  -d '{"base": 10, "altura": 5}'
  
Resposta esperada:
json{
  "figura": "triangulo",
  "base": 10,
  "altura": 5,
  "area": 25.0
}


Exemplo para o losango:
bashcurl -X POST http://127.0.0.1:5000/paralelogramos/losango \
  -H "Content-Type: application/json" \
  -d '{"diagonal_maior": 8, "diagonal_menor": 4}'

Resposta esperada:
json{
    "area": 16.0,
    "diagonal_maior": 8,
    "diagonal_menor": 4,
    "figura": "losango"
}

-->