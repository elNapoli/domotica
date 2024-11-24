import os
import importlib.util
import threading

def ejecutar_tarea(task_file):
    task_path = os.path.join('./tasks', task_file)

    spec = importlib.util.spec_from_file_location(task_file, task_path)
    task_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(task_module)

    # Ejecutar la función main() si existe
    if hasattr(task_module, 'main'):
        print(f"Ejecutando la función main() de {task_file}")
        task_module.main()
    else:
        print(f"No se encontró una función main() en {task_file}.")


def ejecutar_tareas():
    # Ruta del directorio donde se encuentran las tareas
    tasks_dir = './tasks'

    # Lista de todos los archivos en el directorio 'tasks/' que son archivos Python (.py)
    task_files = [f for f in os.listdir(tasks_dir) if f.endswith('.py') and f != '__init__.py']

    # Crear un hilo para cada tarea
    for task_file in task_files:
        thread = threading.Thread(target=ejecutar_tarea, args=(task_file,))
        thread.start()  # Inicia la ejecución de la tarea en paralelo

if __name__ == "__main__":
    ejecutar_tareas()
