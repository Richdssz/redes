# 🧮 01 - Guia Definitivo: Conversão Binária, Subnetting e Exercícios Resolvidos

> **Foco:** Aprender o método visual do "Número Mágico" para nunca mais errar cálculo de sub-rede na prova e responder questões abertas com justificativas perfeitas.

---

## 📌 1. A Tabela Sagrada de Potências de 2 (8 Bits = 1 Octeto)

Um endereço IPv4 possui **32 bits**, divididos em **4 octetos** (4 blocos de 8 bits separados por ponto):
$$\text{Exemplo: } 192.168.10.1 \iff \underbrace{11000000}_{8\text{ bits}}.\underbrace{10101000}_{8\text{ bits}}.\underbrace{00001010}_{8\text{ bits}}.\underbrace{00000001}_{8\text{ bits}}$$

Para qualquer cálculo de sub-rede, você só precisa memorizar esta tabela de 8 posições (da esquerda para a direita):

| Posição do Bit | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Potência** | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| **Valor Decimal** | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| **Soma Acumulada (Máscara)** | **128** | **192** | **224** | **240** | **248** | **252** | **254** | **255** |

### 💡 Macete da Máscara Decimal:
Quando você empresta bits no último octeto, os valores decimais da máscara **sempre** serão um desses:
- 1 bit ligado (`10000000`): **128** (/25)
- 2 bits ligados (`11000000`): $128+64 =$ **192** (/26)
- 3 bits ligados (`11100000`): $128+64+32 =$ **224** (/27)
- 4 bits ligados (`11110000`): $128+64+32+16 =$ **240** (/28)
- 5 bits ligados (`11111000`): $240+8 =$ **248** (/29)
- 6 bits ligados (`11111100`): $248+4 =$ **252** (/30)

---

## 🎯 2. As 3 Regras de Ouro do Subnetting

Quando o exercício pede: *"Divida a rede X em N sub-redes"*:

### Regra 1: Quantos bits emprestar?
$$2^s \ge \text{quantidade de sub-redes desejadas}$$
- Onde $s$ = número de bits roubados da parte de host.
- *Exemplo:* Quer 4 sub-redes? $2^2 = 4 \implies s = 2$ bits.
- *Exemplo:* Quer 8 sub-redes? $2^3 = 8 \implies s = 3$ bits.

### Regra 2: Quantos hosts válidos por sub-rede?
$$N_{\text{hosts}} = 2^h - 2$$
- Onde $h$ = bits que sobraram para host ($h = 32 - \text{nova máscara}$).
- **Por que subtrai 2?**
  - O **primeiro endereço** (tudo zero na parte de host) é o **Endereço da Rede**.
  - O **último endereço** (tudo um na parte de host) é o **Endereço de Broadcast** (envio para todos).

### Regra 3: O Salto (Tamanho do Bloco)
$$\text{Salto} = 256 - \text{último octeto da máscara} \quad \text{ou} \quad \text{Salto} = 2^h$$
- O salto determina onde começa cada sub-rede:
  - Sub-rede 1: começa em $0$
  - Sub-rede 2: começa em $0 + \text{Salto}$
  - Sub-rede 3: começa em $\text{Sub-rede 2} + \text{Salto}$
  - e assim por diante!

---

## 📝 3. Exercício 1 Resolvido Passo a Passo (Sua Atividade)

### Enunciado:
> Uma empresa recebeu o bloco de endereços `192.168.10.0/24` para configurar sua rede interna.
> O setor de TI precisa dividir essa rede em **4 sub-redes iguais**, atendendo a diferentes departamentos.
> Com base nisso, responda:
> 1. Qual será a nova máscara de sub-rede (em notação decimal e CIDR)?
> 2. Liste o endereço de rede e o endereço de broadcast de cada sub-rede.
> 3. Indique o intervalo de endereços de host válidos de cada sub-rede.
> 4. Quantos hosts utilizáveis cada sub-rede terá?

### Resolução Passo a Passo:

**Passo 1: Quantos bits emprestar?**
- Queremos 4 sub-redes.
- $2^s = 4 \implies s = 2$ bits emprestados.

**Passo 2: Nova máscara:**
- Máscara original: `/24` (`255.255.255.0`)
- Nova notação CIDR: $/24 + 2 =$ **/26**
- Nova notação Decimal: Pegamos os 2 primeiros bits do 4º octeto ($128 + 64 = 192$):
  - **255.255.255.192**

**Passo 3: Salto e Quantidade de Hosts:**
- Bits restantes para host: $8 - 2 = 6$ bits ($h = 6$).
- **Salto (Tamanho do Bloco):** $2^6 = 64$ (ou $256 - 192 = 64$).
- **Hosts utilizáveis:** $2^6 - 2 = 64 - 2 =$ **62 hosts utilizáveis por sub-rede**.

**Passo 4: Montagem da Tabela das 4 Sub-redes:**

