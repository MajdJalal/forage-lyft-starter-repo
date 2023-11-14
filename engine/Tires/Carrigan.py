import Tires

class Carrigan(Tires):
    def needs_service(self, array):
        for val in array:
            if val >= 0.9:
                return True
        return False