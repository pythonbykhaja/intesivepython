class Mobile:
    def dial(self, number):
        print(f"dialing number {number}")

    def ring(self):
        print("ringing using built in tones.....")

class SmartMobile(Mobile):

    def ring(self):
        """
        overriding a Method
        """
        print("ringing using custom ring tones .... ")