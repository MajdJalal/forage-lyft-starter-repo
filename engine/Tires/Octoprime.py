import sys
sys.path.append('C:\\Users\\PC\\Desktop\\forage-lyft-starter-repo')
from engine.Tires.Tires import Tires

class Octoprime(Tires):
    def needs_service(self, array):
        sum = 0
        for val in array:
            sum += val
        return (sum >= 3)