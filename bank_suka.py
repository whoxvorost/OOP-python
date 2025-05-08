class BankAccount:
    def __init__(self, accreator = 'name'):
        self.__balance = 0
        self.accreator = accreator
        self.__history = []
        
    def up_balance(self,howmany):
        self.__balance = self.__balance + howmany
        self.__history.append(f"Закинув {howmany}")
        return howmany   
        
    def down_balance(self,howmany):
        if self.__balance - howmany < 0:
            raise ValueError('NO MONEY')
        self.__balance = self.__balance - howmany
        self.__history.append(f"Зняв {howmany}")
        return howmany
    
    def show_history(self):
        print(f"Історія {self.accreator} : ")
        for h in self.__history:
            print(" -",h)
        
    def info(self):
        print (f"{self.accreator} :" , self.__balance)
        return self.__balance
    
    
    
x = BankAccount('Nazarii')
y = BankAccount('Volodya')


x.up_balance(100)
y.up_balance(100)


y.up_balance(x.down_balance(20))
x.up_balance(y.down_balance(30))


x.show_history()
y.show_history() 

       
print(x.info())
print(y.info())