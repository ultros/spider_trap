# 🕸️ spider_trap: The Web Weaver's Nightmare

**Welcome, intrepid coder, to the realm of SPIDER_TRAP!** A concoction so fiendish, it lures unsuspecting web crawlers into an endless waltz of recursive doom. Proceed with caution, for this is not a tool to be trifled with!

This tool is a double-edged sword, sharp enough to ensnare and potentially harm. Deploying SPIDER_TRAP can lead to unintended consequences, including but not limited to:

- **Overwhelming web crawlers** to the point of malfunction.

## 🧪 THE DESIGN

SPIDER_TRAP is a Python script that conjures a web server, serving pages that dynamically generate links to more pages, ad infinitum. This endless web ensnares crawlers, trapping them in a cycle from which they cannot escape.

## 🛠️ SUMMONING THE BEAST

**1. Clone the Repository:**

```bash
git clone https://github.com/ultros/spider_trap.git
cd spider_trap
```

```bash
python spider_trap.py
```

By default, the trap springs to life at http://localhost:80. Adjust the port by modifying the script's configuration variables as needed.

# ⚙️ CONFIGURATION: TAILORING YOUR WEB
Within spider_trap/Core/settings.py, you'll find variables to customize your trap:  

HOST: The IP address to bind the server (default is 'localhost')  
PORT: The port number (default is 8000)  
MAX_DEPTH: The depth of the recursive link structure (tweak with caution!)  

# 🧼 DISARMING THE TRAP
To dismantle the trap:  

Terminate the Script: Press Ctrl+C in the terminal running the server.
