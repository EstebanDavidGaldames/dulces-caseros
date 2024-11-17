from screen_helpers import clear_screen


frutas = ['Manzana', 'Pera', 'Uva', 'Durazno', 'Damasco', 'Ciruela', 'Melón', 'Sandía',
          'Frutilla', 'Frambuesa', 'Mora', 'Cereza', 'Limón', 'Higo', 'Ananá', 'Banana',
          'Naranja', 'Pomelo', 'Mandarina', 'Limón', 'Palta', 'Kiwi', 'Arándanos']

frascos_disponibles = {1:'Amanecer 360 cc', 2:'Campana 360 cc', 
                       3:'Hexagonal 190 cc', 4:'Hexagonal 360 cc', 
                       5:'Alba 800 cc', 6:'Jupiter 800 cc'}


def get_fruta() -> str:
    fruta_in = input('¿Qué dulce preparó? : ').strip().replace(' ', '').capitalize()
    
    if fruta_in in frutas:
        clear_screen()
        return f'{fruta_in}'
    else:
        clear_screen()
        print('No ingresó una fruta.'+'\n')
        get_fruta()


def get_frasco():
    print('==== Frascos ===='+'\n')
    
    for key, value in frascos_disponibles.items():
        print(f'{key} -> {value}')
    
    print('\n')
    try:
        tipo_de_frasco = int(input('¿Qué frasco utilizó? : ').strip().replace(' ', ''))
    
        if tipo_de_frasco in frascos_disponibles.keys():
            clear_screen()
            return f'{frascos_disponibles[tipo_de_frasco]}'
        else:
            clear_screen()
            print('No ingresó una opción válida.'+'\n')
            get_frasco()
    
    except ValueError:
        clear_screen()
        print('No ingresó una opción válida.'+'\n')
        get_frasco()


def get_cantidad():
    try:
        producidos = int(input('¿Cuántos frascos preparó? : ').strip().replace(' ', ''))
        clear_screen()
        return producidos
    except ValueError:
        clear_screen()
        print('No ingresó un número.'+'\n')
        get_cantidad()


def get_año():
    try:
        fecha_ingresada = int(input('¿En qué año se produjo el dulce? : ').strip().replace(' ', ''))
        
        if len(str(fecha_ingresada)) == 4:
            clear_screen()
            return fecha_ingresada
        else:
            clear_screen()
            print('No ingresó un año válido.'+'\n')
            get_año()

    except ValueError:
        clear_screen()
        print('No ingresó un número.'+'\n')
        get_año()
