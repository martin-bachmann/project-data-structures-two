class TrackOrders:
    def __init__(self):
        self._orders = list()

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        self._orders.append((customer, order, day))

    def contador_mais_comum(self, data):
        mais_comum = ""
        mais_comum_contador = 0

        for item in data.items():
            if item[1] > mais_comum_contador:
                mais_comum = item[0]
                mais_comum_contador = item[1]

        return mais_comum

    def contador_menos_comum(self, data):
        menos_comum = ""
        menos_comum_contador = 9999

        for item in data.items():
            if item[1] < menos_comum_contador:
                menos_comum = item[0]
                menos_comum_contador = item[1]

        return menos_comum

    def contador_nao_ocorrido(self, data):
        nao_ocorrido = set()

        for item in data.items():
            if item[1] == 0:
                nao_ocorrido.add(item[0])

        return nao_ocorrido

    def get_most_ordered_dish_per_customer(self, customer):
        pedidos = {}
        for item in self._orders:
            if item[0] == customer:
                if item[1] not in pedidos:
                    pedidos[item[1]] = 1
                else:
                    pedidos[item[1]] += 1

        return self.contador_mais_comum(pedidos)

    def get_never_ordered_per_customer(self, customer):
        pedidos = {}
        for item in self._orders:
            if item[1] not in pedidos:
                pedidos[item[1]] = 0
            if item[0] == customer:
                pedidos[item[1]] += 1

        return self.contador_nao_ocorrido(pedidos)

    def get_days_never_visited_per_customer(self, customer):
        dias = {}
        for item in self._orders:
            if item[2] not in dias:
                dias[item[2]] = 0
            if item[0] == customer:
                dias[item[2]] += 1

        return self.contador_nao_ocorrido(dias)

    def get_busiest_day(self):
        dias = {}
        for item in self._orders:
            if item[2] not in dias:
                dias[item[2]] = 1
            else:
                dias[item[2]] += 1

        return self.contador_mais_comum(dias)

    def get_least_busy_day(self):
        dias = {}
        for item in self._orders:
            if item[2] not in dias:
                dias[item[2]] = 1
            else:
                dias[item[2]] += 1

        return self.contador_menos_comum(dias)
