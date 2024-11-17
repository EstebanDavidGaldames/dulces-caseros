#from datetime import datetime

from models.lote_model import Lote
from screen_helpers import clear_screen, menu, get_option
from core.data_input import get_fruta, get_frasco, get_cantidad, get_año #, get_tiempo


class LoteController:

    @classmethod
    def start(cls):
        Lote.load()
        clear_screen()
        while True:
            menu()
            choosed = input('¿Qué operación deseas realizar? ').upper()
            match choosed:
                case 'A':
                    clear_screen()
                    cls.add_lote()
                case 'B':
                    clear_screen()
                    cls.show_lotes()
                case 'C':
                    clear_screen()
                    cls.update_lote()
                case 'D':
                    clear_screen()
                    cls.delete_lote()
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
                print('\n*** ==== INVENTARIO DE DULCES APAGADO ==== ***\n')
                break

    
    @classmethod
    def add_lote(cls):
        fruta = get_fruta()
        frasco = get_frasco()
        cantidad = get_cantidad()
        año = get_año()
        #tiempo = get_tiempo()
        new_lote = Lote(fruta, frasco, cantidad, año)
        i = len(Lote.all)
        print(f'\n'+'Usted agregó un nuevo lote:'+'\n')
        print(f'====== Lote {i+1} ======')
        
        for key, value in new_lote.__dict__.items():
            print(f'{key.capitalize()} : {value}')

        #lotes.append(new_lote)
        Lote.all.append(new_lote)

        #write_json_file(INVENTARIO_PATH, lotes)
        Lote.save()

    @classmethod
    def show_lotes(cls):

        if Lote.all != []:
            print('Usted posee los siguientes lotes:'+'\n')
            
            for i, lote_obj in enumerate(Lote.all, start=1):
                print(f'====== Lote {i} ======')

                for key, value in lote_obj.__dict__.items():
                    print(f'{key.capitalize()} : {value}')

                '''
                print(f'{lote_obj.fruta}')
                print(f'{lote_obj.tipo}')
                print(f'{lote_obj.cantidad}')
                print(f'{lote_obj.año}')
                print(f'{lote_obj.tiempo}')
                '''
            # PASANDO Lote a diccionaro:
            #n = 1
            #for lote_obj in Lote.all:
            #    print(f'==== LOTE {n} ====')
            #    for key, value in lote_obj.__dict__.items():
            #        print(f'{key}:{value}')
            #    n += 1
    
            print('\n')
        else:
            print('Usted no posee ningún lote en el sistema.'+'\n')

    @classmethod
    def update_lote(cls):
        cls.show_lotes()
        while Lote.all != []:
            print('\n')
            try:
                to_update = int(input('¿Qué lote desea modificar? : ')) - 1

                if to_update >= 0 and to_update <= len(Lote.all):
                    clear_screen()
                    print('\n'+'Usted va a modificar el siguiente lote:'+'\n')
                    print(f'====== Lote {to_update+1} ======')

                    for key, value in Lote.all[to_update].__dict__.items():
                        print(f'{key.capitalize()} : {value}')

                    print('\n')

                    while True:
                        try:
                            extraidos = int(input('¿Cuántos frascos va a extraer? : '))
                            if extraidos >= 0 and extraidos <= Lote.all[to_update].__dict__['cantidad']:
                                print('\n')
                                print(f'Usted tenía {Lote.all[to_update].__dict__['cantidad']} frascos disponibles en el lote {to_update+1}.')
                                Lote.all[to_update].__dict__['cantidad'] -= extraidos
                                print(f'Ahora tiene {Lote.all[to_update].__dict__['cantidad']} frascos disponibles en el lote {to_update+1}.')
                                
                                #write_json_file(INVENTARIO_PATH, lotes)
                                Lote.save()
                                break
                            else:
                                print('No ingresó una cantidad válida.'+'\n')
                        except ValueError:
                            print('No ingresó un número válido.'+'\n')
                    break
                else:
                    clear_screen()
                    print('No ingresó un número de lote válido.'+'\n')
       
            except ValueError:
                clear_screen()
                print('No ingresó un número válido.'+'\n')

    @classmethod
    def delete_lote(cls):
        cls.show_lotes()
        if Lote.all != []:
            try:
                to_delete = int(input('¿Qué lote desea eliminar? : ')) - 1
                if to_delete >=0 and to_delete <= len(Lote.all):
                    print(f'\n'+'Usted seleccionó eliminar el siguiente lote:'+'\n')
                    print(f'==== Lote {to_delete+1} ===='+'\n')

                    for key, value in Lote.all[to_delete].__dict__.items():
                        print(f'{key.capitalize()} : {value}')

                    deleted = Lote.all.pop(to_delete)
                    print('\n')
                    print(f'Lote {to_delete+1} : Dulce de {deleted.__dict__['fruta']} - Año {deleted.__dict__['año']} eliminado.')
                    #write_json_file(INVENTARIO_PATH, lotes)
                    Lote.save()

                else:
                    clear_screen()
                    print('No ingresó un número de lote válido.'+'\n')
                    cls.delete_lote()

            except ValueError:
                clear_screen()
                print('No ingresó un número válido.'+'\n')
                cls.delete_lote()
        else:
            pass

    #@property
    #def tiempo_de_almacenamiento(self):
    #   hoy = datetime.now()
    #    año_actual = hoy.year
    #    return (año_actual - self.año_de_produccion)
