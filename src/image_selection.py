from pathlib import Path
import random
import yaml

_ROOT = Path(__file__).resolve().parents[0]
used_images_path = _ROOT / 'data/used_images.yaml'
print(used_images_path)

def get_filepaths(patterns):
    path = _ROOT.parents[0] / 'images'
    files = []
    for pattern in patterns:
        file = path.glob(pattern)
        files += file
    return files


def save_used_paths(files):
    yaml_dict = {
        'used_images': [str(x) for x in files]
    }
    with open(used_images_path, 'w') as yaml_file:
        yaml.safe_dump(yaml_dict, yaml_file)


def load_used_images():
    with open(used_images_path) as file:
        used_images = yaml.load(file, Loader=yaml.FullLoader)
    return used_images


def get_random_image():
    # 1. Leer lista de todas las imagenes en la carpeta y las ya usadas
    files = get_filepaths(['*.jpg', '*.png', '*.jpeg'])
    used_images = load_used_images()['used_images']

    # 2. Convertir ambas a set (sin dupes)
    files = set([str(x) for x in files])

    # 2.1 Comprobar que used_images no esta vacio
    if used_images:
        used_images = set(used_images)
    else:
        used_images = set()

    # 3. Nuevo set formado por la diferencia
    usable_images = files.difference(used_images)

    # 4. Elegir imagen random de las disponibles
    if not usable_images:
        image_path = random.choice(tuple(files))
    else:
        image_path = random.choice(tuple(usable_images))
    print('-------')
    print('Seleccion:' + str(image_path))
    print('-------')

    # 5. Updatear lista de imagenes usadas
    used_images.add(image_path)
    save_used_paths(used_images)

    return image_path
