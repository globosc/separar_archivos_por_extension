from pathlib import Path
import shutil

def organize_files_by_extension(root_folder):
    try:
        root_path = Path(r'D:\photos\cam')

        for file_path in root_path.rglob('*.*'):
            if file_path.is_file():
                file_extension = file_path.suffix.lower()
                folder_path = root_path / file_extension.lstrip('.')

                # Verifica si la carpeta ya existe
                if not folder_path.is_dir():
                    folder_path.mkdir(parents=True)
                
                # Verifica si el archivo ya está en la carpeta correspondiente
                if not (folder_path / file_path.name).exists():
                    # Mueve el archivo a la carpeta correspondiente
                    shutil.move(file_path, folder_path / file_path.name)
                    print(f'Movido {file_path} a {folder_path}')
                else:
                    print(f'{file_path.name} ya está en {folder_path}')

        print('Organización completada.')
    except Exception as e:
        print(f'Se produjo un error al organizar los archivos: {e}')

if __name__ == "__main__":
    root_folder = 'directorio_raiz'  # Reemplaza con la ruta de tu directorio raíz
    organize_files_by_extension(root_folder)
