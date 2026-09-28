# 🌐 02 - Fundamentos: Introdução a Redes, Topologias e Modelos OSI vs TCP/IP

> **Foco para Prova Discursiva:** Conceitos de classificação de redes, topologias físicas vs lógicas, comparação detalhada das camadas OSI vs TCP/IP e o processo vital de **Encapsulamento / Desencapsulamento de PDUs**.

---

## 📌 1. Classificação das Redes por Abrangência Geográfica

Em provas abertas, o professor costuma pedir para classificar ou justificar o tipo de rede em um cenário prático:

| Sigla | Nome Completo | Abrangência | Exemplo Real |
| :---: | :--- | :--- | :--- |
| **PAN** | *Personal Area Network* | Poucos metros (~1m a 10m) | Seu fone Sony WH-1000XM3 conectado via Bluetooth ao notebook/celular. |
| **LAN** | *Local Area Network* | Cômodo, prédio, campus | A rede Wi-Fi/Ethernet da sua casa ou o laboratório da faculdade. |
| **MAN** | *Metropolitan Area Network* | Uma cidade ou região metropolitana | Rede de fibra óptica da prefeitura ligando órgãos públicos municipais. |
| **WAN** | *Wide Area Network* | Países, continentes, global | A própria **Internet** ou links submarinos que conectam matriz e filiais em outros estados/países. |
| **WLAN** | *Wireless LAN* | Extensão sem fio da LAN | Rede Wi-Fi doméstica (IEEE 802.11). |

---

## 📌 2. Topologias de Rede (Física vs Lógica)

- **Topologia Física:** Como os cabos e equipamentos estão fisicamente dispostos e conectados.
- **Topologia Lógica:** Como os dados efetivamente trafegam pelo meio.

### As 4 Principais Topologias:

```
    BARRAMENTO                ESTRELA                   ANEL                  MALHA (MESH)
[PC]--[PC]--[PC]           [PC]     [PC]              [PC]-->[PC]              [PC]---[PC]
  |     |     |                \   /                   ^      |                 |  X   |
=================              [SWITCH]                |      v                [PC]---[PC]
 (Cabo Coaxial)                /   \                  [PC]<--[PC]             (Totalmente
                           [PC]     [PC]                                       conectada)
```

1. **Estrela (*Star*) - A mais usada hoje:**
   - Todos os dispositivos conectam-se a um ponto central concentrador (Switch).
   - **Vantagem:** Se um cabo romper, apenas aquele computador para. Fácil de isolar falhas.
   - **Desvantagem:** Ponto único de falha central (*Single Point of Failure*): se o switch central queimar, toda a rede cai.

2. **Barramento (*Bus*) - Legado:**
   - Todos compartilham um único cabo coaxial com terminadores nas pontas.
   - **Problema:** Alto índice de colisões (CSMA/CD) e se o cabo central for cortado, toda a rede para.

3. **Anel (*Ring*) - Token Ring / FDDI:**
   - Cada host se conecta ao próximo em formato de circuito fechado. Um "token" circula dando a vez para quem pode transmitir.
   - **Problema:** Se um nó falhar sem bypass, quebra o circuito.

4. **Malha (*Mesh*) - Redes Críticas / Redes Militares / Backbones:**
   - **Totalmente Conectada (*Full Mesh*):** Cada roteador se conecta diretamente a todos os outros.
   - Fórmula de enlaces: $\frac{n(n-1)}{2}$ links.
   - **Vantagem máxima:** Altíssima redundância e tolerância a falhas (resiliência).
   - **Desvantagem:** Custo altíssimo de cabeamento e portas.

---

## 📌 3. Modelo OSI (7 Camadas) vs Modelo TCP/IP (4 Camadas)

O Modelo OSI é um **modelo conceitual/didático** (criado pela ISO). O Modelo TCP/IP é a **arquitetura prática que roda a Internet**.

```
    MODELO OSI (7 Camadas)                        MODELO TCP/IP (4 Camadas)
+-------------------------------+              +-------------------------------+
|  7. Aplicação                 |              |                               |
|  6. Apresentação              | -----------> |  4. Aplicação                 |
|  5. Sessão                    |              |  (HTTP, DNS, DHCP, SSH, etc.) |
+-------------------------------+              +-------------------------------+
|  4. Transporte                | -----------> |  3. Transporte (TCP, UDP)     |
+-------------------------------+              +-------------------------------+
|  3. Rede                      | -----------> |  2. Internet (IPv4, IPv6, ICMP)|
+-------------------------------+              +-------------------------------+
|  2. Enlace de Dados           | -----------> |  1. Acesso à Rede             |
|  1. Física                    |              |  (Ethernet, Wi-Fi, Cabos)     |
+-------------------------------+              +-------------------------------+
```

