from machine import Pin, PWM
from time import sleep

frequency = 5000
led = PWM(Pin(18), frequency)

while True:
  for duty_cycle in range(0,1024):
    led.duty(duty_cycle)
    sleep(0.005)

