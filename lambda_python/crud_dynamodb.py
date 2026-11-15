import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

# Inicializar el recurso. Usará el Rol de IAM si está en EC2 o Lambda.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('Vacantes')

def insertar_datos_ejemplo():
    items = [
        {'habilidad': 'Java', 'fecha_publicacion': '2026-10-10', 'id_vacante': 'V-001', 'empresa': 'TechSol', 'puesto': 'Desarrollador Java', 'ubicacion': 'Culiacán'},
        {'habilidad': 'Python', 'fecha_publicacion': '2026-10-11', 'id_vacante': 'V-002', 'empresa': 'InnovaSoft', 'puesto': 'Programador Python', 'ubicacion': 'Los Mochis'}
    ]
    for item in items:
        tabla.put_item(Item=item)
    print("Datos insertados correctamente.")

def consultar_por_habilidad(habilidad_buscar):
    respuesta = tabla.query(
        KeyConditionExpression=Key('habilidad').eq(habilidad_buscar)
    )
    return respuesta['Items']

# Ejemplo de función Lambda Handler
def lambda_handler(event, context):
    try:
        habilidad = event['queryStringParameters']['habilidad']
        resultados = consultar_por_habilidad(habilidad)
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(resultados)
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }