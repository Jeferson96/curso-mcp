 # Demo MCP Server – Clase 4 🚀
 
 Servidor MCP de ejemplo construido con `FastMCP`, pensado para mostrar:
 
 - Cómo definir **tools** (acciones)
 - Cómo exponer **resources** dinámicos
 - Cómo trabajar con **prompts** (`@mcp.prompt`) dentro de un servidor MCP
 
 Este proyecto es una versión un poco más estructurada del demo de la clase 3, ideal para profundizar.
 
 ## 🧩 ¿Qué encontrarás aquí?
 
 - `server.py`: implementación principal del servidor MCP:
   - Tools de aritmética y utilidades de texto.
   - Resources para saludos/despedidas.
   - Prompts de ejemplo para guiar al modelo.
 - `main.py`: punto de entrada (si tu runner/CLI lo requiere).
 - `pyproject.toml`: configuración mínima del proyecto (nombre, dependencias, etc.).

 ## ⚡ Uso de `uv` en este proyecto

 En este proyecto se recomienda usar **`uv`**, una herramienta moderna para gestionar entornos y dependencias de Python.

 - **¿Qué es `uv`?**  
   Es un gestor ultra-rápido para:
   - Crear y gestionar entornos de Python.
   - Instalar dependencias definidas en `pyproject.toml`.
   - Ejecutar comandos dentro de ese entorno sin tener que activar manualmente el virtualenv.

 - **¿Por qué usarlo aquí?**  
   Porque este proyecto ya tiene un `pyproject.toml`, lo que encaja perfecto con el flujo de trabajo de `uv`:  
   puedes sincronizar dependencias y ejecutar el servidor MCP con un par de comandos.

 - **Instalación de `uv`** (si aún no lo tienes):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

   En macOS también puedes instalarlo con Homebrew:

   ```bash
   brew install uv
   ```

 - **Comandos típicos con `uv` en este repo**:

   Desde la carpeta `demo-mcp-server`:

   - **Sincronizar dependencias según `pyproject.toml`:**

     ```bash
     uv sync
     ```

     Esto crea (o actualiza) el entorno y deja todo listo según las dependencias definidas en el proyecto.

   - **Ejecutar el servidor usando el entorno gestionado por `uv`:**

     ```bash
     uv run python server.py
     ```

     `uv run` se encarga de usar el entorno correcto sin que tengas que activarlo manualmente.

   - **Ejecutar otros comandos (por ejemplo, el inspector MCP) dentro del entorno:**

     ```bash
     uv run npx @modelcontextprotocol/inspector mcp run server.py
     ```

     Así te aseguras de que usas las mismas versiones de dependencias del proyecto cuando lanzas herramientas auxiliares.
 
 ## 🛠️ Requisitos rápidos
 
 - Python 3.10 o superior (recomendado).
 - Entorno virtual activado (opcional pero buena práctica).
 - Dependencias instaladas según la configuración del curso/proyecto.
 
 > Si en el curso estás usando un `requirements.txt` global, asegúrate de tenerlo instalado antes de probar este servidor.
 
 ## 📦 Instalaciones MCP recomendadas
 
 1. **CLI oficial de MCP (Python)**
 
    ```bash
    pip install "mcp[cli]"
    ```
 
    Te proporciona una **línea de comandos MCP** para registrar y ejecutar servidores, así como hacer pruebas rápidas desde la terminal.
 
 2. **Inspector visual de MCP (Node.js)**
 
    Desde la carpeta `demo-mcp-server`:
 
    ```bash
    npx @modelcontextprotocol/inspector mcp run server.py
    ```
 
    Abre una UI donde podrás:
 
    - Cargar el servidor definido en `server.py`.
    - Ver todas las **tools**, **resources** y **prompts** disponibles.
    - Ejecutar pruebas interactivas sin escribir código adicional.
 
 3. **Servidor “everything” de ejemplo (Node.js, global)**
 
    ```bash
    npm install -g @modelcontextprotocol/server-everything
    ```
 
    Útil como referencia para comparar este demo sencillo con un servidor MCP mucho más completo.
 
 ## ▶️ Guía rápida de uso
 
 1. (Opcional) Activa tu entorno virtual.
 2. Instala las dependencias que indique el curso/proyecto.
 3. Desde la carpeta `demo-mcp-server`, ejecuta el servidor MCP con tu flujo preferido, por ejemplo:
 
    ```bash
    python server.py
    ```
 
    o bien usando la CLI de MCP / Inspector según tu configuración.
 
 4. Conéctate desde tu cliente MCP o desde el Inspector para explorar tools, resources y prompts.
 
 ## 🧪 Tools disponibles
 
 | Tool | Firma | Propósito |
 | --- | --- | --- |
 | ➕ `add` | `add(a: int, b: int) -> int` | Suma dos enteros. |
 | ➖ `subtract` | `subtract(a: int, b: int) -> int` | Resta el segundo entero al primero. |
 | 🔁 `repeat_message` | `repeat_message(message: str, times: int = 1) -> str` | Repite un mensaje varias veces, validando que `times >= 1`. |
 
 ## 📚 Resources incluidos
 
 - 👋 `greeting://{name}`: genera un saludo personalizado (`Hello, {name}!`).
 - 👋 `farewell://{name}`: genera una despedida personalizada (`Goodbye, {name}!`).
 
 ## 💬 Prompts de ejemplo (`@mcp.prompt`)
 
 - 🧠 `explain_tool_usage()`  
   Prompt pensado para que el modelo **explique cómo usar las tools** del servidor (`add`, `subtract`, `repeat_message`) con ejemplos claros.
 
 - 📘 `math_coach(operation: str, a: int, b: int)`  
   Convierte al modelo en un **“coach de matemáticas”** que explica paso a paso cómo realizar una operación (`operation`) con los números `a` y `b`, y luego da el resultado final.
 
 Estos prompts se pueden invocar desde clientes que soporten prompts MCP (por ejemplo, el Inspector), seleccionándolos por nombre y completando los parámetros cuando aplique.
 
 ## ✅ Buenas prácticas aplicadas
 
 - Docstrings consistentes para tools, resources y prompts.
 - Tipado estricto en parámetros y retornos (`int`, `str`, `dict`, etc.).
 - Separación clara entre:
   - **Tools** → acciones/operaciones.
   - **Resources** → datos dinámicos via esquemas tipo URL.
   - **Prompts** → plantillas para guiar el comportamiento del modelo.
 
 ## 📎 Notas finales
 
 - Ajusta la forma de ejecución (`python server.py`, integración con CLI MCP, etc.) según lo que el curso o tu entorno recomiende.
 - Usa este servidor como laboratorio: añade nuevas tools/resources/prompts mientras avanzas en la clase 4. ✨
 
