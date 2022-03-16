consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'costa': ('Guayaquil', 'Manta'),
 'sierra': ('Quito', 'Ambato', 'Loja'),
 'oriente': ('Tena', 'Nueva Loja')
}

costa = tot_coca_codo_g + tot_sopladora_g
sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
oriente = ('No existe registro de Planta en el oriente')

print('''
    ===============================
          PLANTAS ENERGETICAS
    ===============================
    ''')

opcion = -1
def menu():
    print('<1>. Total de megavatios en la Planta y la ciudad ')
    print('<2>. Total de energía por cada Ciudad ')
    print('<3>. Dinero recaudado por cada Región ')
    print('<4>. Opción para Salir del programa ')

while opcion != 0:
        menu()
        opcion = int(input('Escoga una opción: '))

    #1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
    # megavatios de consumos para dicha ciudad en dicha planta
        if opcion == 1 :
    
            print('''
            ===============================
                    TOTAL DE MEGAVATIOS
                      PLANTAS:
            Coca Codo Sinclair, Sopladora
                    CIUDADES:
            Guayaquil, Quito, Loja
            ===============================
            ''')

            n_planta = input('Digite el nombre de la planta: ')

            if n_planta == 'Coca Codo Sinclair':
                n_ciudad = input('Digite el nombre de la ciudad: ')

                if n_ciudad == 'Quito':
                    print('Total de megavatios cosumidos en Coca Codo Sinclair, Quito: ', tot_coca_codo_q, 'Megavatios')
                    print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
                elif n_ciudad == 'Guayaquil':
                    print('Total de Megavatios consumidos en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'Megavatios')
                    print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
                elif n_ciudad =='Loja':
                    print("No existe registro de Planta de Coca Codo Sinclair en Loja")
                else:
                    print('No existe, digite correctamente')
            


            if n_planta == 'Sopladora':
                n_ciudad = input('Digite el nombre de la ciudad: ')

                if n_ciudad == 'Quito':
                    print('Total de Megavatios consumidos en Sopladora, Quito: ', tot_sopladora_q, 'Megavatios')
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
                elif n_ciudad == 'Guayaquil':
                    print('Total de Megavatios consumidos en Sopladora, Guayaquil: ', tot_sopladora_g, 'Megavatios')
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
                elif n_ciudad == 'Loja':
                    print('Total de Megavatios consumidos en Sopladora, Loja: ', tot_sopladora_l)
                    print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
                else:
                    print("Digito mal, por favor intente de nuevo")

            # exit
    


 
        #2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
        # son los nombres de las plantas generadoras y el valor es el total megavatios que cada
        # planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
        # no debería aparecer en el nuevo diccionario  

        elif opcion == 2:
            print('''
            ===============================
            TOTAL DE ENERGIA DADA A CADA
                CIUDAD POR CADA PLANTA

            Digite como se le muestra, para 
            adquirir informacion de la ciudad:
            Guayaquil
            Quito
            Loja
            Ambato
            Tena
            Nueva loja
            ===============================
            '''),

            n_ciudad2 = input('Digite el nombre de la ciudad: ')

            if n_ciudad2 == 'Guayaquil':
                print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_g, 'Megavatios')
                print('Total de Megavatios, Sopladora:', tot_sopladora_g, 'Megavatios')
            elif n_ciudad2 == 'Quito':
                print('Total de Megavatios, Coca Codo Sinclair: ', tot_coca_codo_q, 'Megavatios')
                print('Total de Megavatios, Sopladora:', tot_sopladora_q, 'Megavatios')
            elif n_ciudad2 == 'Loja':
                print('Total de MMegavatios, Sopladora:', tot_sopladora_l, 'Megavatios')
            else:
                print('Ninguna planta proporciona energía a la ciudad seleccionada')
            print()

            # exit



        #3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
        # región
        elif opcion == 3:
            print('''
            ===============================
            DINERO RECAUDADO DE CADA REGION
            Digite así para adquirir información:
            Costa
            Sierra
            Oriente
            ===============================
            '''),

            n_region = input('Digite nombre de la región: ')

            if n_region == 'Costa':
                print('Total de recaudadación en la región Costa: ', costa, '$')
            elif n_region == 'Sierra':
                print('Total de recaudación en la región Sierra: ', sierra, '$')
            elif n_region == 'Oriente':
                print(oriente)
            else:
                print("Digite adecuadamente la primera en mayuscula")

        elif opcion == 4:
            print('Gracias por su cooperación')
            quit()
