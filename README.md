# Panel de Analistas GCG

Panel interactivo para visualizar y gestionar la distribución de analistas y sus clientes asignados.

## Características

- Visualización de analistas y sus clientes en tarjetas interactivas
- Búsqueda en tiempo real por analista o cliente
- Indicador de estado activo/inactivo basado en horario
- Integración con WhatsApp para contacto rápido
- Marcado de analistas ausentes con doble clic
- Diseño responsive adaptable a diferentes dispositivos
- Animaciones y efectos visuales interactivos

## Uso

1. Abre el archivo `DISTRIBUCION 03-2025.html` en un servidor web
2. Los datos de los analistas se cargan automáticamente desde `analysts_data.json`
3. Usa el campo de búsqueda para filtrar por analista o cliente
4. Haz doble clic en una tarjeta para marcar/desmarcar ausencia
5. Haz clic en el botón de WhatsApp para contactar directamente

## Desarrollo Local

Para ejecutar el proyecto localmente:

```bash
python -m http.server 8000
```

Luego abre `http://localhost:8000/DISTRIBUCION%2003-2025.html` en tu navegador. 