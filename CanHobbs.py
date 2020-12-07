
class Can:
    """
    Class with a default constructor and
    another constructor that takes all perimeters

    """
    company = "Shell Corp"
    content = "Soup"
    size = 8.0
    price = 10.0

    def __init__(self, company, content, size, price):
        self.company = company
        self.content = content
        self.size = size
        self.price = price
        self.next = None

    def __repr__(self):
        return "<Test a:%s b:%s c:%s d:%s>" % (self.company, self.content,
                                               self.size, self.price)

    def __str__(self):
        return "%s %s is %s ounces and cost $%s" % (self.company, self.content,
                                                    self.size, self.price)


if __name__ == '__main__':
    """
    Making objects of the Can class and printing the information
    """
    soup1 = Can("Campells", "spaghetti", 8.6, 12.0)
    soup2 = Can("Hyvee", "Cream of Chicken", 6.8, 5)
    soup3 = Can("Fareway", "Chicken Noodle", 12, 9)
    soup4 = Can("Do Goods", "Chicken Dumpling", 7, 15.25)

    """ 
        I believe that this program will have a runtime of O(1) which 
        is o of constant time because there are no
        loops
    """