from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase

class Character:
    def __init__(self, model_path, position=Point3(0, 0, 0)):
        self.model_path = model_path
        self.position = position
        self.model = None

    def load_model(self, base):
        """بارگذاری مدل کاراکتر"""
        self.model = base.loader.loadModel(self.model_path)
        self.model.setScale(0.5)  # تنظیم مقیاس مدل (اختیاری)
        self.model.setPos(self.position)  # تنظیم موقعیت مدل
        self.model.reparentTo(base.render)  # قرار دادن مدل در صحنه بازی

    def set_position(self, position):
        """تنظیم موقعیت جدید برای کاراکتر"""
        self.position = position
        if self.model:
            self.model.setPos(self.position)

    def move_character_up(self):
        """حرکت کاراکتر به سمت بالا"""
        new_position = self.position + Point3(0, 1, 0)
        self.set_position(new_position)

    def move_character_down(self):
        """حرکت کاراکتر به سمت پایین"""
        new_position = self.position - Point3(0, 1, 0)
        self.set_position(new_position)

# کلاس اصلی بازی
class GameApp(ShowBase):
    def __init__(self):
        super().__init__()

        # ایجاد یک کاراکتر جدید و لود کردن مدل
        self.character = Character("models/player.glb")
        self.character.load_model(self)

        # تنظیمات دوربین
        self.camera.setPos(0, -10, 3)
        self.camera.lookAt(self.character.model)

        # کنترل حرکت کاراکتر
        self.accept("w", self.character.move_character_up)
        self.accept("s", self.character.move_character_down)

# شروع بازی
app = GameApp()
app.run()