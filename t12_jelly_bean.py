from t11_desert import Desert


class JellyBean(Desert):
    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.__flavor = flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def is_healthy(self):
        if self.get_calories() < 200:
            return True
        else:
            return False

    def is_delicious(self):
        if self.__flavor == "black licorice":
            return False
        else:
            return True
