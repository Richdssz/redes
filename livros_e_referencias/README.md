# 📚 Livros e Referências Bibliográficas (Estudo com IA)

Esta pasta contém transcrições e anotações integrais em formato de texto (`.txt`) das duas maiores obras de referência mundial em **Redes de Computadores**.

O objetivo destes arquivos é servir como **base de conhecimento local (Ground Truth)** para estudos aprofundados, consultas rápidas e contextualização direta com modelos de Inteligência Artificial (LLMs).

---

## 📖 O que são estes livros?

### 1. `kurose_top_down.txt`
- **Obra:** *Redes de Computadores e a Internet: Uma Abordagem Top-Down*
- **Autores:** James F. Kurose & Keith W. Ross (6ª Edição)
- **Abordagem Didática:** **Top-Down (De cima para baixo)**.
  - Começa na **Camada de Aplicação** (o que o usuário e desenvolvedor já conhecem no dia a dia: HTTP, DNS, Web, Streaming) e vai descendo camada por camada (Transporte $\to$ Rede $\to$ Enlace $\to$ Física).
- **Para que serve:**
  - Excelente para compreender o funcionamento prático da Internet, programação com Sockets, arquitetura de aplicações distribuídas e como o TCP/IP opera sob o ponto de vista de quem constrói ou consome sistemas.

---

### 2. `tanenbaum_6a.txt`
- **Obra:** *Redes de Computadores*
- **Autores:** Andrew S. Tanenbaum, Nick Feamster & David Wetherall (6ª Edição)
- **Abordagem Didática:** **Bottom-Up (Da base para o topo) & Engenharia de Sistemas**.
  - O livro de cabeceira dos cientistas da computação e engenheiros. Começa na **Camada Física e Enlace** (sinais elétricos, modulação, códigos de correção de erro de Hamming, protocolos de janela deslizante no nível do hardware) e sobe até a aplicação.
- **Para que serve:**
  - Ideal para entender os fundamentos rigorosos de hardware de telecomunicações, telecom, algoritmos matemáticos de roteamento (Dijkstra, Bellman-Ford), criptografia profunda e teoria dos sistemas operacionais de rede.

---

## 🤖 Como Usar Estes Arquivos para Estudar com a IA

Ao estudar com o Antigravity ou qualquer assistente de IA, você pode referenciar trechos ou capítulos diretamente nos seus prompts para obter explicações personalizadas:

### 1. Perguntas de Auditoria Conceitual
> *"Consulte o capítulo sobre TCP no `kurose_top_down.txt` e me explique como funciona a fase de Slow Start com um exemplo numérico."*

### 2. Comparação de Explicações
> *"Como o Tanenbaum explica a diferença entre roteamento por estado de enlace e vetor de distância no `tanenbaum_6a.txt`?"*

### 3. Extração de Exercícios Clássicos
> *"Procure exercícios sobre cálculo de fragmentação IPv4 ou janelas de congestionamento nos livros e me dê uma questão para eu resolver."*

### 4. Criação de Flashcards e Resumos Rápidos
> *"Leia a seção sobre protocolo DNS no Kurose e resuma os tipos de registros em uma tabela Markdown direta ao ponto."*
