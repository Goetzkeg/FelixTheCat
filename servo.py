"""Provide Servo functions."""
from time import sleep
from machine import Pin, PWM


class Servo:
    """Represent a Servo."""

    def __init__(self, pin, back = 50, front = 100, middle = 75, pause = 0.2) -> None:
        self.pin = pin
        self.back = back
        self.front = front
        self.middle = middle
        self.pause = pause

    def wave(self):
        """Wave arm."""
        servo = PWM(Pin(self.pin), freq=50, duty=self.middle)
        sleep(self.pause)  # might move to middle
        servo.duty(self.front)
        sleep(self.pause)  # move to front
        servo.duty(self.back)
        sleep(3 * self.pause)  # move to back
        servo.duty(self.front)
        sleep(3 * self.pause)  # move to front
        servo.duty(self.back)
        sleep(3 * self.pause)  # move to back
        servo.duty(self.middle)
        sleep(3 * self.pause)  # move to middle
        servo.deinit()
        Pin(self.pin, mode=Pin.IN)
