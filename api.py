import os
import shutil
from fastapi import FastAPI, UploadFile, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from uuid import uuid4
from gtts import gTTS
#? Modelo CNN
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

pokedex_model = load_model('./Pokedex_Ariel 88% (79% reales) 512x512.keras')

@app.get("/tts")
async def text_to_speech(text: str = Query(...)):
    # Genera el archivo de audio
    tts = gTTS(text, lang="en", tld="co.uk")
    filename = "output.mp3"
    tts.save(filename)

    # Devuelve el archivo de audio
    return FileResponse(filename, media_type="audio/mpeg", filename="output.mp3")

    # Limpia el archivo después de enviarlo
    os.remove(filename)

@app.post("/pokemon")
async def classify_pokemon(file: UploadFile):
    content_type = file.content_type.split('/')[-1]
    file_name = f"{uuid4()}.{content_type}"
    save_path = f"./__temp__/{file_name}"
    #! Para debug; creo la Carpeta si es que NO existe.
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    #? Almaceno el Archivo recibido en el SavePath y lo guardo en una variable Buffer.
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    predicted_mon = predict_pokemon(save_path)
    return { "result": predicted_mon }

__model_classes__ = {'001 - Bulbasaur': 0, '002 - Ivysaur': 1, '003 - Venusaur': 2, '004 - Charmander': 3, '005 - Charmeleon': 4, '006 - Charizard': 5, '007 - Squirtle': 6, '008 - Wartortle': 7, '009 - Blastoise': 8, '010 - Caterpie': 9, '011 - Metapod': 10, '012 - Butterfree': 11, '025 - Pikachu': 12, '150 - Mewtwo': 13}

def predict_pokemon(img_path):
    img = image.load_img(img_path, target_size=(512, 512))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalizar
    img_array = np.expand_dims(img_array, axis=0)

    predictions = pokedex_model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Invertir el diccionario de class_indices
    class_indices = {v: k for k, v in __model_classes__.items()}

    # Obtener la clase predicha
    predicted_class_name = class_indices[predicted_class[0]]
    return predicted_class_name