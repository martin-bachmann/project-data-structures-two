class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self._orders = list()
        self.ingredientes_utilizados = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        receita = self.INGREDIENTS[order]
        for ingredient in receita:
            if (
                self.ingredientes_utilizados[ingredient]
                >= self.MINIMUM_INVENTORY[ingredient]
            ):
                return False
            self.ingredientes_utilizados[ingredient] += 1
        self._orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        return self.ingredientes_utilizados

    def get_unavailable_ingredients(self):
        ingredientes_zerados = set()

        for ingrediente in self.ingredientes_utilizados.items():
            if ingrediente[1] >= self.MINIMUM_INVENTORY[ingrediente[0]]:
                ingredientes_zerados.add(ingrediente[0])

        return ingredientes_zerados

    def get_available_dishes(self):
        receitas_possiveis = set(self.INGREDIENTS.keys())
        ingredientes_zerados = self.get_unavailable_ingredients()

        for receita in self.INGREDIENTS.items():
            for ingrediente in receita[1]:
                if ingrediente in ingredientes_zerados:
                    receitas_possiveis.discard(receita[0])

        return receitas_possiveis
