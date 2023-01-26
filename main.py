from machine import Pin, SPI, I2C
from ssd1306 import SSD1306_I2C
import time


class DISPLAY():
    def __init__(self):
        self.hspi = SPI(1)  # sck=14 (scl), mosi=13 (sda), miso=12 (unused)
        self.i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.inverted = 0  # 0 normal, 1 inverted
        self.rotated = False

    def _square(self, x, y, length):
        self.oled.vline(x, y, length, 1)
        self.oled.vline(x + length, y, length, 1)
        self.oled.hline(x, y, length, 1)
        self.oled.hline(x, y + length, length, 1)

    def anim(self, y):
        pad = 10
        length = 20
        change = False
        off_set = 20
        steps = 2
        for j in range(y, y + off_set):
            for i in range(0, 86, steps):
                self.oled.fill(0)
                x_1 = i
                if i < 20:
                    x_2 = i - 20
                elif i < 50:
                    x_2 = i
                elif i < 80:
                    x_2 = i + (i % 50)
                else:
                    x_2 = i
                y_1 = 5
                y_2 = y_1 - length

                self.oled.line(0, y_1 + length + pad, 128, y_1 + length + pad, 1)
                self.oled.text('-  -   -   -   -   -  -', 0, y_1 + 32, 1)
                self.oled.line(0, y_1 + length + 10 + pad, 128, y_1 + length + 10 + pad, 1)

                # City
                self._square(x_1 + 48, y_1 + 48, length)
                self._square(x_2 + 48, y_2 + 48, length)
                self.oled.line(x_2 + 48, y_2 + 48, x_2 + 48, y_2 + 48, 1)
                self.oled.line(x_1 + length + 48, y_1 + 48, x_2 + length + 48, y_2 + 48, 1)
                self.oled.line(x_1 + 48, y_1 + length + 48, x_2 + 48, y_2 + length + 48, 1)
                self.oled.line(x_1 + length + 48, y_1 + length + 48, x_2 + length + 48, y_2 + length + 48, 1)

                self._square(x_1 - 40, y_1 + 48, length)
                self._square(x_2 - 40, y_2 + 48, length)
                self.oled.line(x_2 - 40, y_2 + 48, x_2 - 40, y_2 + 48, 1)
                self.oled.line(x_1 + length - 40, y_1 + 48, x_2 + length - 40, y_2 + 48, 1)
                self.oled.line(x_1 - 40, y_1 + length + 48, x_2 - 40, y_2 + length + 48, 1)
                self.oled.line(x_1 + length - 40, y_1 + length + 48, x_2 + length - 40, y_2 + length + 48, 1)

                self._square(x_1 + 36, y_1, length)
                self._square(x_2 + 36, y_2, length)
                self.oled.line(x_2 + 36, y_2, x_2 + 20, y_2, 1)
                self.oled.line(x_1 + length + 36, y_1, x_2 + length + 36, y_2, 1)
                self.oled.line(x_1 + 36, y_1 + length, x_2 + 36, y_2 + length, 1)
                self.oled.line(x_1 + length + 36, y_1 + length, x_2 + length + 36, y_2 + length, 1)

                self._square(x_1 - 46, y_1, length)
                self._square(x_2 - 46, y_2, length)
                self.oled.line(x_2 - 46, y_2, x_2 - 46, y_2, 1)
                self.oled.line(x_1 + length - 46, y_1, x_2 + length - 46, y_2, 1)
                self.oled.line(x_1 - 46, y_1 + length, x_2 - 46, y_2 + length, 1)
                self.oled.line(x_1 + length - 46, y_1 + length, x_2 + length - 46, y_2 + length, 1)
                self.oled.show()
                time.sleep(0.06)

            change = not change

    def _load(self, load_cycles):
        for i in range(load_cycles):
            for j in range(0, 70):
                self.oled.hline(30, 30, j, 1)
                self.oled.show()

            for j in range(30, 100):
                self.oled.pixel(j, 30, 0)
                self.oled.show()
            time.sleep(0.05)


display = DISPLAY()
display._load(1)
switch = Pin(10, Pin.IN)
while True:
    if switch.value():
        display.anim(1)
