from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor

tank = MoveTank(OUTPUT_A, OUTPUT_B)
color = ColorSensor(INPUT_1)

tank.on(30, 30)

while color.reflected_light_intensity > 20:
    pass

tank.off()
