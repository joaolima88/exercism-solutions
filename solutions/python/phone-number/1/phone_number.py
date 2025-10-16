class PhoneNumber:
    def __init__(self, number):

        punc = "-@:!-"
        punc_counter = 0
        number_counter = 0

        for i in number:
            if i.isalpha():
                raise ValueError("letters not permitted")

        for i in number:
            if i in punc:
                punc_counter += 1
            if i.isdigit():
                number_counter += 1

        if punc_counter > 3 and number_counter < 10:
            raise ValueError("punctuations not permitted")
        else:
            self.number = ''.join([i for i in number if i.isdigit()])
            if number_counter < 10:
                raise ValueError("must not be fewer than 10 digits")
            elif number_counter > 11:
                raise ValueError("must not be greater than 11 digits")
            elif number_counter == 11 and self.number[0] != '1':
                raise ValueError("11 digits must start with 1")

            elif number_counter == 10:
                if self.number[3] == '0':
                    raise ValueError("exchange code cannot start with zero")
                elif self.number[3] == '1':
                    raise ValueError("exchange code cannot start with one")
                elif self.number[0] == '0':
                    raise ValueError("area code cannot start with zero")
                elif self.number[0] == '1':
                    raise ValueError("area code cannot start with one")

            elif number_counter == 11:
                if self.number[4] == '0':
                    raise ValueError("exchange code cannot start with zero")
                elif self.number[4] == '1':
                    raise ValueError("exchange code cannot start with one")
                elif self.number[1] == '0':
                    raise ValueError("area code cannot start with zero")
                elif self.number[1] == '1':
                    raise ValueError("area code cannot start with one")

        if number_counter == 11:
            self.number = ''.join([i for i in number if i.isdigit()][1:])
        else:
            self.number = ''.join([i for i in number if i.isdigit()])
        self.area_code = self.number[:3]
        
    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'