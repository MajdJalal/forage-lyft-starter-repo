import Tires

class Octoprime(Tires):
    def needs_service(self, array):
        sum = 0
        for val in array:
            sum += val
        return (sum >= 3)