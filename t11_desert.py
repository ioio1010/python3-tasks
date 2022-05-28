class Desert:
    def __init__(self, name, calories):
        self.__name = name
        self.__calories = calories

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_calories(self, calories):
        self.__calories = calories

    def get_calories(self):
        return self.__calories

    def is_healthy(self):
        if self.__calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True