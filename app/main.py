import os
import time
import importlib.util

def ejecutar_tareas():
    # Ruta del directorio donde se encuentran las tareas
    tasks_dir = './tasks'

    # Lista de todos los archivos en el directorio 'tasks/' que son archivos Python (.py)
    task_files = [f for f in os.listdir(tasks_dir) if f.endswith('.py') and f != '__init__.py']

    for task_file in task_files:
        # Construye la ruta completa del archivo de la tarea
        task_path = os.path.join(tasks_dir, task_file)

        # Usa 'importlib' para cargar el módulo dinámicamente
        spec = importlib.util.spec_from_file_location(task_file, task_path)
        task_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(task_module)

        # Si los archivos en tasks tienen alguna función o código que ejecutar, este se ejecutará ahora.
        print(f"Ejecutando tarea: {task_file}")

# Bucle que ejecuta las tareas cada 10 segundos
if __name__ == "__main__":
    while True:
        print("Esperando 10 segundos para la próxima ejecución...")
        time.sleep(10)

