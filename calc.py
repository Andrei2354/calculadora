class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        if self.numero2 == 0:
            return "Error: No se puede dividir por cero. "
        else:
            return self.numero1 / self.numero2