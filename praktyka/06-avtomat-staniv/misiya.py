from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import UltrasonicSensor
import time

tank = MoveTank(OUTPUT_A, OUTPUT_B)
ultra = UltrasonicSensor(INPUT_2)
time.sleep(0.5)

stan = "poshuk"
vkhid = time.time()

def perekhid(novyi):
    global stan, vkhid
    print(f"{stan} -> {novyi}")
    stan = novyi
    vkhid = time.time()

while stan != "gotovo":
    d = ultra.distance_centimeters

    if stan == "poshuk":
        tank.on(SpeedPercent(30), SpeedPercent(30))
        if d < 45:
            perekhid("pidhid")

    elif stan == "pidhid":
        tank.on(SpeedPercent(10), SpeedPercent(10))
        if d < 15:
            perekhid("signal")

    elif stan == "signal":
        tank.off()
        if time.time() - vkhid > 1:
            perekhid("gotovo")

    if time.time() - vkhid > 20:
        print("таймаут у стані", stan)
        tank.off()
        break

print("місію завершено")
