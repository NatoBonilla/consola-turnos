from numeros import siguiente_f, siguiente_p, siguiente_c

def turnero():
    while True:
        print("Bienvenido.")
        print("Las opciones para ser atendido son las siguientes: ")
        print("[1] Farmacia")
        print("[2] Perfumeria")
        print("[3] Cosmética")
        opcion = input("Escoja una opcion por favor: ")
        print("\n")

        if opcion == "1":
            siguiente_f()
        elif opcion == "2":
            siguiente_p()
        elif opcion == "3":
            siguiente_c()
        else:
            print("Ingrese una opcion valida.")
            
        
        while True:
            print("\n")
            otro_turno = input("Quieres sacar otro turno? [S]/[N]: ").upper()
            if otro_turno in ["S", "N"]:
                break
        
            else:
                print("Esa no es una opcion valida")
                continue
                    
                
        if otro_turno == "N":
            print("Gracias por venir, vuelva pronto.")
            break
        
            

turnero()