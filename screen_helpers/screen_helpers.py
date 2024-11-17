import os

from termcolor import colored

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu():
    print(colored('******************************', 'light_red', 'on_black'))
    print(colored('==== INVENTARIO DE DULCES ====', 'light_red', 'on_black', attrs=['bold']))
    print(colored('******************************', 'light_red', 'on_black')+'\n')
    print(colored('Opciones:', 'light_cyan')+'\n')
    print(colored('A: AGREGAR NUEVO LOTE DE DULCES', 'green'))
    print(colored('B: MOSTRAR LOTES DE DULCES DISPONIBLES', 'light_green'))
    print(colored('C: EXTRAER FRASCOS DEL INVENTARIO', 'light_blue'))
    print(colored('D: ELIMINAR LOTE COMPLETO', 'blue'))
    print(colored('E: SALIR', 'cyan')+'\n')


def get_option():
    option = input('\n'+colored('¿Desea realizar otra operación? ', 'light_yellow')+colored('(S --> Sí / N --> No): ', 'red', attrs=['bold'])).upper()
    if option == 'S' or option == 'N':
        return option
    else:
        print('\n'+colored('Ingrese S para Sí o N para No.', 'light_green'))
        return get_option()
