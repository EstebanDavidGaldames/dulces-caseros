from file_helpers import write_json_file
from config import INVENTARIO_PATH
from .data_input import get_fruta, get_frasco, get_cantidad, get_fecha_produccion
from screen_helpers import clear_screen


def add_lote(lotes:list[dict]):
    fruta = get_fruta() #input('¿Qué dulce preparó? : ')
    tipo = get_frasco() #input('¿Qué frasco utilizó? : ')
    #capacidad = input('¿Qué capacidad tiene el frasco? : ')
    cantidad = get_cantidad() #int(input('¿Cuántos frascos preparó? : '))
    año_de_produccion = get_fecha_produccion() #int(input('¿Año de producción? : '))
    tiempo_de_almacenamiento = 'Produccion.tiempo_de_almacenamiento'
    new_lote = {
        'Fruta':fruta, 
        'Frasco':tipo, 
        #'Capacidad':capacidad, 
        'Cantidad':cantidad, 
        'Año':año_de_produccion, 
        'Tiempo':tiempo_de_almacenamiento}
    
    i = len(lotes)
    print(f'\n'+'Usted agregó un nuevo lote:'+'\n')
    print(f'==== Lote {i+1} ====')

    for key, value in new_lote.items():
        print(f'{key}:{value}')
    lotes.append(new_lote)
    write_json_file(INVENTARIO_PATH, lotes)


def update_lote(lotes:list[dict]):
    while True:
    
        show_lotes(lotes)
        print('\n')
        try:
            to_update = int(input('¿Qué lote desea modificar? : ')) - 1

            if to_update >= 0 and to_update <= len(lotes):
                clear_screen()
                print('\n'+'Usted va a modificar el siguiente lote:'+'\n')
                print(f'==== Lote {to_update+1} ====')

                for key, value in lotes[to_update].items():
                    print(f'{key}:{value}')

                print('\n')

                while True:
                    try:
                        extraidos = int(input('¿Cuántos frascos va a extraer? : '))
                        if extraidos >= 0 and extraidos <= lotes[to_update]['Cantidad']:
                            print('\n')
                            print(f'Usted tenía {lotes[to_update]['Cantidad']} frascos disponibles en el lote {to_update+1}.')
                            lotes[to_update]['Cantidad'] -= extraidos #lotes[to_update]['Cantidad'] = lotes[to_update]['Cantidad'] - extraidos
                            print(f'Ahora tiene {lotes[to_update]['Cantidad']} frascos disponibles en el lote {to_update+1}.')
                            write_json_file(INVENTARIO_PATH, lotes)
                            break
                        else:
                            print('No ingresó una cantidad válida.')
                    except ValueError:
                        print('No ingresó un número válido.')
                break
            else:
                clear_screen()
                print('No ingresó un número de lote válido.')
       
        except ValueError:
            clear_screen()
            print('No ingresó un número válido.')


def show_lotes(lotes:list[dict]):
    print('Usted posee los siguientes lotes:'+'\n')
    n = 1
    for lote in lotes:
        print(f'==== LOTE {n} ====')
        
        for key, value in lote.items():
            print(f'{key}:{value}')
        
        n += 1
    
    print('\n')


def delete_lote(lotes:list[dict]):
    show_lotes(lotes)
    try:
        to_delete = int(input('¿Qué lote desea eliminar? : ')) - 1
        if to_delete >=0 and to_delete <= len(lotes):
            print(f'\n'+'Usted seleccionó eliminar el siguiente lote:'+'\n')
            print(f'==== Lote {to_delete+1} ===='+'\n')

            for key, value in lotes[to_delete].items():
                print(f'{key}:{value}')

            deleted = lotes.pop(to_delete)
            print('\n')
            print(f'Lote {to_delete+1} : Dulce de {deleted['Fruta']} - Año {deleted['Año']} eliminado.')
            write_json_file(INVENTARIO_PATH, lotes)

        else:
            clear_screen()
            print('No ingresó un número de lote válido.')
            delete_lote(lotes)

    except ValueError:
        clear_screen()
        print('No ingresó un número válido.')
        delete_lote(lotes)
