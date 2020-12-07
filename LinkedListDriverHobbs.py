"""
Noah Hobbs
10/3/2020
"""
from LinkedList import LinkedList
from CanHobbs import Can

if __name__ == '__main__':

    soup1 = Can("Campells", "spaghetti", 8.6, 12.0)
    soup2 = Can("Do Goods", "Chicken Dumpling", 7, 15.25)
    soup3 = Can("Fareway", "Chicken Noodle", 12, 9)
    soup4 = Can("Hyvee", "Cream of Chicken", 6.8, 5)
    soup5 = Can("Zebra Soups", "Zebra Chunks", 7.5, 34.99)
    # creating my linked list
    my_list = LinkedList()
    print(my_list.isEmpty())
    # adding the cans to my linked list
    my_list.addBack(soup1)
    my_list.addFront(soup2)
    my_list.addFront(soup3)
    my_list.addBack(soup4)
    my_list.addBack(soup5)
    print(my_list.print())
    print(my_list.isEmpty())
    my_list.remove(soup2)
    print(my_list.print())
    print(my_list.find(soup5))
    my_list.removeFront()
    print("")
    print(my_list.print())
    input('Press any key to continue')
