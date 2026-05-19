# NetPulse

NetPulse es una herramienta modular diseñada para monitorear el rendimiento de red en tiempo real, registrar latencias y generar gráficos históricos de desempeño. Utiliza SQLite como base de datos para almacenar métricas y proporciona una visualización interactiva en la terminal, además de una representación gráfica del historial con Matplotlib.

---

## Características

- **Monitoreo periódico:** Realiza pings cada 5 segundos a objetivos específicos para rastrear su estado y latencia.
- **Base de datos SQLite:** Guarda todos los registros de latencia, timestamp y estado en `netpulse_metrics.db`.
- **Tabla interactiva en la terminal:** Utiliza `rich.live` para mostrar los datos en tiempo real de forma visual y ordenada.
- **Generación de gráficos:** Exporta gráficos de líneas representando las latencias históricas almacenadas como un archivo PNG.

---

## Archivos principales

### 1. `netpulse.py`
- **Propósito:**
  - Ejecuta el monitoreo de latencias para los objetivos `8.8.8.8`, `github.com` y `google.com`.
  - Almacena estas métricas en la base de datos.
  - Proporciona visualización en vivo en la terminal.

- **Cómo ejecutarlo:**
  ```bash
  python netpulse.py
  ```
- **Salida:**
  - Interfaz interactiva mostrando objetivos con sus respectivas latencias y estados.

### 2. `generate_charts.py`
- **Propósito:**
  - Extrae datos históricos de `netpulse_metrics.db`.
  - Genera gráficos de líneas visualizando las latencias históricas.
  - Exporta el gráfico como `charts/network_performance.png`.

- **Cómo ejecutarlo:**
  ```bash
  python generate_charts.py
  ```
- **Requisitos previos:**
  - Asegúrate de que exista la base de datos con datos relevantes.
  - Instala Matplotlib si es necesario:
    ```bash
    pip install matplotlib
    ```

### 3. `charts/network_performance.png`
- **Propósito:**
  - Archivo generado que muestra visualmente el rendimiento de la red a lo largo del tiempo a través de las latencias registradas.

---

## Configuración

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/IngElecSebas/NetPulse.git
   cd NetPulse
   ```

2. **Instalar dependencias necesarias**
   - Solo si necesitas Matplotlib:
     ```bash
     pip install matplotlib
     ```

3. **Ejecutar el monitoreo en tiempo real**
   ```bash
   python netpulse.py
   ```

4. **Generar gráficos de desempeño**
   ```bash
   python generate_charts.py
   ```

   - Gráficos exportados en: `charts/network_performance.png`

---

## Herramientas utilizadas

- **Lenguaje de programación:** Python
- **Bases de datos:** SQLite
- **Visualización interactiva:** `rich` (tabla en la terminal)
- **Gráficos:** Matplotlib

---

## Estructura del repositorio

```plaintext
NetPulse/
├── charts/                     # Carpeta donde se guardan los gráficos
│   └── network_performance.png # Gráfico de latencias históricas
├── netpulse.py                 # Script principal para monitoreo en tiempo real
├── generate_charts.py          # Script secundario para generar gráficos
├── netpulse_metrics.db         # Base de datos SQLite con las métricas registradas
├── AGENTS.md                   # Archivo de ayuda para agentes OpenCode
├── README.md                   # Este archivo explicativo
```