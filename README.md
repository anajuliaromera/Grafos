# 🔎 Busca em Largura e Menor Caminho em Grafos – Python

Este projeto apresenta a implementação do algoritmo **Busca em Largura (BFS)** e o cálculo do **Menor Caminho** em grafos **não ponderados**, utilizando **lista de adjacência** como estrutura base.

Os códigos foram desenvolvidos em Python, de forma simples, didática e totalmente comentada para facilitar o entendimento.

---

## ⚙️ Algoritmos Implementados

### 1. Busca em Largura (BFS)

Percorre o grafo camada por camada, garantindo que todos os vértices a uma mesma distância sejam explorados antes de avançar para a próxima profundidade.

- ✅ Útil para percorrer grafos por nível  
- ✅ Garante menor caminho **em grafos não ponderados**  
- ❌ Não funciona para grafos com pesos negativos  

---

### 2. Menor Caminho Usando BFS

Utiliza a própria lógica da BFS para encontrar o menor número de arestas entre dois vértices.

- ✅ Funciona apenas para grafos **não ponderados**  
- 🧠 Reconstrói o caminho percorrido usando uma tabela de pais  
- 🔁 Retorna a sequência completa de vértices do caminho mínimo  

---

## 🧪 Funcionalidades do Projeto

O código permite:

- Criar um grafo usando **lista de adjacência**  
- Executar BFS a partir de qualquer vértice  
- Calcular o menor caminho entre dois nós  
- Reconstruir automaticamente o caminho percorrido  
- Demonstrar o funcionamento das funções com exemplos práticos  

---

## 📌 Exemplo de Uso

### Estrutura Básica do Grafo

```python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


## 👥 Integrantes do Projeto

| Nome                              | RA      | Função / Contribuição Principal                      |
|-----------------------------------|---------|------------------------------------------------------|
| **Thauanny da Cruz Oliveira**     | 2002166 | Estrutura do código, testes e documentação           |
| **Ana Júlia Pereira Romera**      | 1986827 | Implementação da matriz de adjacência                |
| **Sophia Mattos**                 | 2001960 | Implementação da lista de adjacência                 |
| **Gabriela Akemi Rejane**         | 2017418 | Revisão e análise comparativa das estruturas         |