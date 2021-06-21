class Mobile:
    # class attribute
    count = 0

    def __init__(self, model, manufacturer):
        # instance attribute
        self.model = model
        self.manufacturer = manufacturer
        Mobile.count += 1

    def dail(self, number):
        # instance
        print(f"dailing from {self.model} to {number}")

    @classmethod
    def count_info(cls):
        print(cls.count)

iphone = Mobile(model='12 PRO', manufacturer='apple')
iphone.dail('9999999999')
Mobile.count_info()

oneplus = Mobile(model='One plus 9', manufacturer='one plus')
oneplus.dail('888888888')
Mobile.count_info()