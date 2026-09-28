# 🚀 04 - Camada de Transporte: TCP vs UDP, Handshake, Portas e Segurança

> **Foco para Prova Discursiva:** Multiplexação/Demultiplexação por portas, comparação detalhada TCP vs UDP, funcionamento passo a passo do Three-Way Handshake, encerramento de conexão (FIN/RST), controle de fluxo (Janela Deslizante) e ataques clássicos de Camada 4 (SYN Flood, Port Scanning).

---

## 📌 1. A Função Central: Comunicação Fim-a-Fim e Sockets

Enquanto a Camada de Rede (IP) entrega o pacote **entre computadores (Host-to-Host)**, a Camada de Transporte é responsável por entregar a mensagem **entre aplicações/processos específicos (Process-to-Process)** rodando dentro desses computadores.

### O que é um Socket?
$$\text{Socket} = \text{Endereço IP} : \text{Número da Porta}$$
*Exemplo:* `192.168.10.15:52341` conectando a `142.250.190.46:443` (Servidor Google HTTPS).

### Categorias de Portas (0 a 65535):
- **Portas Conhecidas / Well-Known (0 a 1023):** Reservadas para serviços de sistema padrão (HTTP 80, HTTPS 443, DNS 53, SSH 22). Exigem privilégios administrativos.
- **Portas Registradas (1024 a 49151):** Usadas por aplicações específicas de mercado (ex: MySQL 3306, PostgreSQL 5432, RDP 3389).
- **Portas Efêmeras / Dinâmicas (49152 a 65535):** Escolhidas aleatoriamente pelo sistema operacional do cliente para abrir conexões de saída temporárias.

---

## 📌 2. O Grande Duelo: TCP vs UDP (Tabela Comparativa para Prova)

> ⚠️ **QUESTÃO CLÁSSICA:** *"Compare TCP e UDP indicando características, overhead e cenários de uso recomendados para cada um."*

| Característica | TCP (*Transmission Control Protocol*) | UDP (*User Datagram Protocol*) |
| :--- | :--- | :--- |
| **Orientação** | **Orientado à Conexão** (estabelece sessão antes de enviar dados) | **Não orientado à Conexão** (envia direto sem aviso) |
| **Confiabilidade** | **Alta**: Garante entrega, retransmite pacotes perdidos e reordena | **Nenhuma**: Melhor esforço (*Best-Effort*). Não garante entrega |
| **Ordem dos dados** | Garante entrega na ordem exata (usa Sequence Numbers) | Não garante ordem. Pacotes podem chegar invertidos |
| **Controle de Fluxo e Congestionamento** | **Sim** (Janela Deslizante, Slow Start, Congestion Avoidance) | **Não**. Não ajusta a taxa de envio |
| **Tamanho do Cabeçalho (Overhead)** | **20 a 60 bytes** (pesado) | **Apenas 8 bytes** (leve e ultrarrápido) |
| **Velocidade / Latência** | Mais lento devido ao handshake e confirmações (ACK) | Quase instantâneo (latência mínima) |
| **Casos de Uso Típicos** | Navegação Web (HTTP/HTTPS), E-mail (SMTP/IMAP), Arquivos (FTP), SSH | Jogos online (FPS/MOBA), Streaming ao vivo, VoIP, chamadas de vídeo, DNS, DHCP |

---

## 📌 3. O Three-Way Handshake do TCP (Aperto de Mão de 3 Vias)

Antes de transmitir qualquer byte de dados no TCP, o cliente e o servidor sincronizam seus números de sequência:

```
    CLIENTE                                      SERVIDOR
       |                                             |
       |  1. SYN (seq = x)                           |
       | ------------------------------------------> |  (Cliente quer conectar)
       |                                             |
       |  2. SYN-ACK (seq = y, ack = x + 1)          |
       | <------------------------------------------ |  (Servidor aceita e sincroniza)
       |                                             |
       |  3. ACK (ack = y + 1)                       |
       | ------------------------------------------> |  (Conexão estabelecida!)
       |                                             |
       | ======= TRANSFERÊNCIA DE DADOS ============ |
```

### Explicação Passo a Passo:
1. **Passo 1 (SYN):** O cliente envia um pacote com a flag `SYN` ativada e escolhe um número de sequência inicial aleatório ($seq = x$).
2. **Passo 2 (SYN-ACK):** O servidor responde com as flags `SYN` e `ACK` ativadas. Ele confirma o número do cliente ($ack = x + 1$) e define seu próprio número de sequência inicial ($seq = y$).
3. **Passo 3 (ACK):** O cliente confirma o recebimento do SYN do servidor enviando um pacote com a flag `ACK` ($ack = y + 1$). A partir deste instante, a conexão está no estado `ESTABLISHED`.

### Encerramento de Conexão:
- **Normal (4-Way Handshake):** Envio mútuo de flags `FIN` (*Finish*) e confirmações com `ACK`.
- **Abrupto (RST):** Envio da flag `RST` (*Reset*) caso uma porta esteja fechada ou ocorra uma anomalia severa.

---

## 📌 4. Mecanismos de Controle do TCP

1. **Controle de Fluxo (Janela Deslizante / *Sliding Window*):**
   - Evita que um emissor rápido **afogue a memória de um receptor lento**.
   - O receptor avisa no campo *Window Size* do cabeçalho TCP quantos bytes seu buffer de memória ainda aguenta receber (`rwnd`).

2. **Controle de Congestionamento:**
   - Evita que muitos emissores **congestionem os enlaces da Internet** (roteadores intermediários).
   - Usa algoritmos como:
     - **Slow Start:** Começa devagar (enviando 1 MSS) e dobra exponencialmente a cada RTT.
     - **Congestion Avoidance:** Ao atingir um teto (*ssthresh*), passa a crescer linearmente. Ao detectar perda de pacote, reduz a janela drasticamente.

---

## 🛡️ Conexão com Cibersegurança & Pentest

1. **Ataque SYN Flood (Negação de Serviço - DoS):**
   - O atacante envia milhares de pacotes `SYN` com IPs de origem forjados (spoofados).
   - O servidor reserva memória para a conexão e responde `SYN-ACK`, mas nunca recebe o terceiro passo (`ACK`).
   - O servidor esgota sua tabela de conexões pendentes (*backlog queue*) e para de atender clientes legítimos.
   - **Mitigação Blue Team:** Ativar *SYN Cookies* no kernel do servidor ou regras de Rate-Limiting no firewall.

2. **TCP Port Scanning (Nmap):**
   - **TCP Connect Scan (`-sT`):** Completa o 3-Way Handshake inteiro. É fácil de detectar nos logs do servidor.
   - **SYN Stealth Scan (`-sS`):** Envia o `SYN`. Se o servidor responder `SYN-ACK`, a porta está **ABERTA**. O Nmap imediatamente manda um `RST` em vez do último `ACK`. A conexão nunca é concluída, não gerando log na maioria das aplicações antigas.
