print("Bienvenido al simulador")
leds = {"led0":0,"led1":0,"led2":0,"led3":0}
def nums(i):
    switcher = {
        0: leds = {"led0":0,"led1":0,"led2":0,"led3":0},
        1: leds = {"led0":0,"led1":0,"led2":0,"led3":1},
        2: leds = {"led0":0,"led1":0,"led2":1,"led3":0},
        3: leds = {"led0":0,"led1":0,"led2":1,"led3":1},
        4: leds = {"led0":0,"led1":1,"led2":0,"led3":0},
        5: leds = {"led0":0,"led1":1,"led2":0,"led3":1},
        6: leds = {"led0":0,"led1":1,"led2":1,"led3":0},
        7: leds = {"led0":0,"led1":1,"led2":1,"led3":1},
        8: leds = {"led0":1,"led1":0,"led2":0,"led3":0},
        9: leds = {"led0":1,"led1":0,"led2":0,"led3":1},
    }
leds = {"led0":0,"led1":0,"led2":0,"led3":0}
while true:
    i=0
    for i in range(0,10):
        while button == 0:
            print("Escribir 1 para accionar el pulsador")
            button = input("Pulsador:")
        leds = {"led0":0,"led1":0,"led2":0,"led3":0}
        num(i)
        print(leds[0] + leds[1] + leds[2] + leds[3])