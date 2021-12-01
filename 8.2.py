class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно по правилам математики")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10000000, 0))
print(DivisionByNull.divide_by_null(555, 0.33))
print(div.divide_by_null(1, 0))