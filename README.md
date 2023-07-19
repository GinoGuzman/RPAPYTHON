# Proyecto de boletas- convertir .txt a  PDF y Envío de Correo Electrónico.

Este proyecto realiza las siguientes tareas:

1. Lee archivos .txt que contienen información de boletas de pago.
2. Genera un archivo PDF con la tabla consolidada.
4. Permite al usuario ingresar sus credenciales de correo electrónico y seleccionar la ruta donde se encuenetran los .txt.
5. Envía el archivo PDF como adjunto por correo electrónico utilizando SMTP.

## Requisitos

Para ejecutar el script, valida que tienes Python 3.9 o superior instalado. También necesitarás instalar las siguientes bibliotecas de Python:

- `reportlab`: Para la generación del PDF.
- `smtplib`: Para el envío de correos electrónicos.

Puedes instalar las bibliotecas con el siguiente comando:

- pip install reportlab
- pip install secure-smtplib

## Ejecución del programa

1. Clona el repositorio o descarga el código en tu computadora.
2. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra el código.
3. Ejecuta el programa con el siguiente comando: python app.py
4. Sigue las instrucciones en pantalla para ingresar los datos necesarios.

##Configuracion de correo  si tienes activo la utentificacion en dos pasos.

1. Habilitar "Acceso a aplicaciones menos seguras" en tu cuenta de Gmail:

    -Ve a la configuración de seguridad de tu cuenta de Gmail (https://myaccount.google.com/security).
    -Desplázate hacia abajo hasta encontrar la opción "Acceso a aplicaciones menos seguras" y actívala. Esto permitirá que aplicaciones que utilizan contraseñas para     
     acceder a tu cuenta de Gmail puedan conectarse.
   
3. Generar una contraseña de aplicación:
   -Como una medida de seguridad adicional, es recomendable que generes una contraseña de aplicación específica para tu script de Python, en lugar de utilizar tu contraseña      principal de Gmail.
   -Ve a la página de "Contraseña y métodos de inicio de sesión" de tu cuenta de Google (https://myaccount.google.com/apppasswords).
   -Selecciona "Correo" como el tipo de aplicación y "Otra (nombre personalizado)" como el dispositivo.
   -Ingresa un nombre para la aplicación (por ejemplo, "Python Email Script") y haz clic en "Generar".
   -Anota la contraseña que se genera, ya que la necesitarás en tu script de Python.

