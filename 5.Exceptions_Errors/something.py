class NegativeNumberError(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if age < 0:
            print("This is not a valid age.")

def enter_age(age):
    if age < 0:
        raise NegativeNumberError(age) # 主動引發 except，表示遇到需要特別處理的狀況，希望透過引發 except 來結束流程並進行錯誤處理。
    if age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age a odd.")
