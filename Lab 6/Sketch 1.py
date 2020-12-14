# Разработать структуру классов с использованием
# механизмов наследования и агрегации для
# предметной области из лабораторной работы № 1
# Полную модель предметной области описывать в
# виде классов не обязательно (достаточно 3-4 классов)

# В работе должны быть использованы:
# 1. Отношение наследования (между одним базовым классом и
# как минимум двумя производными)
# 2. Не менее одного отношения агрегации между классами

class Flight:
    '''Система бронирования билетов'''
    def __init__(self, voyage, cost, site):
        self.voyage = voyage
        self.cost = cost
        self.site = site
        self.dates = {}

    def reserv(self, date, site):
        reserved = self.dates[date]
        if site + reserved > self.site:
            raise Exception
        else:
            self.dates[date] = reserved + site

class Order:
    new = "New"
    reserved = "Reserved"
    payed = "Payed"
    canceled = "Canceled"

    def __init__(self, city, flight, date, site, transport):
        self.city = city
        self.flight = flight
        self.date = date
        self.site = site
        self.transport = transport
        self.state = Order.new

    def reserv(self):
        if self.state == Order.new:
            try:
                self.flight.reserv()
                self.state = Order.reserved
            except:
                raise Exception
        else:
            raise Exception

class System:
    t1 = "Moscow"
    t2 = "St. Petersburg"
    t3 = "Volgograd"

    rc1 = Flight(t1, 155, 25)
    rc2 = Flight(t2, 455, 15)
    rc3 = Flight(t3, 755, 25)

    orders = []

    def order(self, flight, city, date, site, transport):
        new_order = Order(city, flight, date, site, transport)
        self.orders.append(new_order)

    def reserv(self, order):
        order.reserv()
