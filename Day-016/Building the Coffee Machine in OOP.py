from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()  # هادي فيها تقرير المواد
        money_machine.report()  # هادي فيها تقرير الفلوس

    else:
        drink = menu.find_drink(choice) # وضعنا في المتغير drink الطلب الذي اختاره المستخدم
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):  # اذا كانت المكونات كافية للطلب (is_resource_sufficient)، وكان المبلغ المدفوع كاملا غير ناقص (make_payment):
            coffee_maker.make_coffee(drink) # فاصنع القهوة

