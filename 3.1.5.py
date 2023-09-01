class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        self.check = [type(x) for x in self.apps]
        if type(app) not in self.check:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memorymax=1024):
        self.name = "YouTube"
        self.memorymax = memorymax


class AppPhone:
    def __init__(self, phone_list={"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}, name="Phone"):
        self.phone_list = phone_list
        self.name = name

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
    print(type(a.name))