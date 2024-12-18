import os
from PIL import Image

def process_images(input_dir, output_dir, target_size=(224, 224)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for class_name in os.listdir(input_dir):
        class_path = os.path.join(input_dir, class_name)
        if os.path.isdir(class_path):
            class_output_path = os.path.join(output_dir, class_name)
            if not os.path.exists(class_output_path):
                os.makedirs(class_output_path)
            for img_name in os.listdir(class_path):
                img_path = os.path.join(class_path, img_name)
                if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    try:
                        with Image.open(img_path) as img:
                            img = img.resize(target_size)
                            if img.format != 'JPEG':
                                img = img.convert('RGB')
                            output_img_path = os.path.join(class_output_path, f"{os.path.splitext(img_name)[0]}.jpg")
                            img.save(output_img_path, 'JPEG')
                            print(f"Imagen procesada y guardada: {output_img_path}")
                    except Exception as e:
                        print(f"Error procesando {img_name}: {e}")

input_directory = 'D:/Pokedex IA/'
output_directory = 'D:/Pokedex IA/pokemon_dataset/'

process_images(input_directory, output_directory, target_size=(512, 512))
