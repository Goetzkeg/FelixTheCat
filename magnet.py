"""Provide functions to control magnet arm"""
from machine import Pin
from time import sleep


class Magnet:
    """Represent magnet Arm."""

    def __init__(self, magnet_pin, duration= 2, sleep_after_wave = 3) -> None:
        """duraton in seconds, sleep after waving in seconds to prevent overwinking"""

        self.magnet_pin = magnet_pin
        self.duration = duration
        self.sleep_after_wave = sleep_after_wave

        self.p_out = Pin(magnet_pin, Pin.OUT)

    def wave(self):
        self.p_out.value(1)
        sleep(self.duration)
        self.p_out.value(0)
        sleep(self.sleep_after_wave)
