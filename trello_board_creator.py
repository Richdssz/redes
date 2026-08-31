import os
import json
import urllib.request
import urllib.parse
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def load_env():
    env = {}
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
    return env

env = load_env()
API_KEY = env.get("TRELLO_API_KEY")
TOKEN = env.get("TRELLO_TOKEN")

if not API_KEY or not TOKEN:
    print("[!] Chave ou Token do Trello nao encontrados! Verifique o .env")
    sys.exit(1)

BASE_URL = "https://api.trello.com/1"

def trello_req(endpoint, params=None, data=None, method="GET"):
    if params is None:
        params = {}
    params["key"] = API_KEY
    params["token"] = TOKEN
    
    query = urllib.parse.urlencode(params)
    url = f"{BASE_URL}{endpoint}?{query}"
    
    encoded_data = None
    if data is not None:
        encoded_data = urllib.parse.urlencode(data).encode("utf-8")
    elif method in ["POST", "PUT"]:
        encoded_data = b""

    req = urllib.request.Request(url, data=encoded_data, method=method)
    req.add_header("Accept", "application/json")
    
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        print(f"[!] Erro na requisicao {method} {url}: {e.code} - {err_msg}")
        raise

print("[*] Conectando ao Trello...")
board = trello_req("/boards", {
    "name": "🌐 Estudos - Redes de Computadores",
    "defaultLists": "false",
    "prefs_background": "blue"
}, method="POST")

board_id = board["id"]
board_url = board["shortUrl"]
print(f"[+] Quadro criado com sucesso!\n🔗 Link: {board_url}\n")

# Criar Labels
labels_to_create = [
    ("Fundamentos", "green"),
    ("Camada de Rede", "orange"),
    ("Camada de Transporte", "purple"),
    ("Camada de Aplicação", "sky"),
    ("Prática & Wireshark", "red")
]
labels_map = {}
for lname, lcolor in labels_to_create:
    lb = trello_req(f"/boards/{board_id}/labels", {
        "name": lname,
        "color": lcolor
    }, method="POST")
    labels_map[lname] = lb["id"]

# Criar Listas
lists_data = [
    "📌 Material & Referências",
    "📚 Módulos do Roadmap",
    "⏳ Em Estudo (Foco Atual)",
    "🎯 Quizzes & Prática",
    "✅ Concluído & Dominado"
]
lists_map = {}
for lname in lists_data:
    lst = trello_req("/lists", {
        "name": lname,
        "idBoard": board_id
    }, method="POST")
    lists_map[lname] = lst["id"]
    print(f"  [+] Lista criada: {lname}")

# 1. Cards na lista Material & Referências
ref_list_id = lists_map["📌 Material & Referências"]

refs = [
    {
        "name": "📖 Livro 1: Kurose & Ross (6ª Ed.) - Top-Down",
        "desc": "**Arquivo local:** `kurose_top_down.txt`\n\nAbordagem da camada de aplicação até a física. Principal referência universitária.",
        "labels": [labels_map["Fundamentos"]]
    },
    {
        "name": "📖 Livro 2: Tanenbaum & Wetherall (6ª Ed.)",
        "desc": "**Arquivos locais:** `tanenbaum_6a.txt` e `Tanenbaum_Redes_de_Computadores_6a.pdf`\n\nReferência clássica e profunda em ciência da computação.",
        "labels": [labels_map["Fundamentos"]]
    },
    {
        "name": "🛠️ Ferramentas Práticas: Wireshark & Packet Tracer",
        "desc": "- **Wireshark**: Análise de tráfego e pacotes reais.\n- **Cisco Packet Tracer**: Simulação de topologias e switches/roteadores.\n- **SubnettingPractice.com**: Treino de cálculo de sub-redes.",
        "labels": [labels_map["Prática & Wireshark"]]
    }
]

for r in refs:
    trello_req("/cards", {
        "idList": ref_list_id,
        "name": r["name"],
        "desc": r["desc"],
        "idLabels": ",".join(r["labels"])
    }, method="POST")

# 2. Cards na lista Módulos do Roadmap com Checklists
modules_list_id = lists_map["📚 Módulos do Roadmap"]

