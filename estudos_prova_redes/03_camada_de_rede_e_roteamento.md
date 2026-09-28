# 🧭 03 - Camada de Rede: Protocolo IPv4, ICMP, Roteamento e Transição para Cibersegurança

> **Foco para Prova Discursiva:** Estrutura do cabeçalho IPv4, campos críticos (TTL, Flags de Fragmentação), classes de IP antigas vs CIDR, faixas de IPs privados da RFC 1918, protocolo ICMP (Ping e Traceroute), roteamento e vetores de ataque/segurança fundamentais.

---

## 📌 1. Anatomia do Cabeçalho IPv4 (Campos Críticos)

O pacote IPv4 possui um cabeçalho padrão de **20 bytes** (sem opções adicionais):

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|     Fragment Offset     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |        Header Checksum        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source IP Address                       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination IP Address                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### 🎯 Campos mais cobrados em prova:
1. **TTL (*Time to Live* - 8 bits):**
   - **O que faz:** Contador que decrementa em **1** a cada roteador (hop) pelo qual o pacote passa.
   - **Por que existe:** Evita que pacotes fiquem girando eternamente em loops de roteamento na Internet. Quando o TTL chega a **0**, o roteador descarta o pacote e envia uma mensagem de erro `ICMP Time Exceeded` de volta para a origem.
   - **Foco em Segurança / Pentest:** É a base do funcionamento do comando `traceroute` e permite fingerprinting de SO (Windows inicia com TTL 128, Linux/Mac com TTL 64, Cisco com 255).

2. **Protocol (8 bits):**
   - Indica qual protocolo da camada superior (Transporte) está encapsulado dentro dos dados do pacote:
     - `1` = **ICMP**
     - `6` = **TCP**
     - `17` = **UDP**

