# calculate_area_figures
Calcular areas de Poligonos e Paralelogramos com flask e python

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