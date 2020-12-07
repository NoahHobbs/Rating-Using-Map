from ListEmptyException import ListEmptyException


class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        """

        :return: if self.empty is true the return is 0 otherwise it returns
        the size of the list
        """
        size = 0
        if self.isEmpty():
            return 0
        else:
            curr = self.head
            while curr:
                size += 1
                curr = curr.next
            return size

    def addBack(self, value):
        """
        Adds a value to the back of the list
        :param value: something to be added to the list
        :return: a string saying what was added
        """
        if not self.head:
            self.head = value
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = value
        return f'{value} added to array '

    def remove(self, value_to_remove):
        """
        Removes a value
        :param value_to_remove: what will be removed
        """
        if self.isEmpty():
            raise ListEmptyException('The list is empty')
        else:
            if self.head == value_to_remove:
                self.head = self.head.next
                return
            current = self.head.next
            previous = self.head

            while current:
                if current == value_to_remove:
                    previous.next = current.next
                    break
                else:
                    previous = current
                    current = current.next

    def print(self):
        """
        :return: a formatted string with everything in the list on a
        different line
        """
        str_print = ""
        current = self.head
        while current:
            str_print += str(current) + "\n"
            current = current.next
        return str_print

    def isEmpty(self):
        """
        :return: a bool value that if the head is empty will return true or
        if it has a value will return false
        """
        return not bool(self.head)

    def find(self, value_to_find):
        """
        is passed a value to check if it is inside the list
        :param value_to_find: The value that will be checked
        :return: the index position of the value will return none if not in
        the list
        """
        found = False
        current = self.head
        if self.head is None:
            ListEmptyException('List is empty')
        while not found:
            if current == value_to_find:
                found = True
            else:
                current = current.next
        return current

    def addFront(self, value):
        """
        Adds to the front
        :param value: What will be added
        :return: an f string saying what value has been added
        """
        if not self.head:
            self.head = value
        else:
            value.next = self.head
            self.head = value
        return f'{value} added to array'

    def removeFront(self):
        """
        Removes from the front of the list
        :return: if the list is empty will raise the exception
        """
        if self.isEmpty():
            raise ListEmptyException('The list is empty')
        else:
            self.head = self.head.next
