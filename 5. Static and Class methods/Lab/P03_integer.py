# Create a class called Integer. Upon initialization, it should receive a single parameter value (int). It should have
# 3 additional methods: •	from_float(float_value) - creates a new instance by flooring the provided floating number.
# If the value is not a float, return a message "value is not a float" •	from_roman(value) - creates a new instance
# by converting the roman number (as string) to an integer •	from_string(value) - creates a new instance by
# converting the string to an integer (if the value cannot be converted, return a message "wrong type")

class Integer:

    def __init__(self, val):
        self.value = val

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return f"value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return cls(num)


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
