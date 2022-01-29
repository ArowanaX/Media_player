
mediaList = []


class IMedia:

    def __init__(self,location:str,name:str,rate:int):
        self.location = location
        self.name = name
        self.rate = rate


    def __str__(self):
        return self.name


class Web_Media(IMedia):
    pass


class Local_Media(IMedia):
    pass







