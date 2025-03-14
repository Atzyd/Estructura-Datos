from datetime import datetime

class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None
    
    def add_task(self, description, priority, due_date):
        new_task = Task(description, priority, due_date)
        if not self.head or (new_task.priority < self.head.priority or 
                             (new_task.priority == self.head.priority and new_task.due_date <= self.head.due_date)):
            new_task.next = self.head
            self.head = new_task
            return
        
        current = self.head
        while current.next and (current.next.priority < new_task.priority or
                                (current.next.priority == new_task.priority and current.next.due_date <= new_task.due_date)):
            current = current.next
        
        new_task.next = current.next
        current.next = new_task
    
    def remove_task(self, identifier):
        if not self.head:
            print("No hay tareas para eliminar.")
            return
        
        if isinstance(identifier, str):  # Eliminar por descripción
            if self.head.description == identifier:
                self.head = self.head.next
                print(f"Tarea '{identifier}' eliminada correctamente.")
                return
            
            current = self.head
            while current.next and current.next.description != identifier:
                current = current.next
            
            if current.next:
                current.next = current.next.next
                print(f"Tarea '{identifier}' eliminada correctamente.")
            else:
                print("Tarea no encontrada.")
        
        elif isinstance(identifier, int):  # Eliminar por posición
            if identifier == 0:
                self.head = self.head.next
                print(f"Tarea en la posición {identifier} eliminada correctamente.")
                return
            
            current = self.head
            prev = None
            index = 0
            while current and index < identifier:
                prev = current
                current = current.next
                index += 1
            
            if current:
                prev.next = current.next
                print(f"Tarea en la posición {identifier} eliminada correctamente.")
            else:
                print("Posición fuera de rango.")
    
    def display_tasks(self):
        current = self.head
        index = 0
        if not current:
            print("No hay tareas en la lista.")
            return
        while current:
            print(f"[{index}] Descripción: {current.description}, Prioridad: {current.priority}, Vence: {current.due_date.strftime('%Y-%m-%d')}")
            current = current.next
            index += 1
    
    def search_task(self, description):
        current = self.head
        while current:
            if current.description == description:
                print(f"Descripción: {current.description}, Prioridad: {current.priority}, Vence: {current.due_date.strftime('%Y-%m-%d')}")
                return
            current = current.next
        print("Tarea no encontrada.")
    
    def complete_task(self, description):
        self.remove_task(description)
        print("Tarea marcada como completada y eliminada.")


tm = TaskManager()
tm.add_task("Finalizar reporte", 1, "2024-03-20")
tm.add_task("Hacer ejercicio", 2, "2024-03-22")
tm.add_task("Comprar víveres", 3, "2024-03-21")

tm.display_tasks()

tm.search_task("Hacer ejercicio")

tm.complete_task("Hacer ejercicio")
tm.display_tasks()

tm.remove_task(0)  
tm.display_tasks()