| Sub-rede | Endereço de Rede | 1º Host Válido | Último Host Válido | Broadcast |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `192.168.10.0` | `192.168.10.1` | `192.168.10.62` | `192.168.10.63` |
| **2** | `192.168.10.64` | `192.168.10.65` | `192.168.10.126` | `192.168.10.127` |
| **3** | `192.168.10.128` | `192.168.10.129` | `192.168.10.190` | `192.168.10.191` |
| **4** | `192.168.10.192` | `192.168.10.193` | `192.168.10.254` | `192.168.10.255` |

---

## 📝 4. Exercício 2 Resolvido Passo a Passo (Sua Atividade)

### Enunciado:
> Você recebeu a rede `192.168.50.0/24` (Classe C).
> O campus precisa de **8 sub-redes de mesmo tamanho** para diferentes laboratórios.
> Responda:
> 1. Qual será a nova máscara para obter 8 sub-redes iguais? (CIDR e decimal)
> 2. Quantos endereços por sub-rede existirão e quantos hosts utilizáveis cada sub-rede terá?
> 3. Liste, para as 8 sub-redes: Endereço de rede, Primeiro host, Último host, Broadcast.
> 4. O IP `192.168.50.173` pertence a qual sub-rede das 8 criadas?
>    a) Identifique o endereço de rede dessa sub-rede.
>    b) Esse IP é um host utilizável? Justifique.
> 5. Se cada sub-rede tiver um roteador com uma interface de gateway (ex.: o primeiro host de cada sub-rede), quantos endereços totais ficarão reservados para gateways no campus?

### Resolução Passo a Passo:

**Item 1: Nova Máscara:**
- Queremos 8 sub-redes: $2^s = 8 \implies s = 3$ bits emprestados.
- **a) Em CIDR:** $/24 + 3 =$ **/27**
- **b) Em Decimal:** Os 3 primeiros bits do 4º octeto valem: $128 + 64 + 32 = 224$.
  - Máscara: **255.255.255.224**

**Item 2: Endereços totais e hosts utilizáveis:**
- Bits restantes para host: $8 - 3 = 5$ bits ($h = 5$).
- **Endereços totais por sub-rede:** $2^5 =$ **32 endereços**.
- **Hosts utilizáveis:** $2^5 - 2 = 32 - 2 =$ **30 hosts utilizáveis**.
- **Salto:** $32$.

**Item 3: Tabela das 8 Sub-redes:**

| # | Endereço de Rede | Primeiro Host Válido | Último Host Válido | Broadcast |
| :-: | :--- | :--- | :--- | :--- |
| **1** | `192.168.50.0` | `192.168.50.1` | `192.168.50.30` | `192.168.50.31` |
| **2** | `192.168.50.32` | `192.168.50.33` | `192.168.50.62` | `192.168.50.63` |
| **3** | `192.168.50.64` | `192.168.50.65` | `192.168.50.94` | `192.168.50.95` |
| **4** | `192.168.50.96` | `192.168.50.97` | `192.168.50.126` | `192.168.50.127` |
| **5** | `192.168.50.128` | `192.168.50.129` | `192.168.50.158` | `192.168.50.159` |
| **6** | `192.168.50.160` | `192.168.50.161` | `192.168.50.190` | `192.168.50.191` |
| **7** | `192.168.50.192` | `192.168.50.193` | `192.168.50.222` | `192.168.50.223` |
| **8** | `192.168.50.224` | `192.168.50.225` | `192.168.50.254` | `192.168.50.255` |

**Item 4: Análise do IP `192.168.50.173`:**
- Localizando o número 173 na tabela acima:
  - Ele cai no intervalo entre `192.168.50.160` e `192.168.50.191` (**Sub-rede 6**).
- **a) Endereço de rede:** **`192.168.50.160`**
- **b) Esse IP é um host utilizável? Justifique:**
  - **Sim.** O intervalo de hosts utilizáveis desta sub-rede vai de `192.168.50.161` até `192.168.50.190`. Como o IP `.173` está dentro dessa faixa e não é nem o endereço de rede (`.160`) nem o de broadcast (`.191`), ele é perfeitamente utilizável por qualquer computador da rede.

**Item 5: Gateways reservados:**
- O campus possui 8 sub-redes. Se cada uma tem 1 interface de gateway do roteador, teremos:
  - **8 endereços IP reservados para gateways** no total (ex.: `.1`, `.33`, `.65`, `.97`, `.129`, `.161`, `.193`, `.225`).

---

## 🏋️ 5. Exercícios de Treino (Tente fazer no papel antes de olhar a resposta!)

### Desafio 1:
Divida a rede `10.0.0.0/24` em **16 sub-redes**.
- Nova máscara CIDR e decimal?
- Quantos hosts por sub-rede?
- Qual o broadcast da 3ª sub-rede?

*(Gabarito: 16 = $2^4 \implies s=4$. Nova máscara = /28 = 255.255.255.240. Salto = $256-240 = 16$. Hosts = $2^4 - 2 = 14$. Sub-rede 1: .0, Sub-rede 2: .16, Sub-rede 3: .32 a .47. Broadcast da 3ª = 10.0.0.47).*
