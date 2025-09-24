class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        num = list(self.card_num.replace(' ', '')[::-1])
        
        if len(num) <= 1:
            return False
        for i in range(0,len(num)):
            if not num[i].isdigit():
                return False
            else:
                num[i] = int(num[i])

                

        for i in range(1,len(num),2):
            if num[i] * 2 > 9:
                num[i] = num[i]* 2 - 9
            else:
                num[i] = num[i] * 2

        return sum(num) % 10 == 0