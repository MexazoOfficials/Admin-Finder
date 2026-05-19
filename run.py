#Developers : MexazoExecuted
#Team : Youth Of Pantura
#Github : https://github.com/MexazoOfficials
import os
import sys
import time
import random
import requests
import cloudscraper
from rich.console import Console
from rich.panel import Panel
from urllib.parse import urljoin

os.system("clear")
console = Console()

def status():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return "[bold green]AKTIF[/bold green]" if response.status_code == 200 else "[bold red]TIDAK AKTIF[/bold red]"
    except:
        return "TIDAK AKTIF"

console.print(f"""[bold cyan]
          ⠀⠀⠀      ⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀       ⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
      ⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
      ⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
      ⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
      ⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
      ⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
      ⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
     ⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
    ⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
     ⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
     ⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
     ⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂[/bold cyan]""")
admin_paths = []
try:
    response = requests.get("https://gist.githubusercontent.com/MexazoOfficials/f8d0cd2be1f66f274c067090ff801ab3/raw/2e9821b717cebca8c7897e9b856b9b1f868d1e8f/page_admin.txt")
    if response.status_code == 200:
        for line in response.text.splitlines():
            path = line.strip()
            if path and not path.startswith('#'):
                admin_paths.append(path)
    else:
        sys.exit(1)
except Exception as e:
    sys.exit(1)

total_path = len(admin_paths)
console.print(Panel(f"""[bold white][[cyan]•[/cyan]] Developers : [underline]MexazoExecuted[/underline]
[[cyan]•[/cyan]] Github : [underline]https://github.com/MexazoOfficials[/underline]
[[cyan]•[/cyan]] Team : [underline]Youth Of Pantura[/underline]
[[cyan]•[/cyan]] Tools : [underline]Admin - Finder - Login[/underline]
[[cyan]•[/cyan]] Version : [underline]2.5[/underline]
[[cyan]•[/cyan]] Conection : [underline]{status()}[/underline]
[[cyan]•[/cyan]] Total Path : [underline]{total_path}[/underline][/bold white]""",border_style="#B8B8B8",title="[white on black][bold underline]INFORMASI[/bold underline]",title_align="center"))
url = console.input("[bold white][[bold cyan]•[/bold cyan]] Target URL: ").strip()
if not url.endswith('/'):
    url += '/'

scraper = cloudscraper.create_scraper()
found_list = []
not_found_list = []
for i, path in enumerate(admin_paths, 1):
    url_target = urljoin(url, path)
    time.sleep(1)
    try:
        response = scraper.get(url_target, allow_redirects=True, timeout=10)
        status_code = response.status_code
        if status_code in [200, 201, 202, 203, 204, 205, 206, 301, 302, 303]:
            console.print(f"[bold white][[bold green]FOUND[/bold green]] [bold white]{url_target}[/bold white] - Status > [bold green]{status_code}[/bold green]")
            found_list.append(url_target)
        elif status_code == 404:
            console.print(f"[bold white][[bold yellow]NOT FOUND[/bold yellow]] [bold white]{url_target}[/bold white] - Status > [bold yellow]404[/bold yellow]")
            not_found_list.append(url_target)
        elif status_code == 403:
            console.print(f"[bold white][[bold red]BLOCKED TO CF[/bold red]] [bold white]{url_target}[/bold white] - Status > [bold red]403[/bold red]")
            console.print(f"[bold white] Wait 10Sec - Recovery Limit[/bold white]")
            time.sleep(10)
        else:
            console.print(f"[bold white][[bold #B8B8B8]CANNOT[/bold #B8B8B8]] [bold white]{url_target}[/bold white] - Status > [bold magenta]{status_code}[/bold magenta]")
    except Exception as e:
        console.print(f"[bold white][[bold red]ERROR[/bold red]] [bold white]{url_target}[/bold white] - {str(e)[:50]}")

console.print(Panel(f"""[bold white][•] Total Path Discanned: {len(admin_paths)}
[•] Total Found: {len(found_list)}
[•] Total Not Found: {len(not_found_list)}[/bold white]""",border_style="#B8B8B8",title="[white on black][bold underline]RESULT[/bold underline]",title_align="center"))

if found_list:
    console.print("\n[bold white][•] LIST OF FOUND ADMIN PANELS:[/bold white]")
    for i, url_found in enumerate(found_list, 1):
        console.print(f"[bold green]    {i}. {url_found}[/bold green]")
    with open("admin_found.txt", "w") as f:
        for url_found in found_list:
            f.write(url_found + "\n")
    console.print(f"\n[bold green][✓] Results saved to admin_found.txt[/bold green]")
else:
    console.print("\n[bold yellow][•] No admin panels found.[/bold yellow]")

