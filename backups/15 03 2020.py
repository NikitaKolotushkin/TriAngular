######################################
#  THIS PROGRAM IS MADE BY RENSYS   # 
#####################################

# INITIALISATION AND IMPORT SECTION
from colorama import Fore, init

init()

# WELCOME TEXT'S
print(Fore.GREEN + """ 
 ______   _______  _        _______           _        _______  _______ 
/ ___  \ (  ___  )( (    /|(  ____ \|\     /|( \      (  ___  )(  ____ )
\/   \  \| (   ) ||  \  ( || (    \/| )   ( || (      | (   ) || (    )|
   ___) /| (___) ||   \ | || |      | |   | || |      | (___) || (____)|
  (___ ( |  ___  || (\ \) || | ____ | |   | || |      |  ___  ||     __)
      ) \| (   ) || | \   || | \_  )| |   | || |      | (   ) || (\ (   
/\___/  /| )   ( || )  \  || (___) || (___) || (____/\| )   ( || ) \ \__
\______/ |/     \||/    )_)(_______)(_______)(_______/|/     \||/   \__/""")

print(Fore.WHITE + """

                      A
                     /|
                    / |
                   /  |
                  /   |
                 /    |
                /     |
               /      |
              /       |
             /       _|
            /_______|_| 
           B           C  
   
   """)


# DEF'S SECTION
def Exit():
   print(Fore.BLUE + 'Нажмите Enter для выхода: ' + Fore.WHITE)

   exit = input('')

   if exit == '':
      print()
   else:
      Exit()

def Continue():
   print(Fore.GREEN + 'Что вы хотите сделать?' + Fore.WHITE)
   print('1. Продолжить решать')
   print('2. Выход')
   Contin = input('Введите номер пункта: ')
   if Contin.isdigit() == True:

      Contin = int(Contin)

      if Contin == 1:
         Questions()    
      elif Contin == 2:
         Exit()
      else:
         print(Fore.RED + 'Ошибка! Такого пункта нет!' + Fore.WHITE)
         Continue()

   else:
      print(Fore.RED + 'Неверный ввод!' + Fore.WHITE)
      Continue()
   
# QUESTIONS SECTION 
def Questions():
   print('\t Что вы хотите сделать?\n')
   print('1. Найти площадь прямоугольного треугольника')
   print('2. Найти площадь произвольного треугольника')
   print('3. Найти синус угла в прямоугольном ▲')
   print('4. Найти косинус угла в прямоугольном ▲')
   print('5. Найти тангенс угла в прямоугольном ▲')
   print('6. Найти котангенс угла в прямоугольном ▲')
   print('7. Проверить, существует ли треугольник')
   print(Fore.RED + '\n8. Выход из программы' + Fore.WHITE)

   print(Fore.GREEN + "Введите номер пункта: " + Fore.WHITE)
   action = input('')

