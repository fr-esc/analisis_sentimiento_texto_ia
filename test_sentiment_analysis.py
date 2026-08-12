# Importamos la función que vamos a probar desde el módulo de análisis de sentimiento
# sentiment_analyzer es la función que se conecta a la API de IBM Watson
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer 

# Importamos el módulo unittest de Python para crear pruebas unitarias
# unittest nos proporciona las herramientas para verificar que nuestro código funciona correctamente
import unittest

# Definimos una clase de pruebas que hereda de TestCase
# Cada método dentro de esta clase será una prueba que se ejecutará automáticamente
class TestSentimentAnalyzer(unittest.TestCase): 
    
    # Definimos un método de prueba para el analizador de sentimientos
    # El nombre debe empezar con 'test_' para que unittest lo reconozca como una prueba
    def test_sentiment_analyzer(self): 
        
        # Caso de prueba para sentimiento positivo
        # Enviamos un texto con connotación positiva a la función
        result_1 = sentiment_analyzer('I love working with Python')
        
        # Verificamos que el resultado sea exactamente 'SENT_POSITIVE'
        # assertEqual comprueba que el valor esperado coincida con el valor real
        # Si no coinciden, la prueba fallará y mostrará el error
        self.assertEqual(result_1['label'], 'SENT_POSITIVE') 

        # Caso de prueba para sentimiento negativo
        # Probamos con un texto que expresa odio o rechazo
        result_2 = sentiment_analyzer('I hate working with Python')
        
        # Comprobamos que el sentimiento detectado sea negativo
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE') 
        
        # Caso de prueba para sentimiento neutral
        # Enviamos un texto sin carga emocional clara
        result_3 = sentiment_analyzer('I am neutral on Python')
        
        # Verificamos que el resultado sea neutral
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')
    
# Bloque que se ejecuta solo si este script se ejecuta directamente (no importado)
# Esto permite ejecutar las pruebas desde la línea de comandos
if __name__ == "__main__":
    # Ejecutamos todas las pruebas definidas en la clase
    # unittest.main() busca automáticamente todos los métodos que empiezan con 'test_'
    unittest.main()