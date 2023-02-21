class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        hour = self.__hour + other.__hour
        minute = self.__minute + other.__minute
        second = self.__second + other.__second

        if second >= 60:
            minute += second // 60
            second = second % 60
        if minute >= 60:
            hour += minute // 60
            minute = minute % 60

        return Time(hour, minute, second)

time1 = Time(1, 20, 30)
time2 = Time(2, 40, 50)
time3 = time1 + time2
print(time3.__dict__) 