# MAIN LOGIC SECTION
   if action.isdigit() == True:

      action = int(action)

      # FINDING THE AREA OF 90 DEGREES TRIANGLE
      # FORMULA - 1/2 * A * B
      if action == 1:
         print(Fore.YELLOW + '\t Площадь прямоугольного треугольника' + Fore.WHITE)
         def area_90_degrees():
            first_side  = input('Введите длину первого катета (только число): ')
            second_side = input('Введите длину второго катета (только число): ')

            if (first_side.isdigit() == True) and (second_side.isdigit() == True):
               print(Fore.CYAN + 'Ответ:' + Fore.WHITE, 0.5 * int(first_side) * int(second_side), '\n')
               Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               area_90_degrees()
         area_90_degrees()

      # FINDING THE AREA OF ARBITRARY TRIANGLE 
      # FORMULA - 1/2 * A * hA
      elif action == 2:
         print(Fore.YELLOW + '\t Площадь произвольного треугольника' + Fore.WHITE)
         def area_arbitrary():
            base_length = input('Введите длину стороны, к которой проведена высота: ')
            height      = input('Введите длину высоты, проведенной к указанной стороне: ')

            if (base_length.isdigit() == True) and (height.isdigit() == True):
               print(Fore.CYAN + 'Ответ:' + Fore.WHITE, 0.5 * int(*base_length) * int(height),'\n')
               Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               area_arbitrary()
         area_arbitrary()

      # FINDING A SINUS 
      # FORMULA - AGAINIST CATHETUS / HYPOTENUSE
      elif action == 3:
         print(Fore.YELLOW + '\t Нахождение синуса угла в прямоугольном ▲' + Fore.WHITE)
         def sinus():
            againist_cathetus    = input('Введите длину противолежащего катета: ')
            hypotenuse           = input('Введите длину гипотенузы: ')

            if (againist_cathetus.isdigit() == True) and (hypotenuse.isdigit() == True):
               print(Fore.CYAN + 'Ответ: ' + Fore.WHITE, int(againist_cathetus) / int(hypotenuse), '\n')
               Continue()
            
            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               sinus()
         sinus()

      # FINDING A COSINUS
      # FORMULA - ADJOINED CATHETUS / HYPOTENUSE
      elif action == 4:
         print(Fore.YELLOW + '\t Нахождение косинуса угла в прямоугольном ▲' + Fore.WHITE)
         def cosinus():
            adjoined_cathetus = input('Введите длину прилежащего катета: ')
            hypotenuse        = input('Введите длину гипотенузы: ')

            if (adjoined_cathetus.isdigit() == True) and (hypotenuse.isdigit() == True):
               print(Fore.CYAN + 'Ответ: ' + Fore.WHITE, int(adjoined_cathetus) / int(hypotenuse), '\n')
               Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               cosinus()
         cosinus()

      # FINDING A TANGENT
      # FORMULA - AGAINIST CATHETUS / ADJOINED CATHETUS 
      elif action == 5:
         print(Fore.YELLOW + '\t Нахождение тангенса угла в прямоугольном ▲' + Fore.WHITE)
         def tangent():
            againist_cathetus = input('Введите длину противолежащего катета: ')
            adjoined_cathetus = input('Введите длину прилежащего катета: ')

            if (againist_cathetus.isdigit() == True) and (adjoined_cathetus.isdigit() == True):
               print(Fore.CYAN + 'Ответ: ' + Fore.WHITE, int(againist_cathetus) / int(adjoined_cathetus), '\n')
               Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               tangent()
         tangent()
      
      # FINDING A COTANGENT  
      # FORMULA - ADJOINED CATHETUS / AGAINIST CATHETUS  
      elif action == 6:
         print(Fore.YELLOW + '\t Нахождение котангенса угла в прямоугольном ▲' + Fore.WHITE)
         def cotangent():
            adjoined_cathetus = input('Введите длину прилежащего катета: ')
            againist_cathetus = input('Введите длину противолежащего катета: ')

            if (adjoined_cathetus.isdigit() == True) and (againist_cathetus.isdigit() == True):
               print(Fore.CYAN + 'Ответ: ' + Fore.WHITE, int(adjoined_cathetus) / int(againist_cathetus), '\n')
               Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               cotangent()
         cotangent()

      # EXISTENCE OF A TRIANGLE
      # IF THE BIG PARTY IS LESS THAN THE AMOUNT OF TWO OTHER PARTIES, A TRIANGLE EXIST
      elif action == 7:
         print(Fore.YELLOW + '\t Проверка, существует ли треугольник' + Fore.WHITE)
         def existence():
            e = []

            first_side  = input('Введите длину первой стороны: ')
            second_side = input('Введите длину второй стороны: ')
            third_side  = input('Введите длину третьей стороны: ')

            if (first_side.isdigit() == True) and (second_side.isdigit() == True) and (third_side.isdigit() == True):
               e.append(int(first_side))
               e.append(int(second_side))
               e.append(int(third_side))

               first_side  = int(first_side)
               second_side = int(second_side)
               third_side  = int(third_side)

               if second_side == max(e):
                  if second_side > (first_side + third_side):
                     print(Fore.GREEN + 'Треугольник существует!' + Fore.WHITE)
                     Continue()

                  else:
                     print(Fore.RED + 'Треугольник не существует!' + Fore.WHITE)
                     Continue()

               else:
                  if max(e) > (second_side + min(e)):
                     print(Fore.GREEN + 'Треугольник существует!' + Fore.WHITE)
                     Continue()

                  else:
                     print(Fore.RED + 'Треугольник не существует!' + Fore.WHITE)
                     Continue()

            else:
               print(Fore.RED + 'Где-то ошибка!' + Fore.WHITE)
               existence()
         existence()

      # JUST EXIT, NO MORE...
      elif action == 8:
         Exit()

      else:
         print(Fore.RED + 'Ошибка! Такого пункта нет \n' + Fore.WHITE)
         Questions()
   else:
      print(Fore.RED + 'Ошибка! Нужно указать номер пункта\n' + Fore.WHITE)
      Questions()

Questions()