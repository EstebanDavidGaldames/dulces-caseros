def menu():
    print('Opciones: \n')
    print('A: AGREGAR NUEVO LOTE DE DULCES')
    print('B: MOSTRAR LOTES DE DULCES DISPONIBLES')
    print('C: EXTRAER FRASCOS DEL INVENTARIO')
    print('D: ELIMINAR LOTE COMPLETO')
    print('E: SALIR\n')


def add_lote(lotes:list[dict]):
    fruta = input('¿Qué dulce preparó? : ')
    tipo = input('¿Qué frasco utilizó? : ')
    capacidad = input('¿Qué capacidad tiene el frasco? : ')
    cantidad = int(input('¿Cuántos frascos preparó? : '))
    año_de_produccion = int(input('¿Año de producción? : '))
    tiempo_de_almacenamiento = 'Produccion.tiempo_de_almacenamiento'
    new_lote = {
        'Fruta':fruta, 
        'Frasco':tipo, 
        'Capacidad':capacidad, 
        'Cantidad':cantidad, 
        'Año':año_de_produccion, 
        'Tiempo':tiempo_de_almacenamiento}
    
    i = len(lotes)
    print(f'Usted agregó un nuevo lote:'+'\n')
    print(f'==== Lote {i+1} ====')

    for key, value in new_lote.items():
        print(f'{key}:{value}')
    lotes.append(new_lote)


def update_lote(lotes:list[dict]):
    show_lotes(lotes)
    print('\n')
    to_update = int(input('¿Qué lote desea modificar? : ')) - 1
    print('Usted va a modificar el siguiente lote:')
    print(f'==== Lote {to_update+1} ====')

    for key, value in lotes[to_update].items():
        print(f'{key}:{value}')

    print('\n')
    extraidos = int(input('¿Cuántos frascos va a extraer? : '))
    print('\n')
    print(f'Usted tenía {lotes[to_update]['Cantidad']} frascos disponibles en el lote {to_update+1}.')
    lotes[to_update]['Cantidad'] -= extraidos #lotes[to_update]['Cantidad'] = lotes[to_update]['Cantidad'] - extraidos
    print(f'Usted tiene ahora {lotes[to_update]['Cantidad']} frascos disponibles en el lote {to_update+1}.')


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
    to_delete = int(input('¿Qué lote desea eliminar? : ')) - 1
    print(f'Usted va a eliminar el siguiente lote:')
    print(f'==== Lote {to_delete+1} ===='+'\n')

    for key, value in lotes[to_delete].items():
        print(f'{key}:{value}')


    deleted = lotes.pop(to_delete)
    print(f'Lote {to_delete+1} : Dulce de {deleted['Fruta']} - Año {deleted['Año']} eliminado.')


def main():
    lotes = []

    while True:
        menu()
        choosed = input('¿Qué operación deseas realizar? ').upper()
        match choosed:
            case 'A':
                #clear_screen()
                add_lote(lotes)
            case 'B':
                #clear_screen()
                show_lotes(lotes)
            case 'C':
                #clear_screen()
                update_lote(lotes)
            case 'D':
                #clear_screen()
                delete_lote(lotes)
            case 'E':
                #clear_screen()
                print('\n*** ==== INVENTARIO DE DULCES APAGADO=== ***\n')
                break               
            case _ :
                #clear_screen()
                print('No ingresó una opción válida.\nIngrese una opción válida.')
                continue

        #option = get_option() #input('\n ¿Desea realizar otra operación? ')
        #if option == 'S':
        #    clear_screen()
        #    continue
        #elif option == 'N':
        #    clear_screen()
        #    ask_delete()
        #    print('\n*** ==== INVENTARIO DE DULCES APAGADO=== ***\n')
        #    break


if __name__ == '__main__':
    print('******************************'+'\n'+'==== INVENTARIO DE DULCES ===='+'\n'+'******************************')
    main()
