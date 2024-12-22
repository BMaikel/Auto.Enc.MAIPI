# Proyecto: Resolución Automática de Encuestas en MAIPI

Este proyecto automatiza la resolución de encuestas en la plataforma MAIPI de la Universidad Nacional Agraria La Molina utilizando Selenium.

![image](https://github.com/user-attachments/assets/8037a594-ef00-4e80-b76c-12fc2a6f66d6)

## Requisitos Previos

1. **Python 3.x**: Asegúrate de tener instalado Python en tu sistema.
2. **Bibliotecas Necesarias**: Instala las siguientes bibliotecas mediante `pip`:
   - selenium
   - time
   - random
3. **Navegador Brave**: El proyecto utiliza el navegador Brave. Descárgalo e instálalo si aún no lo tienes.
4. **WebDriver**: Asegúrate de tener el ChromeDriver compatible con la versión de Brave instalada.

## Configuración Inicial

### Parámetros Importantes
- **Rutas del navegador y WebDriver**:
  - `brave_path`: Ruta al ejecutable de Brave en tu sistema.
  - `chromedriver_path`: Ruta al archivo de ChromeDriver.
- **Credenciales**:
  - `MAIL`: Correo electrónico institucional para iniciar sesión.
  - `PASS`: Contraseña de tu cuenta.
- **Comentarios**:
  - `COM1`: Respuesta para las preguntas abiertas de la primera parte de las encuestas.
  - `COM2`: Respuesta para las preguntas abiertas de la segunda parte de las encuestas.

### Personalización

Modifica las variables mencionadas en el script según tus necesidades:
- Ajusta los valores de `COM1` y `COM2` para personalizar los comentarios abiertos.
- Configura los tiempos de espera (`time.sleep`) si encuentras problemas de sincronización.

## Estructura del Script

### Principales Funciones

1. **`_login(driver, MAIL, PASS)`**: Realiza el inicio de sesión en la plataforma MAIPI.
   - Navega a la página de inicio.
   - Introduce las credenciales proporcionadas.
   - Maneja el acceso en caso de autenticación de dos factores (espera manual).

2. **`complete_survey(driver)`**: Automatiza la resolución de una encuesta.
   - Selecciona opciones aleatorias para preguntas cerradas.
   - Introduce texto personalizado para preguntas abiertas.
   - Navega entre las páginas de la encuesta y la finaliza.

3. **`_interact_with_surveys(driver)`**: Busca encuestas pendientes y las resuelve.
   - Detecta enlaces a encuestas disponibles.
   - Llama a `complete_survey()` para resolver cada encuesta.

4. **`main()`**: Configura el entorno Selenium, inicia sesión y comienza la interacción con las encuestas.

## Ejecución

1. Configura los parámetros importantes en el archivo.
2. Ejecuta el script con el siguiente comando:
   ```bash
   python <nombre_del_script>.py
   ```
3. Observa cómo el script automatiza la resolución de encuestas en la plataforma MAIPI.

## Notas Importantes

- **Seguridad de las Credenciales**: Evita compartir tu correo y contraseña. Utiliza métodos seguros para almacenar credenciales si planeas compartir el script.
- **Uso Responsable**: Este script debe usarse para fines educativos o personales. Respeta las normas y políticas de uso de la plataforma MAIPI.
- **Mantenimiento**: Si la estructura de la página cambia, puede ser necesario ajustar los selectores de los elementos web.

---

Desarrollado por: Mi, obvio.
