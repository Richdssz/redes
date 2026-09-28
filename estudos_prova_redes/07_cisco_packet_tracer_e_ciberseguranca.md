# 🛠️ 07 - Prática Cisco Packet Tracer: Do Básico ao Laboratório de Cibersegurança

> **Foco:** Entender a interface e o funcionamento do Cisco Packet Tracer, comandos fundamentais do Cisco IOS (Switch e Roteador), configuração de sub-redes na prática e introdução a conceitos essenciais de segurança para quem quer trilhar caminho em Blue Team / Red Team.

---

## 📌 1. Visão Geral do Cisco Packet Tracer

O **Packet Tracer** é o simulador oficial da Cisco para arquitetura, configuração e análise de tráfego de redes:
- **Modo Realtime:** A rede opera normalmente como equipamentos físicos em produção.
- **Modo Simulation:** Permite pausar o tempo e inspecionar cada pacote (**PDU**) passando por fios, switches e roteadores camada por camada (excelente para visualizar o ARP, o 3-Way Handshake e o Encapsulamento acontecendo na tela!).

---

## 📌 2. Os Modos de Operação do Cisco IOS (Linha de Comando)

Ao conectar na porta de Console de um Switch ou Roteador Cisco, você navega por 3 níveis de privilégio:

```
Roteador>              <-- 1. Modo Usuário (User Exec Mode) - Visualização básica
   |
   | digitar: enable
   v
Roteador#              <-- 2. Modo Privilegiado (Privileged Exec Mode) - Diagnósticos, show run, ping
   |
   | digitar: configure terminal
   v
Roteador(config)#      <-- 3. Modo de Configuração Global - Onde as alterações reais são feitas
```

---

## 📌 3. Comandos Essenciais do Cisco IOS

### Comandos de Diagnóstico e Consulta (Executar em `Roteador#`):
```cisco
show ip interface brief     ! Mostra status rápido de todas as portas e seus IPs
show ip route               ! Exibe a tabela de roteamento atual do equipamento
show running-config         ! Mostra toda a configuração que está ativa na memória RAM
show mac address-table      ! (No Switch) Mostra a tabela CAM de endereços MAC aprendidos
copy running-config startup-config  ! SALVA as alterações na NVRAM para não perder ao reiniciar
```

### Configurando o IP e Ativando uma Interface de Roteador:
Por padrão de fábrica, as portas dos roteadores Cisco vêm **desligadas (*administratively down*)**. É obrigatório usar `no shutdown`:

```cisco
Roteador# configure terminal
Roteador(config)# interface GigabitEthernet0/0/0
Roteador(config-if)# ip address 192.168.10.1 255.255.255.192
Roteador(config-if)# no shutdown
Roteador(config-if)# exit
```

---

## 📌 4. Laboratório Prático: Montando a Questão 1 no Packet Tracer

Vamos simular o exercício que caiu na sua lista: a rede `192.168.10.0/26` dividida em sub-redes.

```
 [PC 1 - Depto Vendas]                     [PC 2 - Depto Suporte]
  IP: 192.168.10.2                          IP: 192.168.10.66
  Mask: 255.255.255.192                     Mask: 255.255.255.192
  Gateway: 192.168.10.1                     Gateway: 192.168.10.65
           |                                         |
      [Switch 1]                                [Switch 2]
           \                                         /
            \                                       /
             +--- (Gig0/0/0)         (Gig0/0/1) ---+
                           [ROTEADOR]
                  Gig0/0/0: 192.168.10.1/26
                  Gig0/0/1: 192.168.10.65/26
```

### Configuração no Roteador:
```cisco
Router> enable
Router# configure terminal
Router(config)# hostname R1-CAMPUS

! Configurando o Gateway da Sub-rede 1 (Vendas)
R1-CAMPUS(config)# interface GigabitEthernet0/0/0
R1-CAMPUS(config-if)# ip address 192.168.10.1 255.255.255.192
R1-CAMPUS(config-if)# no shutdown
R1-CAMPUS(config-if)# exit

! Configurando o Gateway da Sub-rede 2 (Suporte)
R1-CAMPUS(config)# interface GigabitEthernet0/0/1
R1-CAMPUS(config-if)# ip address 192.168.10.65 255.255.255.192
R1-CAMPUS(config-if)# no shutdown
R1-CAMPUS(config-if)# end
R1-CAMPUS# copy running-config startup-config
```

> 💡 **Teste de Conectividade:**  
> Ao abrir o terminal do `PC 1` e digitar `ping 192.168.10.66`, o pacote sai da Sub-rede 1, bate no Gateway (`192.168.10.1`), o roteador comuta internamente para a interface `Gig0/0/1` e entrega ao `PC 2` na Sub-rede 2 com sucesso!

---

## 🛡️ Laboratório de Cibersegurança: Hardening Básico Cisco

Para começar a pensar como um profissional de **Defesa (Blue Team)** e **Ataque (Red Team)**:

### 1. Protegendo a Senha do Modo Privilegiado com Criptografia:
Por padrão, `enable password` grava a senha em texto claro. Em segurança, usamos `enable secret` (que aplica algoritmo de hash SHA-256):
```cisco
R1-CAMPUS(config)# enable secret SenhaForteCisco#2026
```

### 2. Bloqueando Acesso em Texto Puro (Desabilitar Telnet e Ativar SSH):
O protocolo Telnet (porta 23) envia senhas em texto puro pela rede. Qualquer atacante com Wireshark captura a senha de admin em 2 segundos. Em segurança, forçamos o uso de **SSH (porta 22)**:
```cisco
R1-CAMPUS(config)# ip domain-name empresa.com.br
R1-CAMPUS(config)# crypto key generate rsa
! Escolha 2048 bits
R1-CAMPUS(config)# ip ssh version 2
R1-CAMPUS(config)# username admin privilege 15 secret Admin@Cyber2026!
R1-CAMPUS(config)# line vty 0 4
R1-CAMPUS(config-line)# transport input ssh
R1-CAMPUS(config-line)# login local
```

### 3. Port Security em Switches (Prevenção contra MAC Flooding e Dispositivos Não Autorizados):
Impede que um invasor plugue um notebook malicioso ou execute scripts de forjação de MAC na porta do switch:
```cisco
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown
```
- Se alguém desconectar o cabo do computador autorizado e plugar outro equipamento, a porta desliga imediatamente (**shutdown**) e gera alerta no log de auditoria!
