# 🌐 05 - Camada de Aplicação: Protocolos, Portas, Mecanismos e Segurança

> **Foco para Prova Discursiva:** Funcionamento aprofundado dos protocolos DNS, DHCP, HTTP/HTTPS, SSH, SMTP/IMAP/POP3, suas respectivas portas padrão e vetores de exploração e defesa em segurança.

---

## 📌 1. Tabela Resumo dos Principais Protocolos da Camada de Aplicação

| Protocolo | Nome Completo | Porta Padrão | Protocolo de Transporte | Função Principal |
| :--- | :--- | :---: | :---: | :--- |
| **DNS** | *Domain Name System* | **53** | **UDP** (consultas normais) / **TCP** (zone transfer) | Traduz nomes de domínio legíveis (ex: `google.com`) para endereços IP (`142.250.190.46`). |
| **DHCP** | *Dynamic Host Configuration Protocol* | **67** (Servidor) / **68** (Cliente) | **UDP** | Atribui dinamicamente endereços IP, máscara, gateway e DNS aos hosts. |
| **HTTP** | *HyperText Transfer Protocol* | **80** | **TCP** | Transferência de páginas e dados web em texto puro (inseguro). |
| **HTTPS** | *HTTP Secure (HTTP + TLS/SSL)* | **443** | **TCP** (ou UDP no HTTP/3) | Comunicação web criptografada com confidencialidade e integridade. |
| **SSH** | *Secure Shell* | **22** | **TCP** | Acesso remoto seguro a terminais de comando com criptografia. |
| **FTP** | *File Transfer Protocol* | **20** (Dados) / **21** (Controle) | **TCP** | Transferência de arquivos em texto claro (legado). |
| **SMTP** | *Simple Mail Transfer Protocol* | **25** (Servidores) / **587** (Submissão) | **TCP** | **Envio** de e-mails entre servidores ou de clientes para servidores. |
| **IMAP** | *Internet Message Access Protocol* | **143** (sem SSL) / **993** (SSL) | **TCP** | **Leitura/Sincronização** de e-mails mantendo-os no servidor. |
| **POP3** | *Post Office Protocol v3* | **110** (sem SSL) / **995** (SSL) | **TCP** | **Leitura/Download** de e-mails, baixando para o cliente e removendo do servidor. |

---

## 📌 2. DNS (Domain Name System) em Detalhes

### A Hierarquia do DNS:
O espaço de nomes é uma árvore hierárquica invertida:
1. **Raiz (*Root Servers*):** Representado por um ponto final (`.`). Existem 13 grupos lógicos de root servers no mundo (de A a M).
2. **TLD (*Top-Level Domain*):** Domínios de primeiro nível como `.com`, `.org`, `.gov`, `.br`.
3. **Domínio Autoritativo (*Authoritative DNS*):** Servidores que guardam a resposta oficial para um domínio específico (ex: `meusite.com.br`).

### Tipos de Registros DNS mais cobrados:
- **A:** Mapeia um nome de host para um endereço **IPv4** (ex: `exemplo.com` $\to$ `93.184.216.34`).
- **AAAA:** Mapeia um nome para um endereço **IPv6**.
- **CNAME (*Canonical Name*):** Cria um apelido (*alias*) apontando para outro nome de domínio (ex: `www.exemplo.com` $\to$ `exemplo.com`).
- **MX (*Mail Exchange*):** Aponta para o servidor responsável por receber e-mails daquele domínio.
- **TXT:** Registros de texto livre, amplamente usados para segurança de e-mail (**SPF, DKIM, DMARC**).
- **PTR:** Usado no **DNS Reverso** (mapeia um IP de volta para um nome).

### Consulta Recursiva vs Iterativa:
- **Recursiva:** O cliente pede ao servidor DNS local (ex: roteador ou `8.8.8.8`) que descubra o IP. O servidor local assume o trabalho inteiro e só devolve a resposta final pronta para o cliente.
- **Iterativa:** O servidor responde com uma indicação (*referral*): "Eu não sei a resposta, mas pergunte para este outro servidor DNS da lista".

---

## 📌 3. DHCP: O Processo DORA Passo a Passo

Quando você conecta seu computador ou celular numa rede Wi-Fi, como ele ganha um IP automaticamente? Através das 4 mensagens do processo **DORA**:

```
      CLIENTE                                  SERVIDOR DHCP
         |                                           |
         |  1. DHCP DISCOVER (Broadcast)             |
         | ----------------------------------------> | "Alguém aí pode me dar um IP?"
         |                                           |
         |  2. DHCP OFFER (Unicast ou Broadcast)     |
         | <---------------------------------------- | "Posso te oferecer o IP 192.168.10.15"
         |                                           |
         |  3. DHCP REQUEST (Broadcast)              |
         | ----------------------------------------> | "Eu aceito o IP 192.168.10.15 que você ofereceu!"
         |                                           |
         |  4. DHCP ACK (Acknowledge)                |
         | <---------------------------------------- | "Fechado! Esse IP é seu por 24 horas."
```

- **Por que a mensagem REQUEST é enviada em Broadcast?**
  - Para que todos os outros eventuais servidores DHCP que também mandaram ofertas saibam que o cliente escolheu uma oferta específica e liberem seus respectivos IPs de volta para o pool.

---

## 📌 4. HTTP e HTTPS

### Códigos de Status HTTP Essenciais:
- **2xx (Sucesso):** `200 OK`, `201 Created`.
- **3xx (Redirecionamento):** `301 Moved Permanently`, `302 Found`.
- **4xx (Erro do Cliente):** `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`.
- **5xx (Erro do Servidor):** `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`.

### HTTP/1.1 vs HTTP/2 vs HTTP/3:
- **HTTP/1.1:** Mantém conexões TCP persistentes (*Keep-Alive*), mas sofre de *Head-of-Line Blocking* no nível da aplicação.
- **HTTP/2:** Introduziu **Multiplexação** (várias requisições simultâneas em uma única conexão TCP) e compressão de cabeçalhos (HPACK).
- **HTTP/3:** Abandonou o TCP e migrou para o protocolo **QUIC sobre UDP**, eliminando o atraso de handshake e o *Head-of-Line Blocking* do TCP.

---

## 🛡️ Conexão com Cibersegurança & Pentest

1. **DNS Spoofing / DNS Cache Poisoning:**
   - O atacante insere respostas DNS falsificadas na memória cache de um servidor recursivo. Quando os usuários tentam acessar `banco.com`, são redirecionados silenciosamente para o IP malicioso do atacante.
   - **Defesa:** Implementação do **DNSSEC** (assinaturas digitais criptográficas nos registros).

2. **Rogue DHCP Server & DHCP Starvation:**
   - **DHCP Starvation:** Atacante forja milhares de endereços MAC falsos pedindo IPs ao servidor legítimo até esgotar o pool de endereços.
   - **Rogue DHCP:** O atacante sobe seu próprio servidor DHCP falso na rede. Os novos computadores receberão como Default Gateway e Servidor DNS o IP do atacante, permitindo ataques Man-in-the-Middle (MitM) completos.
   - **Defesa Cisco:** Recurso de switch chamado **DHCP Snooping** (apenas portas confiáveis podem responder com pacotes DHCP Offer/Ack).
