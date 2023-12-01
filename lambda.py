# Fichier : lambda.py

def handler(event, context):
    print("Événement reçu :", event)
    print("Contexte :", context)

    # Une réponse simple
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
