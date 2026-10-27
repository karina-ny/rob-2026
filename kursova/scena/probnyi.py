from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
import time
import random

tank = MoveTank(OUTPUT_A, OUTPUT_B)
color = ColorSensor(INPUT_1)
time.sleep(0.5)

pochatok = time.time()
while time.time() - pochatok < 30:
    v = color.reflected_light_intensity + random.randint(-8, 8)
    # поки просто їдемо прямо; v вже «шумний»
    tank.on(SpeedPercent(30), SpeedPercent(30))
    time.sleep(0.1)

tank.off()
print("час: %.1f с" % (time.time() - pochatok))
print("останній v з шумом:", v)
