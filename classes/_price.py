from copy import deepcopy
class Price :
    def __init__(self, value) :
        self.__value = int(value) if isinstance(value, int) else None
    
    def to_string(self) :
        return "Rp{},00".format(self.__value) if self.__value is not None else "Rp0,00"