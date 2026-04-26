from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window

class Car(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 0
        self.fuel = 100
        self.brake = False
        self.pos = (200, 100)
        self.size = (60, 100)

class CarGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.car = Car()
        self.add_widget(self.car)
        Clock.schedule_interval(self.update, 1/60)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.car.speed = min(self.car.speed + 1, 10)
        if keycode[1] == 'down':
            self.car.brake = True
        if keycode[1] == 'left':
            self.car.x -= 10
        if keycode[1] == 'right':
            self.car.x += 10

    def _on_key_up(self, keyboard, keycode):
        if keycode[1] == 'down':
            self.car.brake = False

    def update(self, dt):
        if self.car.brake:
            self.car.speed = max(self.car.speed - 0.5, 0)
        if self.car.speed > 0:
            self.car.fuel = max(self.car.fuel - 0.1, 0)
        self.car.y += self.car.speed

class CarGameApp(App):
    def build(self):
        return CarGame()

if __name__ == '__main__':
    CarGameApp().run()
