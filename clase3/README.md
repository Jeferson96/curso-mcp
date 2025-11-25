# Clase 3 – Demo MCP Server 🚀

Pequeño servidor MCP construido con `FastMCP` para practicar cómo definir tools y resources dentro del ecosistema Model Context Protocol.

## 🧩 ¿Qué encontrarás aquí?

- `server.py`: implementación principal con tools y resources.
- Ejemplos de instalación, prueba y ejecución.
- Referencias a utilidades oficiales del ecosistema MCP.

## 🛠️ Requisitos rápidos

- Python 3.10 o superior (usa un entorno virtual si puedes).
- Dependencias del curso instaladas:

```bash
pip install -r ../requirements.txt  # ajusta la ruta si tu archivo vive en otro sitio
```

## 📦 Instalaciones recomendadas

1. **CLI oficial de MCP (Python)**

   ```bash
   pip install "mcp[cli]"
   ```

   Incluye la línea de comandos para registrar servidores y hacer pruebas básicas.

2. **Inspector visual de MCP (Node.js)**

   ```bash
   npx @modelcontextprotocol/inspector mcp run server.py
   ```

   Te abre una UI para cargar `server.py`, ver tools/resources y probarlos sin código adicional.

3. **Servidor “everything” de ejemplo (Node.js, global)**

   ```bash
   npm install -g @modelcontextprotocol/server-everything
   ```

   Útil para comparar este demo sencillo con un servidor MCP más completo.

## ▶️ Guía rápida de uso

1. Activa tu entorno virtual (opcional pero recomendado).
2. Instala dependencias del curso y las utilidades que necesites.
3. Ejecuta el servidor:

   ```bash
   python server.py
   ```

4. Prueba el servidor con tu cliente MCP o abre el Inspector con `npx` si quieres una vista gráfica.

## 🧪 Tools disponibles

| Tool | Firma | Propósito |
| --- | --- | --- |
| ➕ `add` | `add(a: int, b: int) -> int` | Suma dos enteros. |
| ➖ `subtract` | `subtract(a: int, b: int) -> int` | Resta el segundo entero al primero. |
| 🔁 `repeat_message` | `repeat_message(message: str, times: int = 1) -> str` | Repite un mensaje validando que `times >= 1`. |

## 📚 Resources incluidos

- 👋 `greeting://{name}`: genera un saludo personalizado.
- 👋 `farewell://{name}`: devuelve una despedida personalizada.

## ✅ Buenas prácticas aplicadas

- Docstrings consistentes (estilo NumPy/Google) para tools y resources.
- Tipado estricto en parámetros y retornos.
- Separación clara entre **tools** (acciones) y **resources** (datos dinámicos exponiendo esquemas como `greeting://`).

## 📎 Notas finales

- Ajusta rutas a `requirements.txt` según tu estructura local.
- Si usas otro cliente MCP, revisa su documentación para registrar `server.py` como servidor externo.
- Este demo sirve como base; extiéndelo agregando tus propias tools/resources conforme avances en el curso. ✨

