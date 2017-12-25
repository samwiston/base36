class base36:
    def __init__(self, num):
        self.__num = num

    def __str__(self):
        return self.__num

    def __add__(self, num2):
        total = c36ToNum(self.__num) + c36ToNum(num2)
        return cnumTo36(total)

    def __sub__(self, num2):
        total = c36ToNum(self.__num) - c36ToNum(num2)
        return cnumTo36(total)

    def __mul__(self, num2):
        total = c36ToNum(self.__num) * c36ToNum(num2)
        return cnumTo36(total)

    def __div__(self, num2):
        total = c36ToNum(self.__num) / c36ToNum(num2)
        return cnumTo36(total)

    def __mod__(self, num2):
        total = c36ToNum(self.__num) % c36ToNum(num2)
        return cnumTo36(total)

    def __lt__(self, num2):
        ans = c36ToNum(self.__num) < c36ToNum(num2)
        return cnumTo36(total)

    def __le__(self, num2):
        ans = c36ToNum(self.__num) <= c36ToNum(num2)
        return cnumTo36(total)

    def __eq__(self, num2):
        ans = c36ToNum(self.__num) == c36ToNum(num2)
        return cnumTo36(total)

    def __ne__(self, num2):
        ans = c36ToNum(self.__num) != c36ToNum(num2)
        return cnumTo36(total)

    def __ge__(self, num2):
        ans = c36ToNum(self.__num) >= c36ToNum(num2)
        return cnumTo36(total)

    def __gt__(self, num2):
        ans = c36ToNum(self.__num) > c36ToNum(num2)
        return cnumTo36(total)

    def __len__(self):
        return len(self.__num)

    def __getitem__(self, num):
        return self.__num[num]

def c36ToNum(num):
    b10 = 0
    while (len(num) > 0):
        if ord(num[0]) <= 57:
            b10 += (ord(num[0])-48) * (36 ** (len(num)-1))
        else:
            b10 += (ord(num[0])-55) * (36 ** (len(num)-1))
        num = num[1:]
    return b10

def cnumTo36(num):
    digits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    num36 = ""
    frac = num % 1
    num -= frac
    degree = 4

    if frac != 0:
        num36 += "."

    while(frac != 0) and (degree != 0):
        frac *= 36
        num36 += digits[int(frac/1)]
        frac -= int(frac/1)
        degree -= 1

    while (num != 0):
        num36 = digits[num%36] + num36
        num /= 36
    return num36

print cnumTo36(.37)
