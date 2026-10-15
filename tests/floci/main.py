import boto3
from botocore.exceptions import ClientError

# Configuración del cliente S3 apuntando al core de Floci
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

BUCKET_NAME = 'lab-s3-smoke-test'
FILE_KEY = 'payload-prod_1.txt'
FILE_CONTENT = '¡Pipeline S3 con Floci y Web UI operando al 100%! Prod-ready.'

def run_smoke_test():
    print("[*] Iniciando smoke test para S3 local (Floci)...")

    # 1. Crear el Bucket
    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"[+] Bucket '{BUCKET_NAME}' provisionado exitosamente.")
    except ClientError as e:
        print(f"[-] Advertencia o error al crear el bucket: {e}")

    # 2. Subir un objeto de prueba
    try:
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=FILE_KEY,
            Body=FILE_CONTENT
        )
        print(f"[+] Archivo '{FILE_KEY}' subido correctamente al bucket.")
    except ClientError as e:
        print(f"[-] Error al subir el objeto: {e}")
        return

    # 3. Listar los objetos del bucket para verificar paridad
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        print(f"\n[+] Contenido actual del bucket '{BUCKET_NAME}':")
        for obj in response.get('Contents', []):
            print(f"    -> Archivo: {obj['Key']} | Tamaño: {obj['Size']} bytes")
    except ClientError as e:
        print(f"[-] Error al listar objetos: {e}")

    print("\n[✓] Smoke test ejecutado con éxito.")
    print("    -> Entra a http://localhost:8080 para verificar visualmente el bucket y el archivo.")

if __name__ == '__main__':
    run_smoke_test()