3. **Identification, Flags e Fragment Offset:**
   - Usados quando o pacote precisa ser **fragmentado** porque seu tamanho excede a MTU (*Maximum Transmission Unit*, normalmente 1500 bytes na Ethernet).
   - **Flags:**
     - **DF (*Don't Fragment*):** Se 1, proíbe fragmentar (se for maior que a MTU, o pacote é descartado).
     - **MF (*More Fragments*):** Se 1, avisa ao receptor que mais fragmentos deste pacote estão a caminho.

---

## 📌 2. Classes de IP Antigas vs CIDR

Historicamente (até 1993), os IPs eram divididos rigidamente em Classes pelo primeiro octeto:

| Classe | Primeiro Octeto | Máscara Padrão | Bits Rede / Host | Finalidade Original |
| :---: | :---: | :---: | :---: | :--- |
| **A** | `1.0.0.0` a `126.255.255.255` | `255.0.0.0` (/8) | 8 bits Rede / 24 bits Host | Redes gigantescas (16 milhões de hosts). |
| **B** | `128.0.0.0` a `191.255.255.255` | `255.255.0.0` (/16) | 16 bits Rede / 16 bits Host | Redes médias (65 mil hosts). |
| **C** | `192.0.0.0` a `223.255.255.255` | `255.255.255.0` (/24) | 24 bits Rede / 8 bits Host | Redes pequenas (254 hosts). |
| **D** | `224.0.0.0` a `239.255.255.255` | Não aplicável | - | **Multicast** (transmissão 1 para muitos). |
| **E** | `240.0.0.0` a `255.255.255.255` | Não aplicável | - | Reservada para pesquisas futuras. |

> ⚠️ **Nota Importante:** O IP `127.0.0.1` (faixa `127.0.0.0/8`) é reservado para **Loopback** (sua própria máquina local / localhost).

### Por que o CIDR (*Classless Inter-Domain Routing*) substituiu as classes?
As classes desperdiçavam milhões de endereços (se uma empresa precisasse de 300 computadores, recebia uma classe B inteira com 65 mil IPs!). O **CIDR** permitiu que a máscara de sub-rede tivesse qualquer tamanho arbitrário (ex: `/23`, `/27`, `/29`), desacoplando o endereço de classes rígidas.

---

## 📌 3. Endereços IP Privados (RFC 1918) vs Públicos

Endereços **privados** são reservados exclusivamente para redes internas e **não são roteáveis na Internet pública**:

| Bloco CIDR | Faixa de Endereços | Quantidade de IPs |
| :--- | :--- | :--- |
| **10.0.0.0/8** | `10.0.0.0` a `10.255.255.255` | ~16,7 milhões (Redes corporativas) |
| **172.16.0.0/12** | `172.16.0.0` a `172.31.255.255` | ~1 milhão |
| **192.168.0.0/16** | `192.168.0.0` a `192.168.255.255` | 65.536 (Roteadores domésticos / SOHO) |

### Como redes privadas acessam a Internet?
Através do **NAT (*Network Address Translation*) / PAT (*Port Address Translation*)**:
O roteador substitui o IP de origem privado (ex: `192.168.10.15`) pelo IP público do seu provedor, mapeando cada conexão por portas aleatórias na tabela NAT.

---

## 📌 4. O Protocolo ICMP (Internet Control Message Protocol)

O ICMP opera na Camada 3 e serve para diagnóstico, controle e reporte de erros de transmissão:

1. **Comando `ping`:**
   - Envia um `ICMP Type 8 (Echo Request)`.
   - O destino responde com `ICMP Type 0 (Echo Reply)`.
   - Mede latência (RTT) e perda de pacotes.

2. **Comando `traceroute` (ou `tracert` no Windows):**
   - Envia pacotes com **TTL = 1**. O primeiro roteador descarta e devolve um `ICMP Type 11 (Time-to-live exceeded in transit)`.
   - Envia o próximo com **TTL = 2**, recebendo resposta do segundo roteador.
   - Repete o processo aumentando o TTL até atingir o destino final, mapeando cada salto do caminho.

---

## 📌 5. Roteamento: Estático vs Dinâmico

| Tipo | Funcionamento | Vantagens | Desvantagens |
| :--- | :--- | :--- | :--- |
| **Roteamento Estático** | O administrador digita manualmente cada rota na tabela: `ip route <destino> <máscara> <gateway>`. | Simples, zero overhead de CPU/rede, seguro. | Não se adapta a falhas em links. Péssimo em redes grandes. |
| **Roteamento Dinâmico** | Roteadores conversam entre si usando protocolos para aprender e recalcular rotas automaticamente. | Autocura: se um enlace rompe, recalcula uma rota alternativa em segundos. | Consome processamento de CPU/memória e tráfego de rede. |

### Protocolos de Roteamento Dinâmico Fundamentais:
1. **RIP (*Routing Information Protocol*):** Baseado em vetor de distância (contagem de saltos/hops, máximo 15).
2. **OSPF (*Open Shortest Path First*):** Baseado em estado de enlace (*Link-State*), usa o algoritmo de Dijkstra (SPF), calcula a rota pelo menor custo/largura de banda. Usado dentro de empresas/campi (IGP).
3. **BGP (*Border Gateway Protocol*):** Protocolo de vetor de caminhos que conecta provedores e operadoras do mundo todo. É o protocolo que mantém a Internet global funcionando (EGP).

---

## 🛡️ Conexão com Cibersegurança / Blue Team / Red Team

Para a sua transição para segurança da informação:
- **Ping Sweep (Varredura ICMP):** Atacantes usam pacotes ICMP Echo Request para descobrir hosts ativos na rede (ex: `nmap -sn 192.168.10.0/24`). Muitos firewalls bloqueiam ICMP para dificultar esse reconhecimento.
- **Ataque Smurf / ICMP Flood:** Envio massivo de requisições ICMP com IP de origem forjado (spoofing) para esgotar links e servidores (DoS/DDoS).
- **IP Spoofing:** O atacante forja o campo *Source IP Address* no cabeçalho IP para se passar por uma máquina confiável da rede interna.
