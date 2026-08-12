import requests
import json

def sentiment_analyzer(text_to_analyse):
    """
    Analiza el sentimiento de un texto utilizando la API de IBM Watson.
    
    Args:
        text_to_analyse (str): Texto a analizar
        
    Returns:
        dict: Diccionario con 'label' (str) y 'score' (float)
        
    Raises:
        KeyError: Si la respuesta de la API no tiene el formato esperado
        requests.exceptions.RequestException: Si hay error en la petición HTTP
    """
    
    # Endpoint de la API REST de IBM Watson para análisis de sentimiento
    # Usamos el servicio BERT (Bidirectional Encoder Representations from Transformers)
    # que es un modelo de lenguaje para NLP muy conocido
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Headers HTTP: En la metadata de la request especificamos el modelo de IA a utilizar
    # gRPC-metadata-mm-model-id es el header que espera la API de IBM para identificar el modelo
    # El valor 'sentiment_aggregated-bert-workflow_lang_multi_stock' indica que usamos
    # el modelo BERT multiclase entrenado para múltiples idiomas y dominios
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # Construimos el payload (body) de la request en el formato que espera la API
    # La estructura sigue el estándar de la API: { "raw_document": { "text": "..." } }
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Realizamos la petición POST con los siguientes parámetros:
    # - url: endpoint del servicio
    # - json: payload en formato JSON (automáticamente serializado por requests)
    # - headers: metadatos de la request (modelo a utilizar)
    # Esto nos devuelve un objeto Response de la librería requests
    response = requests.post(url, json=myobj, headers=headers)
    
    # Deserializamos la respuesta JSON a un objeto Python (dict)
    # response.text contiene el string JSON, json.loads() lo convierte a dict
    formatted_response = json.loads(response.text)
    
    # Extraemos los datos del sentimiento de la estructura anidada de la respuesta
    # La API devuelve: { "documentSentiment": { "label": "...", "score": ... } }
    label = formatted_response['documentSentiment']['label'] 
    score = formatted_response['documentSentiment']['score']
    
    # Devolvemos un objeto dict con los datos relevantes
    # Esto permite un fácil acceso a los resultados y mantiene la coherencia de la interfaz
    return {'label': label, 'score': score}