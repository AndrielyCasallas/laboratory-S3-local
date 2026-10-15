import boto3
from botocore.exceptions import ClientError

# Configuración del cliente S3 apuntando a MinIO AIStor local
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='password123',
    region_name='us-east-1'
)

BUCKET_NAME = 'aistor-smoke-bucket'
FILE_KEY = 'healthcheck.txt'
FILE_CONTENT = 'MinIO AIStor object storage operational and prod-ready.'

def run_minio_test():
    print("[*] Iniciando smoke test para MinIO AIStor...")

    # 1. Crear el Bucket
    try:
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print(f"[+] Bucket '{BUCKET_NAME}' creado exitosamente.")
    except ClientError as e:
        print(f"[-] Nota sobre el bucket (puede que ya exista): {e}")

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

    # 3. Listar los objetos del bucket
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        print(f"\n[+] Contenido actual del bucket '{BUCKET_NAME}':")
        for obj in response.get('Contents', []):
            print(f"    -> Archivo: {obj['Key']} | Tamaño: {obj['Size']} bytes")
    except ClientError as e:
        print(f"[-] Error al listar objetos: {e}")

    print("\n[✓] Smoke test finalizado con éxito.")
    print("    -> Abre http://localhost:9001 e inicia sesión (admin / password123) para ver el bucket y archivo de forma gráfica.")

if __name__ == '__main__':
    run_minio_test()