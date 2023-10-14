class Carp: #Carp = 붕어
    def __init__(self, name, material, price):
        self.name = name #붕어빵 이름
        self.material = material #붕어빵 재료
        self.price = price #붕어빵 가격
        self.total = 0 #총합 가격을 계산하기 위해서 지정해놓은 값

    def what(self):
        print(f"{self.name}에는 {self.material}이 들어갔습니다.")

    def sell(self):
        print(f"{self.name}이 {self.price}원에 판매되었습니다.")
        if self.name == "팥 붕어빵": #팥 붕어빵을 팔았을 때
            self.total += 500
        elif self.name == "슈크림 붕어빵": #슈크림 붕어빵을 팔았을 때
            self.total += 1000

    def eat(self):
        print(f"{self.name}을 먹었습니다")

팥 = Carp("팥 붕어빵", "팥", 500)
슈크림 = Carp("슈크림 붕어빵", "슈크림", 1000)
팥.what()
슈크림.what()
슈크림.sell()
슈크림.sell()
슈크림.sell()
슈크림.sell()
print(슈크림.total)
팥.sell()
팥.sell()
print(팥.total)
슈크림.eat()
팥.eat()
