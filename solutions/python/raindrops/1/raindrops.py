def convert(number):
    def Pling(number):
        if number % 3 == 0:
            return "Pling"
    def Plang(number):
        if number % 5 == 0:
            return "Plang"
    def Plong(number):
        if number % 7 == 0:
            return "Plong"
    def strnum(number):
        if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            return str(number)
    return f"{Pling(number) if Pling(number) else ''}{Plang(number) if Plang(number) else ''}{Plong(number) if Plong(number) else ''}{strnum(number) if strnum(number) else ''}"
