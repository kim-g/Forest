import ProgramInterface

class Region(ProgramInterface.Window):
    '''Базовый класс области'''
    def __init__(self):
        super().__init__(np.array([(monitor_info.current_w-width) / 2, (monitor_info.current_h-height) / 2]), np.array([width, height]))
        self._max:int = 0
        self._number:float = 0.
        self._a:float = 0.

    @property
    def Max(self):
        '''Максимальное количество особей, которое может выдержать среда'''
        return self._max
    @Max.setter
    def Max(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Max')
            else:
                self._max = int(value)
        except:
            print('Недопустимое значение Pegions.Max')

    @property
    def Number(self):
        '''Количество особей на данный момент'''
        return int(self._number)
    @Number.setter
    def Number(self, value):
        try:
            if value < 0:
                print('Недопустимое значение Regions.Number')
                return
            if value == 0:
                self.kill()
                return
            self._number = float(value)
        except:
            print('Недопустимое значение Regions.Number')

    @property
    def A(self):
        '''Удельный прирост'''
        return self._a
    @A.setter
    def A(self, value):
        try:
            self._a = float(value)
        except:
            print('Недопустимое значение Regions.A')
        
