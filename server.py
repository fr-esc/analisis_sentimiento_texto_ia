'''
Este script inicia una aplicación web con Flask que expone un servicio
de análisis de sentimiento. La aplicación se desplegará en localhost:5000
y permitirá a los usuarios enviar texto a través de una interfaz web.
'''

# Importamos Flask y sus herramientas para crear la aplicación web
# render_template: para mostrar archivos HTML
# request: para recibir datos enviados por el usuario
from flask import Flask, render_template, request

# Importamos la función que conecta con la API de IBM Watson
# Esta función es la que realmente analiza el sentimiento del texto
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Creamos la instancia de la aplicación Flask
# El parámetro __name__ ayuda a Flask a ubicar los archivos estáticos y plantillas
app = Flask("Sentiment Analyzer")
   
# Decorador que asocia la ruta "/sentimentAnalyzer" con la función sent_analyzer
# Cuando el usuario visite /sentimentAnalyzer, se ejecutará esta función
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    '''
    Esta función recibe el texto enviado desde la interfaz HTML,
    ejecuta el análisis de sentimiento y devuelve el resultado formateado.
    '''
    
    # Obtenemos el parámetro "textToAnalyze" de la URL (método GET)
    # request.args es un diccionario con los parámetros de la URL
    # .get() devuelve None si el parámetro no existe (evita errores)
    text_to_analyse = request.args.get("textToAnalyze")
    
    # Llamamos a la función que analiza el sentimiento
    # Esta función se conecta a la API de IBM Watson
    response = sentiment_analyzer(text_to_analyse)
    
    # Extraemos los datos de la respuesta
    # El label puede ser 'SENT_POSITIVE', 'SENT_NEGATIVE' o 'SENT_NEUTRAL'
    label = response["label"]
    score = response["score"]
    
    # Devolvemos un mensaje formateado:
    # - Dividimos el label para quedarnos con la parte después del guión bajo
    # - Mostramos el score con su valor numérico
    return "El texto proporcionado ha sido identificado como {} con un puntaje de {}.".format(label.split('_')[1], score)

# Decorador que asocia la ruta raíz "/" con la función render_index_page
# Esta será la página principal de nuestra aplicación
@app.route("/")
def render_index_page():
    '''
    Esta función renderiza y devuelve la página principal (index.html)
    que contiene el formulario para que el usuario introduzca texto.
    '''
    
    # render_template busca el archivo index.html en la carpeta 'templates'
    # y lo devuelve como respuesta HTTP
    return render_template('index.html')

# Este bloque se ejecuta SOLO si ejecutamos este script directamente
# (no cuando lo importamos desde otro archivo)
if __name__ == "__main__":
    '''
    Inicia el servidor web de Flask en localhost (127.0.0.1) puerto 5000
    host="0.0.0.0" permite que la aplicación sea accesible desde otros dispositivos en la red
    port=5000 es el puerto estándar para aplicaciones Flask
    '''
    
    # app.run() inicia el servidor web
    # La aplicación estará disponible en: http://localhost:5000
    app.run(host="0.0.0.0", port=5000)