import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print('******************************')
    print('==== INVENTARIO DE DULCES ====')
    print('******************************'+'\n')
    print('Opciones: \n')
    print('A: AGREGAR NUEVO LOTE DE DULCES')
    print('B: MOSTRAR LOTES DE DULCES DISPONIBLES')
    print('C: EXTRAER FRASCOS DEL INVENTARIO')
    print('D: ELIMINAR LOTE COMPLETO')
    print('E: SALIR\n')


def get_option():
    option = input('\n ¿Desea realizar otra operación? (S --> Sí / N -- > No): ').upper()
    if option == 'S' or option == 'N':
        return option
    else:
        print('\n Ingrese S para Sí o N para No.')
        return get_option()