### O que faz cada camada do Modelo OSI (Decorar com clareza):
1. **Física (1):** Transmissão de **bits brutos** pelo meio físico (voltagem, conectores RJ-45, luz na fibra, sinais de rádio).
2. **Enlace de Dados (2):** Controle de acesso ao meio físico, detecção de erros e endereçamento físico (**Endereço MAC**). Equipamento: **Switch L2**.
3. **Rede (3):** Roteamento lógico de pacotes entre redes diferentes através de endereçamento lógico (**Endereço IP**). Equipamento: **Roteador**.
4. **Transporte (4):** Comunicação fim-a-fim entre processos/aplicações. Controle de fluxo, confiabilidade e multiplexação através de **Portas** (TCP e UDP).
5. **Sessão (5):** Estabelece, gerencia e finaliza diálogos/sessões entre aplicações cliente e servidor.
6. **Apresentação (6):** Tradução, formatação de dados, compressão e criptografia (ex: SSL/TLS, JSON, ASCII, JPEG).
7. **Aplicação (7):** Interface direta com os programas do usuário (HTTP, DNS, SMTP, FTP, etc.).

---

## 📌 4. O Mecanismo de Encapsulamento, Desencapsulamento e PDUs

> ⚠️ **PERGUNTA CLÁSSICA DE PROVA ABERTA:** *"Explique o que é encapsulamento e descreva a PDU de cada camada."*

### O que é PDU (Protocol Data Unit)?
PDU é a unidade de dados trocada em uma camada específica. Conforme o dado desce as camadas no transmissor, cada camada adiciona seu próprio cabeçalho (*header*) contendo informações de controle:

```
[Aplicação]  ------>  DADOS (Mensagem pura)
                         │
                         ▼ (Adiciona Cabeçalho TCP/UDP com Porta Origem/Destino)
[Transporte] ------>  SEGMENTO (ou Datagrama se for UDP)
                         │
                         ▼ (Adiciona Cabeçalho IP com IP Origem/Destino)
[Rede]       ------>  PACOTE (ou Datagrama IP)
                         │
                         ▼ (Adiciona Cabeçalho MAC Origem/Destino + FCS no final)
[Enlace]     ------>  QUADRO (Frame)
                         │
                         ▼ (Modula em sinais elétricos/ópticos)
[Física]     ------>  BITS (0s e 1s)
```

- **Encapsulamento (Transmissor):** Do topo para a base (Aplicação $\to$ Física). Adiciona cabeçalhos.
- **Desencapsulamento (Receptor):** Da base para o topo (Física $\to$ Aplicação). Remove e processa cada cabeçalho sucessivamente até entregar a mensagem pura à aplicação.

---

## ✍️ Questões Abertas de Fixação (Estilo Prova)

### Q1: Um pacote precisa sair de um PC na rede local e chegar a um servidor na Internet. O switch e o roteador abrem o pacote até qual camada? Justifique.
> **Resposta Modelo para Prova:**  
> O **Switch comum (Camada 2 - Enlace)** só inspeciona o cabeçalho do **Quadro (Frame)** até a Camada 2 para ler o endereço MAC de destino e encaminhar pela porta correta. Ele não altera o cabeçalho IP.  
> O **Roteador (Camada 3 - Rede)** desencapsula o quadro até a Camada 3 para ler o endereço IP de destino contido no **Pacote**, consulta sua tabela de roteamento, recalcula o TTL e reencapsula o pacote em um novo quadro de enlace (com novo MAC) para a próxima interface. Nenhum dos dois toca na camada 4 (Transporte) nem nos Dados de Aplicação.

### Q2: Qual a diferença fundamental entre endereço MAC e endereço IP?
> **Resposta Modelo para Prova:**  
> O **endereço MAC (Camada 2)** é um endereço físico, permanente (gravado na placa de rede/NIC), com 48 bits, usado para comunicação dentro do **mesmo domínio de broadcast / mesmo enlace local**.  
> O **endereço IP (Camada 3)** é um endereço lógico, hierárquico, com 32 bits (IPv4), atribuído dinamicamente ou estaticamente, usado para **roteamento global entre redes distintas**.
