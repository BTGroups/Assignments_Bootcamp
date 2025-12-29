from typing import List, Set
class menu_item:
    def __init__(self, item_name, price):
        if not item_name:
            raise ValueError("Item name is required")
        if price <= 0:
            raise ValueError("Price must be positive")

        self.item_name = item_name 
        self.price = price 
    def __eq__(self, other):
        return isinstance(other, menu_item) and self.item_name == other.item_name

    def __hash__(self):
        return hash(self.item_name)


class Course_category:
    def __init__(self, category_name):
        if not category_name:
            raise ValueError("Category name is required")
        self.category_name = category_name 
        self.menuitems : Set[menu_item] = set()

    def add_item(self, item : menu_item):
        if not isinstance(item, menu_item):
            raise TypeError("Expected MenuItem")
        if item in self.menuitems:
            raise ValueError("Item already exists in this category")
        self.menuitems.add(item)

    def __eq__(self, other):
        return isinstance(other, Course_category) and self.category_name == other.category_name

    def __hash__(self):
        return hash(self.category_name)


class Menu:
    def __init__(self, menu_name : str):
        if not menu_name:
            raise ValueError("Menu name is required")
        self.menu_name = menu_name 
        self.categories : Set[Course_category] = set()

    def add_category(self, category : Course_category) -> None:
        if not isinstance(category, Course_category):
            raise TypeError("Expected CourseCategory")

        if category in self.categories:
            raise ValueError("Category already exists in this menu")
        self.categories.add(category)

    def get_all_items(self) -> List[menu_item]:
        items = []
        for category in self.categories:
            items.extend(category.menuitems)  
        return items 


class SpecialMenu(Menu):
    def __init__(self, menu_name : str, discount : int = 30):
        super().__init__(menu_name)   
        self.discount = discount


class Branch:
    def __init__(self, location : str):
        if not location:
            raise ValueError("Branch location is required")
        self.location = location 
        self.menus : Set[Menu] = set()

    def add_menu(self, menu : Menu) -> None:
        if not isinstance(menu, Menu):
            raise ValueError("Expected Menu")
        if menu in self.menus:
            raise ValueError("Menu already exists in this branch")
        self.menus.add(menu)
    
class Restaurant:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Restaurant name is required")

        self.name = name
        self.branches: Set[Branch] = set()

    def add_branch(self, branch: Branch) -> None:
        if not isinstance(branch, Branch):
            raise TypeError("Expected Branch")

        if branch in self.branches:
            raise ValueError("Branch already exists")

        self.branches.add(branch)



class MenuService:
    def __init__(self, menus: Set[Menu]):
        self.menus = menus

    def total_menu_items(self) -> int:
        return sum(len(menu.get_all_items()) for menu in self.menus)

    def items_by_category(self, category_name: str) -> List[str]:
        result = []
        for menu in self.menus:
            for category in menu.categories:
                if category.category_name == category_name:
                    result.extend(item.item_name for item in category.menu_items)
        return result

    def special_discount_menus(self) -> List[str]:
        return [
            menu.menu_name
            for menu in self.menus
            if isinstance(menu, SpecialMenu)
        ]


def create_sample_data():
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

    return branch

if __name__ == "__main__":

    branch = create_sample_data()

    service = MenuService(branch.menus)

    print("Total Menu Items:", service.total_menu_items())
    print("Items in Main Course:", service.items_by_category("Main Course"))
    print("Special Discount Menus:", service.special_discount_menus())
