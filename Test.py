"""
Preguntando a la IA de Google: python code to detect drones with gemini-3.5 flash
Modificado por Alfonso Blanco García 23/05/2026
Gemini normaliza las coordenadas de las imágenes en una escala de 0 a 1000 (donde [0, 0] es la esquina superior izquierda y [1000, 1000] es la inferior derecha). El siguiente código procesa la imagen y extrae la ubicación de cada dron:
"""

import os
import re


# Fuerza la clave en el script (reemplaza con tu clave real)
os.environ["GEMINI_API_KEY"] = "your_api_key_here"



from typing import List
from google import genai
from google.genai import types
from PIL import Image
from PIL import ImageDraw
from pydantic import BaseModel, Field

# 1. Definir la estructura de datos que deseamos recibir usando Pydantic
class DronDeteccion(BaseModel):
    box_2d: List[int] = Field(
        description="Coordenadas de la caja delimitadora en formato [ymin, xmin, ymax, xmax] normalizadas de 0 a 1000."
    )
    confianza: str = Field(
        description="Nivel de certeza de la detección: Alta, Media o Baja."
    )

class ResultadoDeteccion(BaseModel):
    drones_detectados: List[DronDeteccion] = Field(
        description="Lista con todos los drones encontrados en la imagen."
    )

def detectar_drones(ruta_imagen: str):
    # 2. Inicializar el cliente oficial
    client = genai.Client()
    
    try:
        imagen = Image.open(ruta_imagen)
    except FileNotFoundError:
        print(f"Error: No se encontró la imagen en '{ruta_imagen}'")
        return None, imagen

    # 3. Diseñar el prompt operativo
    prompt = (
        "Identifica todos los drones (vehículos aéreos no tripulados, cuadricópteros, "
        "UAVs) presentes en la imagen. Localiza su ubicación exacta mediante cajas delimitadoras."
    )

    print("Analizando imagen con Gemini 3.5 Flash...")
    
    # 4. Llamar a la API forzando la estructura JSON mediante Pydantic
    try:
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=[imagen, prompt],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ResultadoDeteccion,
                temperature=0.1, # Temperatura baja para mayor precisión factual
            ),
        )
        
        # El SDK parsea automáticamente el JSON de vuelta al objeto Pydantic
        resultado: ResultadoDeteccion = response.parsed
        return resultado, imagen

    except Exception as e:
        print(f"Error en la API: {e}")
        #return None
        return None, imagen

# --- Ejemplo de ejecución ---
if __name__ == "__main__":
   
 #imgpath="test\\images"
 #imgpath="Test1" # images test folder
 imgpath="Test2" # images test folder
 for root, dirnames, filenames in os.walk(imgpath):

 
 
   for filename in filenames:
     
    if re.search("\.(jpg|JPEG|jpeg|png|bmp|tiff)$", filename):
         
         
        filepath = os.path.join(root, filename) 

        #detecciones = detectar_drones(archivo_imagen) #MOD
        detections, imagen = detectar_drones(filepath)
        if detections == None:
            imagen.show()
            input("PLEASE, PRESS ENTER TO CONTINUE...")
            continue
        ancho_real, alto_real = imagen.size
        dibujo = ImageDraw.Draw(imagen)
        if detections and detections.drones_detectados:
            print(f"\nSe encontraron {len(detections.drones_detectados)} drones:")
            for idx, dron in enumerate(detections.drones_detectados, 1):
                print(f"\nDron #{idx}:")
                print(f"  - Confianza: {dron.confianza}")

                #¿Cómo pintar las coordenadas en la imagen?#
                #Como Gemini te devuelve los valores normalizados (0-1000), si quieres dibujar los rectángulos
                #sobre la imagen original usando librerías como OpenCV o Pillow,
                # solo debes desnormalizarlos con una simple multiplicación matemática:
                # Ejemplo para convertir las coordenadas de Gemini a píxeles reales
                
                print(f"  - Coordenadas [ymin, xmin, ymax, xmax]: {dron.box_2d}")
                ymin, xmin, ymax, xmax = dron.box_2d
                pixel_ymin = int((ymin / 1000) * alto_real)
                pixel_xmin = int((xmin / 1000) * ancho_real)
                pixel_ymax = int((ymax / 1000) * alto_real)
                pixel_xmax = int((xmax / 1000) * ancho_real)
                

                # 3. Definir las coordenadas del rectángulo [x0, y0, x1, y1]
                # (x0, y0) es la esquina superior izquierda y (x1, y1) la esquina inferior derecha
                #coordenadas = [pixel_ymin, pixel_xmin, pixel_ymax, pixel_xmax]
                coordenadas = [pixel_xmin, pixel_ymin, pixel_xmax, pixel_ymax]

                # 4. Dibujar el rectángulo
                dibujo.rectangle(
                    coordenadas, 
                    outline="red",     # Color del borde (puedes usar nombres o tuplas RGB)
                    width=5,           # Grosor del borde en píxeles
                    #fill="lightblue"   # Color de relleno (puedes omitirlo o usar None para que sea transparente)
                )



        else:
            print("\nNo se detectó ningún dron en la imagen.")
        imagen.show()
        input("PLEASE, PRESS ENTER TO CONTINUE...")
        

