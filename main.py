from dataclasses import dataclass
from fasthtml.common import *

# 1) Definimos nuestra aplicación
app, rt = fast_app()

# 2) Definimos un dataclass que representará la tabla "Task" en SQLite
@dataclass
class Task:
    id: int = None   # Primary key (autoincrement)
    title: str = ""  # Texto de la tarea
    done: bool = False  # ¿Tarea finalizada?

# 3) Conectamos a la base de datos y creamos la tabla si no existe
db = database("tasks.db")
tasks = db.create(Task, pk="id")  # Creamos la tabla 'Task' con pk="id"

########################################################
# UTILIDADES
########################################################

def task_list():
    """
    Genera un listado de todas las tareas, con botones de 'marcar como hecha'
    y 'borrar', y actualiza solamente la sección que muestra tareas.
    """
    all_tasks = tasks.all()
    # Retornamos un contenedor con la lista de tareas
    # Cada tarea tendrá un botón para marcarla como hecha o pendiente, y un botón para eliminar
    return Ul([
        Li(
            f"{t.title} {'(Hecha)' if t.done else '(Pendiente)'} ",
            Button("✔", hx_post=f"/toggle/{t.id}", hx_target="#tasks_list", cls="secondary"),
            Button("X", hx_post=f"/delete/{t.id}", hx_target="#tasks_list", cls="error"),
            style="margin-bottom: 5px;"
        )
