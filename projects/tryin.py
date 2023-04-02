class My_tab:
    menu = {
        'wine': 5,
        'beer': 3,
        'soft drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'desert': 6
    }
    def __init__(self):
        self.items = []
        self.total = 0

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]
        
    def print_bill(self):
        for item in self.items:
            print(f'{item:20} {self.menu[item]}')
        print(f'{"Total":20} {self.total}')
