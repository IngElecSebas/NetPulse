import os
import sys
import time
import sqlite3
import threading
import requests
import subprocess
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.live import Live

console = Console()
DB_NAME = "netpulse_metrics.db"

# 1. Inicializar la Base de Datos SQLite
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            target TEXT,
            latency_ms REAL,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 2. Función para medir la latencia (Ping)
def ping_target(target):
    # Ajustar el comando ping según el sistema operativo (Windows usa -n, Linux/macOS usa -c)
    param = "-n" if sys.platform.lower() == "win32" else "-c"
    command = ["ping", param, "1", target]
    
    try:
        start_time = time.time()
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end_time = time.time()
        
        if output.returncode == 0:
            # Intentar extraer la latencia real del output del ping
            match = re.search(r"average[=\s](\d+)\s*ms|media\s*=\s*(\d+)ms", output.stdout, re.IGNORECASE)
            if match:
                latency = float(match.group(1) or match.group(2))
            else:
                latency = (end_time - start_time) * 1000
            return round(latency, 2), "Online"
        else:
            return 0.0, "Offline"
    except Exception:
        return 0.0, "Error"

# 3. Guardar métricas en la base de datos
def log_metric(target, latency, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO metrics (timestamp, target, latency_ms, status)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, target, latency, status))
    conn.commit()
    conn.close()

# 4. Bucle principal de monitoreo
def monitor_loop(targets, stop_event):
    init_db()
    while not stop_event.is_set():
        for target in targets:
            latency, status = ping_target(target)
            log_metric(target, latency, status)
        time.sleep(5) # Muestreo cada 5 segundos

# 5. Generar Tabla en Vivo para la Terminal
def generate_table():
    table = Table(title="📡 Monitor de Red en Tiempo Real - NetPulse")
    table.add_column("Última Actualización", style="cyan")
    table.add_column("Objetivo (Target)", style="magenta")
    table.add_column("Latencia", style="green")
    table.add_column("Estado", style="bold white")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Obtener el último registro de cada objetivo
    cursor.execute('''
        SELECT timestamp, target, latency_ms, status FROM metrics 
        WHERE id IN (SELECT MAX(id) FROM metrics GROUP BY target)
    ''')
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        ts, target, lat, status = row
        status_color = "[green]Online[/]" if status == "Online" else "[red]Offline[/]"
        table.add_row(ts, target, f"{lat} ms", status_color)
    
    return table

import re
if __name__ == "__main__":
    targets = ["8.8.8.8", "github.com", "google.com"]
    stop_event = threading.Event()
    
    # Iniciar el hilo de recolección de datos
    monitor_thread = threading.Thread(target=monitor_loop, args=(targets, stop_event), daemon=True)
    monitor_thread.start()
    
    console.print("[bold green]NetPulse iniciado.[/] Presiona Ctrl+C para salir y guardar.\n")
    
    try:
        # Renderizar la tabla interactiva en Warp
        with Live(generate_table(), refresh_per_second=1) as live:
            while True:
                time.sleep(1)
                live.update(generate_table())
    except KeyboardInterrupt:
        console.print("\n[yellow]Deteniendo NetPulse de forma segura... Base de datos guardada.[/]")
        stop_event.set()