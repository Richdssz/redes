# 🌐 Repositório de Estudos: Redes de Computadores

Repositório estruturado para consolidação teórica e prática em **Redes de Computadores**, com materiais focados em exames acadêmicos, certificações e fundamentos para atuação em **Cibersegurança (Blue Team / Red Team)**.

---

## 📁 Estrutura de Pastas

```text
redes/
├── estudos_prova_redes/           # 📚 Módulos de estudo intensivo e resoluções
│   ├── 00_PLANO_DE_ESTUDOS.md     # Cronograma de 4 dias e metas diárias
│   ├── 01_calculo_subrede_e_binario.md # Guia de conversão binária e subnetting
│   ├── 02_introducao_e_modelos_osi_tcpip.md # Topologias, modelos OSI e TCP/IP, PDUs
│   ├── 03_camada_de_rede_e_roteamento.md # IPv4, ICMP, roteamento e classes/CIDR
│   ├── 04_camada_de_transporte_tcp_udp.md # TCP vs UDP, 3-way handshake e portas
│   ├── 05_camada_de_aplicacao_protocolos.md # DNS, DHCP (DORA), HTTP/S, SSH, e-mail
│   ├── 06_banco_questoes_abertas_simulado.md # Questões discursivas com gabarito comentado
│   └── 07_cisco_packet_tracer_e_ciberseguranca.md # CLI Cisco, labs e port-security
├── livros_e_referencias/          # 📖 Notas e materiais de apoio bibliográfico
│   ├── kurose_top_down.txt        # Notas baseadas em Kurose & Ross
│   └── tanenbaum_6a.txt           # Notas baseadas em Andrew S. Tanenbaum (6ª Ed.)
├── scripts/                       # ⚙️ Automações e utilitários
│   └── trello_board_creator.py    # Script para criação/sincronização de quadro no Trello
├── FONTES_RECOMENDADAS.md         # 🔗 Livros, ferramentas e referências recomendadas
├── ROADMAP.md                     # 🧭 Roteiro completo de tópicos do básico ao avançado
└── README.md                      # 📌 Documentação principal
```

---

## 🎯 Conteúdos em Destaque

- **Cálculo de Sub-redes e Subnetting:** Método prático de conversão por potências de 2, cálculo de tamanho de bloco (salto), identificação de rede/broadcast e intervalo de hosts válidos.
- **Modelos OSI e TCP/IP:** Encapsulamento de dados, desencapsulamento e unidades de dados de protocolo (PDU: Dados, Segmento, Pacote, Quadro, Bits).
- **Protocolos Fundamentais:** Análise de cabeçalhos IPv4 (TTL, fragmentação), TCP (flags, janelas, controle de fluxo) e UDP, além de DNS, DHCP, HTTP/S e SSH.
- **Laboratórios Práticos:** Introdução a comandos de configuração do Cisco IOS e mecanismos de segurança (port-security, desativação de Telnet e habilitação de SSHv2).

---

## ⚙️ Uso do Script de Integração (Trello)

O script contido na pasta [`scripts/trello_board_creator.py`](./scripts/trello_board_creator.py) utiliza variáveis de ambiente para integração segura via API.

1. Crie um arquivo `.env` na raiz do projeto (este arquivo é ignorado pelo Git):
   ```env
   TRELLO_API_KEY=sua_api_key_aqui
   TRELLO_TOKEN=seu_token_aqui
   ```
2. Execute o script:
   ```bash
   python scripts/trello_board_creator.py
   ```
