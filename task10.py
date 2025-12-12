"""
Задача: (М. Попков) В волшебном лесу живет юный маг по имени Снежок. 
У Снежка есть три волшебных заклинания:
A: Призвать 1 снежинку (num = num + 1)
B: Призвать 2 снежинки (num = num + 2)
C: Увеличить количество снежинок в 2 раза (num = num * 2)

Снежок начал с 5 снежинок и мечтает собрать 25 снежинок, но ему нужно 
обязательно собрать 13 снежинок.

Сколько существует различных последовательностей заклинаний, которые помогут Снежку?

Ответ должен быть напечатан как одно число.
"""

ways = [0]* 25  * 2
ways[5] = 1

for i in range(5, 14):
    ways[i+1] += ways[i]
    ways[i+2] += ways[i]
    ways[i*2] += ways[i]

road200 = ways[13]

ways = [0]* 511 * 4
ways[13] = 1

for i in range(13, 26):
    ways[i+1] += ways[i]
    ways[i+2] += ways[i]
    ways[i*2] += ways[i]

print(road200 * ways[25])


#I don't know how to live through this hell
#Woken up, I'm still locked in this shell
#Frozen soul, frozen down to the core
#Break the ice, I can't take anymore
#
#Freezing, can't move at all
#Screaming, can't hear my call
#I am dying to live
#Cry out, I'm trapped under ice
