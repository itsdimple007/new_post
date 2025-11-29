class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    # def show_color(self):
    #     return self.color
    # def show_cost(self):
    #     return self.cost
    def show_item(self):
        print("color is",self.color)
        print("Enter cost here",self.cost)

p2=Phone()
p2.set_color("Pink")
p2.set_cost(120)
p2.show_item()   
      

