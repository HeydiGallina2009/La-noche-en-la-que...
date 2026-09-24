class NivelPadre:
    """Clase padre que define la estructura básica de un nivel."""
    def __init__(self, numero_nivel):
        self.numero_nivel = numero_nivel

    def jugar(self):
        print(f"\n--- JUGANDO EL NIVEL {self.numero_nivel} ---")
        print("Controles: [W] Adelante | [A] Izquierda | [S] Atrás | [D] Derecha")
        print("Opciones: [reiniciar] Repetir nivel | [volver] Menú principal")
        print("*(Debes ingresar 2 comandos de movimiento para pasar el nivel)*\n")
        
        comandos_ingresados = 0
        
        while comandos_ingresados < 2:
            accion = input(f"[Nivel {self.numero_nivel} - Movimiento {comandos_ingresados + 1}/2] Ingresa una tecla o comando: ").strip().lower()
            if accion == 'w':
                print("-> Vas hacia adelante.")
                comandos_ingresados += 1
            elif accion == 'a':
                print("-> Vas hacia la izquierda.")
                comandos_ingresados += 1
            elif accion == 's':
                print("-> Vas hacia atrás.")
                comandos_ingresados += 1
            elif accion == 'd':
                print("-> Vas hacia la derecha.")
                comandos_ingresados += 1
            elif accion == 'reiniciar':
                return 'reiniciar'
            elif accion == 'volver':
                return 'volver'
            else:
                print("Entrada no válida. Usa W, A, S, D para moverte, o escribe 'reiniciar' / 'volver'.")

        print(f"\n¡Has realizado 2 movimientos con éxito!")
        return 'si'

class Nivel1(NivelPadre):
    def __init__(self):
        super().__init__(1)

class Nivel2(NivelPadre):
    def __init__(self):
        super().__init__(2)

class Nivel3(NivelPadre):
    def __init__(self):
        super().__init__(3)

class Nivel4(NivelPadre):
    def __init__(self):
        super().__init__(4)


def mostrar_tutorial():
    """Muestra los controles del juego."""
    print("\n" + "="*30)
    print("Tutorial: Cómo jugar")
    print("Presiona la tecla 'w' para avanzar.")
    print("Presiona la tecla 'a' para la izquierda.")
    print("Presiona la tecla 's' para atrás.")
    print("Presiona la tecla 'd' para la derecha.")
    print("="*30 + "\n")


def iniciar_juego():
    """Flujo principal del juego."""
    while True:
        print("\n*** BIENVENIDA AL JUEGO ***")
        ver_tutorial = input("¿Ver tutorial de como jugar? (si / no): ").strip().lower()
        
        if ver_tutorial == 'si':
            mostrar_tutorial()
            volver = input("¿Deseas volver al menú de inicio? (si / no): ").strip().lower()
            
            if volver == 'si':
                print("Regresando al menú de inicio...")
                continue
            else:
                print("Iniciando el juego desde el Nivel 1...")
        niveles = [Nivel1(), Nivel2(), Nivel3(), Nivel4()]
        indice_nivel = 0
        volver_inicio = False

        while indice_nivel < len(niveles):
            nivel_actual = niveles[indice_nivel]
            resultado = nivel_actual.jugar()
            
            if resultado == 'si':
                print(f"¡Nivel {nivel_actual.numero_nivel} superado! Pasando al siguiente...")
                indice_nivel += 1
            elif resultado == 'reiniciar':
                print(f"Reiniciando el Nivel {nivel_actual.numero_nivel}...")
                continue
            elif resultado == 'volver':
                volver_inicio = True
                break
                
        if volver_inicio:
            print("Regresando al menú principal...")
            continue

        if indice_nivel == len(niveles):
            print("\n¡Felicidades! Has completado el nivel final.")
            print("--- FIN ---")
            break

if __name__ == "__main__":
    iniciar_juego()