modules = [
    {
        "title": "Módulo 1: Fundamentos & Modelos (OSI vs TCP/IP)",
        "desc": "Conceitos fundamentais de redes, topologias, encapsulamento e comparação entre Modelo OSI e Pilha TCP/IP.",
        "label": labels_map["Fundamentos"],
        "items": [
            "1.1 Classificação de redes (LAN, MAN, WAN, PAN)",
            "1.2 Topologias (Estrela, Malha, Barramento, Anel)",
            "1.3 Modelo OSI (7 camadas) vs TCP/IP (4/5 camadas)",
            "1.4 Encapsulamento, Desencapsulamento e PDUs",
            "1.5 Latência, Throughput, RTT, Jitter e Perda de Pacotes"
        ]
    },
    {
        "title": "Módulo 2: Camada Física e Enlace de Dados",
        "desc": "Transmissão física de sinais, padrão Ethernet, switches, endereçamento MAC e segmentação de rede.",
        "label": labels_map["Prática & Wireshark"],
        "items": [
            "2.1 Meios físicos (Par trançado, Fibra, Wi-Fi 802.11)",
            "2.2 Endereçamento Físico (MAC Address e Broadcast)",
            "2.3 Padrão Ethernet (IEEE 802.3) e CSMA/CD",
            "2.4 Switches e Tabela MAC (CAM Table)",
            "2.5 Protocolo ARP (Address Resolution Protocol)",
            "2.6 VLANs (IEEE 802.1Q) e Portas de Acesso vs Trunk",
            "2.7 Spanning Tree Protocol (STP) e prevenção de loops"
        ]
    },
    {
        "title": "Módulo 3: Camada de Rede (IPv4, IPv6, Subnetting & Roteamento)",
        "desc": "Endereçamento lógico, cálculo de sub-redes CIDR, protocolos ICMP/NAT e roteamento OSPF/BGP.",
        "label": labels_map["Camada de Rede"],
        "items": [
            "3.1 Protocolo IPv4 e Cabeçalho (RFC 791)",
            "3.2 Subnetting e Notação CIDR (/24, /27, etc.)",
            "3.3 Cálculo rápido de rede, broadcast e faixa de hosts",
            "3.4 Protocolo IPv6 (SLAAC, notação e tipos)",
            "3.5 ICMP: Ping (Echo Request/Reply) e Traceroute (TTL)",
            "3.6 NAT, PAT e CGNAT",
            "3.7 Roteamento Estático vs Dinâmico (OSPF, BGP)"
        ]
    },
    {
        "title": "Módulo 4: Camada de Transporte (TCP vs UDP)",
        "desc": "Multiplexação por portas, controle de conexão, confiabilidade do TCP e baixa latência do UDP.",
        "label": labels_map["Camada de Transporte"],
        "items": [
            "4.1 Sockets (IP:Porta) e Portas Conhecidas/Efêmeras",
            "4.2 Protocolo UDP (Características e casos de uso)",
            "4.3 Protocolo TCP: Cabeçalho e Flags (SYN, ACK, FIN, RST)",
            "4.4 Three-Way Handshake (SYN -> SYN-ACK -> ACK)",
            "4.5 Confiabilidade: Números de Sequência (SEQ) e ACK",
            "4.6 Janela Deslizante (Sliding Window) e Controle de Fluxo",
            "4.7 Controle de Congestionamento (Slow Start, TCP Reno/Cubic)"
        ]
    },
    {
        "title": "Módulo 5: Camada de Aplicação (DNS, DHCP, HTTP, TLS)",
        "desc": "Protocolos de serviços que operam direto com o usuário e a web moderna.",
        "label": labels_map["Camada de Aplicação"],
        "items": [
            "5.1 DNS: Resolução hierárquica e registros (A, AAAA, CNAME, MX)",
            "5.2 DHCP: Processo DORA (Discover, Offer, Request, ACK)",
            "5.3 HTTP/1.1 vs HTTP/2 (multiplexing) vs HTTP/3 (QUIC)",
            "5.4 HTTPS e TLS Handshake (Criptografia simétrica/assimétrica)",
            "5.5 SSH, FTP/SFTP, SMTP e WebSockets"
        ]
    },
    {
        "title": "Módulo 6: Segurança, Diagnóstico e Redes em Nuvem",
        "desc": "Firewalls, proxies, VPNs, inspeção de pacotes no Wireshark e topologias de nuvem.",
        "label": labels_map["Prática & Wireshark"],
        "items": [
            "6.1 Firewalls Stateful vs Stateless e IDS/IPS",
            "6.2 Reverse Proxy (Nginx) e Load Balancers L4 vs L7",
            "6.3 VPNs (IPsec, WireGuard, OpenVPN)",
            "6.4 Captura e filtros no Wireshark (tcpdump)",
            "6.5 Redes em Nuvem: VPC, Subnets Públicas/Privadas, Gateways"
        ]
    }
]

for m in modules:
    card = trello_req("/cards", {
        "idList": modules_list_id,
        "name": m["title"],
        "desc": m["desc"],
        "idLabels": m["label"]
    }, method="POST")
    card_id = card["id"]
    print(f"  [+] Card criado: {m['title']}")
    
    # Criar Checklist
    cl = trello_req(f"/cards/{card_id}/checklists", {
        "name": "Checklist de Aprendizado"
    }, method="POST")
    cl_id = cl["id"]
    
    for item in m["items"]:
        trello_req(f"/checklists/{cl_id}/checkItems", {
            "name": item
        }, method="POST")

print(f"\n[✔] SUCESSO! Quadro completo criado no Trello!")
print(f"🔗 Link do Quadro: {board_url}")
