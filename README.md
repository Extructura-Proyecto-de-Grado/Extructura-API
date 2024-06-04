# Extructura-API
API para el servicio de extracción de texto de facturas electrónicas AFIP para las aplicaciones Extructura desarrollada con Python y Fast-API

## Comandos para ejecutar el servicio
Comando para correr uvicorn, host de api <br>
```uvicorn api.main:app --reload``` 

Para publicar el domino, exponiendo el puerto en donde funciona uvicorn <br>
```ngrok http --domain=allowing-starling-heroic.ngrok-free.app 8000```


