class base62:
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return self.__num

    def __add__(self, num2):
        total = c62ToNum(self.__num) + c62ToNum(num2)
        return cnumTo62(total)

    def __sub__(self, num2):
        total = c62ToNum(self.__num) - c62ToNum(num2)
        return cnumTo62(total)

    def __mul__(self, num2):
        total = c62ToNum(self.__num) * c62ToNum(num2)
        return cnumTo62(total)

    def __div__(self, num2):
        total = c62ToNum(self.__num) / c62ToNum(num2)
        return cnumTo62(total)

    def __mod__(self, num2):
        total = c62ToNum(self.__num) % c62ToNum(num2)
        return cnumTo62(total)

    def __lt__(self, num2):
        ans = c62ToNum(self.__num) < c62ToNum(num2)
        return cnumTo62(total)

    def __le__(self, num2):
        ans = c62ToNum(self.__num) <= c62ToNum(num2)
        return cnumTo62(total)

    def __eq__(self, num2):
        ans = c62ToNum(self.__num) == c62ToNum(num2)
        return cnumTo62(total)

    def __ne__(self, num2):
        ans = c62ToNum(self.__num) != c62ToNum(num2)
        return cnumTo62(total)

    def __ge__(self, num2):
        ans = c62ToNum(self.__num) >= c62ToNum(num2)
        return cnumTo62(total)

    def __gt__(self, num2):
        ans = c62ToNum(self.__num) > c62ToNum(num2)
        return cnumTo62(total)

    def __len__(self):
        return len(self.__num)

    def __getitem__(self, num):
        return self.__num[num]

def c62ToNum(num):
    b10 = 0
    while (len(num) > 0):
        if ord(num[0]) <= 57:
            b10 += (ord(num[0])-48) * (62 ** (len(num)-1))
        elif ord(num[0]) <= 90:
            b10 += (ord(num[0])-55) * (62 ** (len(num)-1))
        else:
            b10 += (ord(num[0])-61) * (62 ** (len(num)-1))
        num = num[1:]
    return b10

def cnumTo62(num):
    digits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    num62 = ""
    while (num != 0):
        num62 = digits[num%62] + num62
        num /= 62
    return num62

print cnumTo62(3000)
