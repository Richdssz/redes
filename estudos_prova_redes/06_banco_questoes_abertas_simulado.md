# 🏆 06 - Banco de Questões Discursivas e Simulado Real para Prova

> **Instruções:** Responda as questões abaixo em uma folha de papel ou em um editor de texto separado sem olhar o gabarito. Em seguida, compare com a **Resposta Modelo Esperada**, prestando atenção nos termos técnicos fundamentais exigidos pelos professores.

---

## 📝 BLOCO 1: Cálculo de Sub-rede & Endereçamento (Peso Alto)

### Questão 1 (Cálculo com /25):
Uma filial precisa configurar a rede `172.16.20.0/24`. A gerência solicitou a divisão em **2 sub-redes iguais** (uma para Vendas e outra para Suporte).
- **a)** Qual a nova máscara de sub-rede em notação CIDR e em formato decimal com pontos?
- **b)** Indique o endereço de rede, primeiro host válido, último host válido e broadcast de cada sub-rede.
- **c)** Quantos computadores utilizáveis cada sub-rede suportará?

<details>
<summary>🔍 Ver Resposta Modelo e Justificativa</summary>

- **a) Nova Máscara:**
  - $2^s \ge 2 \implies s = 1$ bit emprestado.
  - CIDR: $/24 + 1 =$ **/25**.
  - Decimal: O 1º bit do 4º octeto vale $128 \implies$ **255.255.255.128**.
- **b) Tabela das 2 Sub-redes:**
  - Salto: $256 - 128 = 128$ (ou $2^7 = 128$).
  - **Sub-rede 1:**
    - Rede: `172.16.20.0`
    - Primeiro Host: `172.16.20.1`
    - Último Host: `172.16.20.126`
    - Broadcast: `172.16.20.127`
  - **Sub-rede 2:**
    - Rede: `172.16.20.128`
    - Primeiro Host: `172.16.20.129`
    - Último Host: `172.16.20.254`
    - Broadcast: `172.16.20.255`
- **c) Hosts utilizáveis:**
  - $2^7 - 2 = 128 - 2 =$ **126 hosts utilizáveis por sub-rede**.
</details>

---

### Questão 2 (Cálculo com /28 e Análise de Pertença):
Uma rede recebeu o endereço `192.168.1.0/24` e foi dividida utilizando a máscara `255.255.255.240`.
- **a)** Qual a notação CIDR dessa máscara?
- **b)** Em quantas sub-redes o bloco original foi dividido?
- **c)** Quantos hosts utilizáveis existem em cada sub-rede?
- **d)** O endereço IP `192.168.1.63` pode ser configurado na placa de rede de um servidor? **Justifique obrigatoriamente.**

<details>
<summary>🔍 Ver Resposta Modelo e Justificativa</summary>

- **a) Notação CIDR:**
  - O valor decimal $240 = 128 + 64 + 32 + 16$ (4 bits ligados).
  - Máscara CIDR: $/24 + 4 =$ **/28**.
- **b) Quantidade de sub-redes:**
  - Foram emprestados 4 bits $\implies 2^4 =$ **16 sub-redes**.
- **c) Hosts utilizáveis por sub-rede:**
  - Sobraram $8 - 4 = 4$ bits para host $\implies 2^4 - 2 = 16 - 2 =$ **14 hosts utilizáveis**.
- **d) Análise do IP `192.168.1.63`:**
  - O salto entre sub-redes é $256 - 240 = 16$.
  - As sub-redes começam em:
    - Sub-rede 1: `192.168.1.0` a `.15` (Broadcast `.15`)
    - Sub-rede 2: `192.168.1.16` a `.31` (Broadcast `.31`)
    - Sub-rede 3: `192.168.1.32` a `.47` (Broadcast `.47`)
    - Sub-rede 4: `192.168.1.48` a `.63` (Broadcast `.63`)
  - **Resposta:** **NÃO pode ser configurado em um servidor.**
  - **Justificativa:** O IP `192.168.1.63` é o **endereço de Broadcast** da 4ª sub-rede (todos os bits da porção de host em nível lógico 1). Endereços de broadcast são reservados para envio de tráfego a todos os dispositivos daquele domínio e não podem ser atribuídos a nenhuma interface de host individual.
