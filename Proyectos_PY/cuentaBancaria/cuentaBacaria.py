class Persona():
    
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):

    def __init__(self,  nombre, apellido,numeroCuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numeroCuenta = numeroCuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numeroCuenta}: ${self.balance}"

    def depositar(self,monto_deposito):
        self.monto_deposito = monto_deposito
        if(monto_deposito<0):
            print("No puede hacer depositos inferiores a 0")
        else:
            self.balance += monto_deposito
            print ("Se realizo deposito correctamente")
            print (f"Su nuevo balance es de: {self.balance}")
   
   
    def retirar(self,monto_retiro):
        self.monto_retiro = monto_retiro
        if(monto_retiro>self.balance):
            print(f"No puede retirar un monto superior a su balance {self.balance}")
        else:
            self.balance -= monto_retiro
            print ("Se realizo deposito correctamente")
            print (f"Su nuevo balance es de: {self.balance}")
    
def crear_cliente():
    nombre=input("Ingrese su nombre: ")
    apellido=input("Ingrese su apellido: ")
    numeroCuenta=input("Ingrese el numero de su cuenta: ")
    cliente=Cliente(nombre, apellido, numeroCuenta)
    return cliente

def es_numerico(cadena):
    try:
         int(cadena)
         return True
    except ValueError:
         return False

def inicio():

    mi_cliente=crear_cliente()
    print(mi_cliente)
    opcion=0

    while opcion != 3:
        
        opcion=int(input('''Elije una opción: 
        [1] - Depositar 
        [2] - Retirar 
        [3] - Salir 
        ->  '''))
        
       

        if opcion == 1:
                monto_deposito= int(input("Ingrese monto del deposito que realizará: "))
                mi_cliente.depositar(monto_deposito)
        elif opcion == 2:
                monto_retiro=int(input("Ingrese monto del retiro: "))
                mi_cliente.retirar(monto_retiro)
        
            
    
    print("Gracias por usar Banco Python")

inicio()
        