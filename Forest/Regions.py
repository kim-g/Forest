import ProgramInterface
class Region(ProgramInterface.Window):
    """Ѕазовый класс области"""

    def __init__(self, position, size):
        super().__init__(self, position, size) 
        self.Max=0
        self.Number=0
        self.A=0
    @property
    def Max(self):
        return self._max
    @Max.setter
    def Max(self,value):
        try:
            max=int(value)
            if self._max>=0:
                self._max = value
        except:
            print("явл€етс€ отрицательным числом")

    @property
    def Number(self):
        return int(self._number)
    @Number.setter
    def Number(self,value):
        try:
            max=float(value)
            if number>=0:
                self._Number = value
        except:
            pass


    @property
    def A(self):
        return self._a
    @A.setter
    def A(self,value):
        try:
            max=float(value)
        except:
            pass