</details>

---

## 📝 BLOCO 2: Teoria de Camadas e Protocolos (Discursivas)

### Questão 3 (Modelos e Encapsulamento):
Descreva o que ocorre durante o processo de **encapsulamento** de dados quando um usuário digita `https://google.com` em seu navegador web até a transmissão física pelo cabo de rede. Cite nominalmente a **PDU** gerada em cada camada.

<details>
<summary>🔍 Ver Resposta Modelo e Justificativa</summary>

- **Camada de Aplicação:** O navegador cria a requisição HTTP/HTTPS contendo o método GET. A PDU é chamada de **Dados (ou Mensagem)**.
- **Camada de Transporte:** Os dados são entregues ao protocolo TCP, que anexa um cabeçalho de transporte contendo a porta de origem dinâmica (ex: 54123), a porta de destino (443 - HTTPS) e números de sequência para confiabilidade. A PDU resultante é o **Segmento**.
- **Camada de Rede:** O segmento desce para o IP, que adiciona um cabeçalho de rede com o IP de origem (computador do usuário) e o IP de destino (Google), além do campo TTL. A PDU resultante é o **Pacote**.
- **Camada de Enlace:** O pacote recebe um cabeçalho de enlace contendo o MAC de origem da placa de rede local e o MAC de destino do Gateway (roteador local), além de um trailer FCS no fim para detecção de erros (CRC). A PDU resultante é o **Quadro (Frame)**.
- **Camada Física:** O quadro é modulado e codificado em sinais elétricos ou pulsos ópticos, transmitidos bit a bit pelo cabo como **Bits**.
</details>

---

### Questão 4 (Camada de Transporte - TCP vs UDP):
Por que o serviço de chamadas de voz e streaming ao vivo (VoIP) utiliza predominantemente o protocolo **UDP**, enquanto o download de um software ou transferência bancária exige estritamente o protocolo **TCP**? Explique fundamentando nos mecanismos de cada protocolo.

<details>
<summary>🔍 Ver Resposta Modelo e Justificativa</summary>

- O **TCP** é orientado à conexão e garante entrega confiável com retransmissão de pacotes perdidos e reordenação por números de sequência. Na transferência de um executável ou transação bancária, a corrupção ou perda de um único bit inviabiliza o arquivo ou altera valores financeiros. O atraso gerado por retransmissões é aceitável, mas a integridade é inegociável.
- O **UDP** não é orientado à conexão e não retransmite pacotes perdidos (*Best-Effort*). Em chamadas de voz e streaming ao vivo, a prioridade máxima é o tempo real (baixa latência e baixo jitter). Se um pacote de voz de 10 milissegundos atrás se perder, retransmiti-lo não faz sentido, pois o som já passou e a retransmissão causaria engasgos perceptíveis na conversa. Logo, tolera-se pequena perda em troca de velocidade imediata.
</details>

---

### Questão 5 (Camada de Aplicação - DHCP):
Explique os 4 passos do processo **DORA** executados pelo protocolo DHCP para fornecimento automático de endereços de rede. Por que a primeira mensagem (Discover) precisa obrigatoriamente ser enviada em broadcast?

<details>
<summary>🔍 Ver Resposta Modelo e Justificativa</summary>

1. **Discover:** O cliente recém-conectado envia uma mensagem em broadcast perguntando se há algum servidor DHCP ativo na rede.
2. **Offer:** Um ou mais servidores DHCP respondem oferecendo uma configuração contendo um IP disponível, máscara, gateway e DNS.
3. **Request:** O cliente envia uma mensagem em broadcast aceitando formalmente uma das ofertas recebidas e comunicando a todos os outros servidores que rejeita as demais.
4. **Acknowledge (ACK):** O servidor DHCP escolhido confirma a locação (*lease*) e finaliza a configuração do host.
- **Por que o Discover é em Broadcast?**  
  Porque o cliente no momento em que liga não possui nenhum endereço IP configurado (usa `0.0.0.0`) e desconhece completamente a topologia e o endereço IP do servidor DHCP local. O único modo de alcançar o servidor é enviando um pacote para o endereço de broadcast de camada 3 (`255.255.255.255`) e camada 2 (`FF:FF:FF:FF:FF:FF`).
</details>
