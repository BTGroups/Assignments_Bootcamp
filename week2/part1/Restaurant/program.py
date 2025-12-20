class menu_item:
    def __init__(self, item_name, price):
        self.item_name = item_name 
        self.price = price 


class Course_category:
    def __init__(self, category_name):
        self.category_name = category_name 
        self.menuitems = []

    def add_item(self, item):
        self.menuitems.append(item)


class Menu:
    def __init__(self, menu_name):
        self.menu_name = menu_name 
        self.categories = [] 

    def add_category(self, category):
        self.categories.append(category)

    def get_all_items(self):
        items = []
        for category in self.categories:
            items.extend(category.menuitems)   # FIXED
        return items 


class SpecialMenu(Menu):
    def __init__(self, menu_name):
        super().__init__(menu_name)   # FIXED
        self.discount = 30


class Branch:
    def __init__(self, location):
        self.location = location 
        self.menus = [] 

    def add_menu(self, menu):
        self.menus.append(menu)
    

class Restaurant:
    def __init__(self, name):
        self.name = name 
        self.branches = [] 

    def add_branch(self, branch):
        self.branches.append(branch)


class MenuService:
    def __init__(self, menus):
        self.menus = menus   # FIXED

    def total_menu_items(self):
        return sum(len(menu.get_all_items()) for menu in self.menus)   # FIXED

    def items_by_category(self, category_name):
        result = [] 
        for menu in self.menus:
            for category in menu.categories:
                if category.category_name == category_name:
                    for item in category.menuitems:   # FIXED
                        result.append(item.item_name) # FIXED
        return result

    def special_discount_menus(self):
        result = []
        for menu in self.menus:
            if isinstance(menu, SpecialMenu):
                result.append(menu.menu_name)   # FIXED
        return result
if __name__ == "__main__":

    starters = Course_category("Starters")
    main_course = Course_category("Main Course")
    desserts = Course_category("Desserts")

    starters.add_item(menu_item("Soup", 100))
    starters.add_item(menu_item("Salad", 120))

    main_course.add_item(menu_item("Biryani", 250))
    main_course.add_item(menu_item("Paneer Curry", 220))

    desserts.add_item(menu_item("Ice Cream", 90))
    desserts.add_item(menu_item("Gulab Jamun", 80))

    regular_menu = Menu("Regular Menu")
    regular_menu.add_category(starters)
    regular_menu.add_category(main_course)
    regular_menu.add_category(desserts)

    special_menu = SpecialMenu("Festival Special Menu")
    special_menu.add_category(starters)
    special_menu.add_category(main_course)
    special_menu.add_category(desserts)

    branch = Branch("Chennai")
    branch.add_menu(regular_menu)
    branch.add_menu(special_menu)

    service = MenuService(branch.menus)

    print("Total Menu Items:", service.total_menu_items())
    print("Items in Main Course:", service.items_by_category("Main Course"))
    print("Special Discount Menus:", service.special_discount_menus())
