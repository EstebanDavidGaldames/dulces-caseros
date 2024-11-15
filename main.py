from screen_helpers import clear_screen, get_option
from file_helpers import read_json_file
from config import INVENTARIO_PATH
from core import add_lote, update_lote, show_lotes, delete_lote


def menu():
    print('Opciones: \n')
    print('A: AGREGAR NUEVO LOTE DE DULCES')
    print('B: MOSTRAR LOTES DE DULCES DISPONIBLES')
    print('C: EXTRAER FRASCOS DEL INVENTARIO')
    print('D: ELIMINAR LOTE COMPLETO')
    print('E: SALIR\n')





def main():
    lotes = read_json_file(INVENTARIO_PATH)

    while True:
        menu()
        choosed = input('¿Qué operación deseas realizar? ').upper()
        match choosed:
            case 'A':
                clear_screen()
                add_lote(lotes)
            case 'B':
                clear_screen()
                show_lotes(lotes)
            case 'C':
                clear_screen()
                update_lote(lotes)
            case 'D':
                clear_screen()
                delete_lote(lotes)
            case 'E':
                clear_screen()
                print('\n*** ==== INVENTARIO DE DULCES APAGADO=== ***\n')
                break               
            case _ :
                clear_screen()
                print('No ingresó una opción válida.\nIngrese una opción válida.')
                continue

        option = get_option() #input('\n ¿Desea realizar otra operación? ')
        if option == 'S':
            clear_screen()
            continue
        elif option == 'N':
            clear_screen()
            print('\n*** ==== INVENTARIO DE DULCES APAGADO=== ***\n')
            break


if __name__ == '__main__':
    clear_screen()
    print('******************************'+'\n'+'==== INVENTARIO DE DULCES ===='+'\n'+'******************************')
    main()
