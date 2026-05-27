# --- MÓDULOS (FUNCIONES) ---

def evaluar_compromiso(duracion, clics):
    """
    Evalúa el nivel de compromiso de una sesión según su duración y clics.
    """
    # Lógica de Negocio:
    # Alta: Duración > 180s Y Clics > 8
    if duracion > 180 and clics > 8:
        return "Alto"
    # Baja: Duración < 60s O Clics < 3
    elif duracion < 60 or clics < 3:
        return "Bajo"
    # Media: Cualquier otro caso
    else:
        return "Medio"


def generar_informe(matriz_sesiones):
    """
    Procesa la matriz de sesiones e imprime el informe final.
    """
    print("-" * 40)
    print(f"{'ID CLIENTE':<15} | {'NIVEL DE COMPROMISO'}")
    print("-" * 40)
    
    # Recorremos cada fila (sesión) de la matriz
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        # Llamamos a la función de evaluación
        clasificacion = evaluar_compromiso(duracion, clics)
        
        # Imprimimos el resultado con formato alineado
        print(f"{id_cliente:<15} | {clasificacion}")
    
    print("-" * 40)

# --- DATOS INICIALES (PRINCIPAL) ---

if __name__ == "__main__":
    # Matriz con el formato: [ID Cliente, Duración (s), Eventos Clics]
    # Cumple con el requisito de al menos 5 filas con casos variados
    sesiones_clientes = [
        ["CLI-101", 200, 10],  # Alto ( >180 y >8 )
        ["CLI-102", 45, 5],    # Bajo ( <60 )
        ["CLI-103", 120, 5],   # Medio (Caso intermedio)
        ["CLI-104", 300, 2],    # Bajo ( <3 clics, aunque dure mucho)
        ["CLI-105", 150, 9]    # Medio (No llega a >180s)
    ]
    
    # Ejecutar la herramienta para generar el informe
    generar_informe(sesiones_clientes)