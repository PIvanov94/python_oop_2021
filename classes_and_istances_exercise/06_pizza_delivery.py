class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def form_ingredients(self):
        form_ingredients_list = []
        for i, q in self.ingredients.items():
            form_ingredients_list.append(f"{i}: {q}")
        return form_ingredients_list

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(self.form_ingredients())}" \
               f" and the price will be {self.price}lv."
