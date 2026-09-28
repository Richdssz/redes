<div align="center">

# 🌐 Redes de Computadores & Cibersegurança

<p align="center">
  <b>Trilha completa de estudos teóricos, práticos e preparatórios para exames universitários e cibersegurança</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Ativo-success?style=for-the-badge&logo=git&logoColor=white" alt="Status" />
  <img src="https://img.shields.io/badge/Foco-Subnetting%20%7C%20OSI%20%7C%20TCP%2FIP-blue?style=for-the-badge&logo=cisco&logoColor=white" alt="Foco" />
  <img src="https://img.shields.io/badge/Prática-Packet%20Tracer-orange?style=for-the-badge&logo=wireshark&logoColor=white" alt="Prática" />
  <img src="https://img.shields.io/badge/Segurança-Blue%20%26%20Red%20Team-red?style=for-the-badge&logo=kalilinux&logoColor=white" alt="Segurança" />
</p>

---

</div>

## 📑 Navegação Rápida pelos Módulos (Índice de Documentações)

Acesse diretamente os roteiros e guias de estudo detalhados:

| 📘 Módulo / Documentação | 🎯 Descrição & Conteúdo Principal | 🔗 Link Direto |
| :--- | :--- | :---: |
| 📅 **00. Plano de Estudos Intensivo** | Cronograma de 4 dias, metas diárias e planejamento para exames. | [`Ver Plano`](./estudos_prova_redes/00_PLANO_DE_ESTUDOS.md) |
| 🧮 **01. Cálculo de Sub-rede & Binário** | Método visual das potências de 2, salto (número mágico), classes e exercícios resolvidos. | [`Acessar Módulo`](./estudos_prova_redes/01_calculo_subrede_e_binario.md) |
| 🏗️ **02. Introdução & Modelos OSI / TCP-IP** | Topologias (Estrela, Barramento, Malha), 7 camadas OSI vs 4 TCP/IP e PDUs. | [`Acessar Módulo`](./estudos_prova_redes/02_introducao_e_modelos_osi_tcpip.md) |
| 🧭 **03. Camada de Rede & Roteamento** | Cabeçalho IPv4, TTL, fragmentação, RFC 1918, ICMP (Ping/Traceroute) e OSPF/BGP. | [`Acessar Módulo`](./estudos_prova_redes/03_camada_de_rede_e_roteamento.md) |
| ⚡ **04. Camada de Transporte (TCP vs UDP)** | Multiplexação por portas, Three-Way Handshake, controle de fluxo e SYN Flood. | [`Acessar Módulo`](./estudos_prova_redes/04_camada_de_transporte_tcp_udp.md) |
| 🌐 **05. Camada de Aplicação & Protocolos** | DNS (recursivo/iterativo), DHCP (processo DORA), HTTP/HTTPS, SSH e E-mail. | [`Acessar Módulo`](./estudos_prova_redes/05_camada_de_aplicacao_protocolos.md) |
| 🏆 **06. Banco de Questões Discursivas** | Simulado com questões abertas idênticas às de provas e gabarito comentado. | [`Treinar Agora`](./estudos_prova_redes/06_banco_questoes_abertas_simulado.md) |
| 🛠️ **07. Cisco Packet Tracer & Segurança** | Comandos Cisco IOS, configuração de sub-redes em roteadores e Port Security. | [`Acessar Lab`](./estudos_prova_redes/07_cisco_packet_tracer_e_ciberseguranca.md) |
| 📚 **Guia dos Livros & Referências** | Como consultar os livros de Kurose & Ross e Tanenbaum usando Inteligência Artificial. | [`Ver Referências`](./livros_e_referencias/README.md) |
| 🗺️ **Roadmap Geral de Aprendizado** | Visão macro de todos os temas do iniciante ao avançado em Redes. | [`Ver Roadmap`](./ROADMAP.md) |

---

## 📂 Arquitetura do Repositório

```text
redes/
├── 📚 estudos_prova_redes/                # Trilha intensiva e materiais de estudo
│   ├── 00_PLANO_DE_ESTUDOS.md            # Cronograma diário
│   ├── 01_calculo_subrede_e_binario.md   # Guia prático de subnetting
│   ├── 02_introducao_e_modelos_osi_tcpip.md # Modelos e encapsulamento
│   ├── 03_camada_de_rede_e_roteamento.md # IPv4, ICMP e roteamento
│   ├── 04_camada_de_transporte_tcp_udp.md # TCP, UDP e Handshake
│   ├── 05_camada_de_aplicacao_protocolos.md # DNS, DHCP, HTTP, SSH
│   ├── 06_banco_questoes_abertas_simulado.md # Questões abertas comentadas
│   └── 07_cisco_packet_tracer_e_ciberseguranca.md # Prática Cisco e defesa
│
├── 📖 livros_e_referencias/               # Base bibliográfica para consulta com IA
│   ├── README.md                         # Guia e contextualização dos livros
│   ├── kurose_top_down.txt               # Kurose & Ross (Abordagem Top-Down)
│   └── tanenbaum_6a.txt                  # Andrew S. Tanenbaum (Engenharia & Hardware)
│
├── 🔗 FONTES_RECOMENDADAS.md              # Indicações de cursos, canais e simuladores
├── 🧭 ROADMAP.md                          # Trilha do básico ao avançado
└── 📌 README.md                           # Visão geral do repositório
```

---

## 💡 Como Estudar com a IA Utilizando Este Repositório

Como este repositório possui uma base de dados estruturada e os livros em texto integral, você pode utilizá-lo abrindo os arquivos lado a lado na IDE ou solicitando interações como:

1. **Explicação de Tópicos Específicos:**
   > *"Abra o arquivo `01_calculo_subrede_e_binario.md` e me dê outro exercício com máscara /27 para eu resolver."*

2. **Consultas Bibliográficas:**
   > *"Pesquise em `livros_e_referencias/kurose_top_down.txt` como funciona a estimativa de RTT no TCP e me explique de forma simples."*

3. **Simulados Interativos:**
   > *"Faça uma pergunta do simulado `06_banco_questoes_abertas_simulado.md` e espere minha resposta para me dar feedback e nota."*
