import time

def crear_proceso():
    print("Llamada al sistema: Creación de proceso")
    print("Proceso creado: Estado = 'Listo'")
    return "Listo"

def ejecutar_proceso():
    print("Llamada al sistema: Ejecución de proceso")
    print("Proceso en ejecución: Estado = 'En ejecución'")
    suma = sum([5, 2, 4, 7, 3])  # Tarea del proceso
    print(f"Resultado de la suma: {suma}")
    return "En ejecución"

def terminar_proceso():
    print("Llamada al sistema: Terminación de proceso")
    print("Proceso terminado: Estado = 'Terminado'")
    return "Terminado"

# Simulación del flujo de un proceso
estado = crear_proceso()
time.sleep(1)  # Simula el tiempo de espera
estado = ejecutar_proceso()
time.sleep(1)  # Simula el tiempo de espera
estado = terminar_proceso()

