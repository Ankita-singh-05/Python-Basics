from Chef import Chef

class ChineseChef(Chef):
    
    # Instead of using this functions again we can inherit the class 
    # def make_chicken(self):
    #     print("The chef makes a chicken")

    # def make_salad(self):
    #     print("The chef makes a salad")

    # Overwriting the same function will add the additional properties to the child class
    def make_special_dish(self):
        print("The chef makes Paneer Tika")

    def make_fried_rice(self):
        print("The Chef makes Fried Rice")