from src.linked_list_element.linked_list_element import LinkedListElement
from random import randint

class LinkedListHead:

    """Linked List Control Class. Manages the linked list and accesses the elements. 
    Is used to create, insert and remove elements from the list or represent the list."""


    def __init__(self) -> None:
        self.value = "head"
        self.next = None


    def __str__(self) -> str:
        return self.__get_list(self)


    def __repr__(self) -> str:
        return_string = self.__get_list(self).replace("head -> ", "").replace(" -> None", "").replace(" -> ", ", ")
        return f"[{return_string}]"
        

    def __get_list(self, LinkedListNode: 'LinkedListElement|LinkedListHead') -> str:

        """Private Method to print the list elements for the representation of the list."""

        if LinkedListNode.next == None:
            return f"{LinkedListNode.value} -> None"
        
        else:
            return f"{LinkedListNode.value} -> {self.__get_list(LinkedListNode.next)}"


    def get_element_by_index(self, index: int) -> int:

        return self.__get_element_by_index(self, index)

    
    def __get_element_by_index(self, LinkedListNode: 'LinkedListElement|LinkedListHead', index: int) -> int:
        
        if index > self.length():
            raise IndexError(f"{index=} is out of List Range {self.length()}.")
        
        current_index = 0
        current_node = LinkedListNode.next
        
        while True:

            if current_index == index:
                return current_node

            current_index += 1
            current_node = current_node.next
        

    def is_empty(self) -> bool:
        
        """Checks if the list contains elements or not. Returns either true or false"""

        return self.next == None


    def value_in_list(self, value_to_search: int) -> bool:

        """Returns a boolean value if a specific value is within the list or not"""

        return self.__value_in_list(value_to_search, self)


    def __value_in_list(self, value_to_search: int, LinkedListNode: 'LinkedListElement|LinkedListHead') -> bool:
        
        """Private method which is used to look up values within the linked list. Returns a boolean value according to the existence or absence of a specific value."""

        if LinkedListNode.value == value_to_search:
            return True

        if LinkedListNode.next == None:
            return False

        return self.__value_in_list(value_to_search, LinkedListNode.next)


    def insert_new_value(self, value_to_insert: int) -> None:

        """Inserts a new value into the linked list. Automatically sorts the value
        to the right place according to the value."""

        self.__insert_new_value(value_to_insert= value_to_insert, LinkedListNode= self)


    def __insert_new_value(self, value_to_insert: int, LinkedListNode: 'LinkedListElement|LinkedListHead') -> None:
        
        """Private Method to insert elements in a sorted way, in a ascending order."""

        if LinkedListNode.next == None:
            # list is empty, no element exists.
            LinkedListNode.next = LinkedListElement(value_to_insert, None)

        elif value_to_insert < LinkedListNode.next.value:
            # next node value is bigger than value to be inserted
            # next node has to be the predecessor of this new value and new LL element

            tempNext = LinkedListNode.next
            LinkedListNode.next = LinkedListElement(value_to_insert, tempNext)

        elif LinkedListNode.next.next == None:
            # at least one node exists, but no next element, end of list is reached.
            # create new element with the value to insert as node value.
            LinkedListNode.next.next = LinkedListElement(value_to_insert)

        else:
            self.__insert_new_value(value_to_insert, LinkedListNode.next)


    def remove_value_from_list(self, value_to_remove: int) -> None:
        
        """Removes an element from the linked list"""

        if self.is_empty() or not self.value_in_list(value_to_remove):
            return

        else:
            # Value is in list, input head node as start
            self.__remove_value_from_list(value_to_remove= value_to_remove, 
                                          LinkedListNode= self)


    def __remove_value_from_list(self, value_to_remove: int, LinkedListNode: 'LinkedListElement|LinkedListHead') -> None:
        
        """Private method to remove a specific value from the linked list."""

        if LinkedListNode.next.value == value_to_remove:
            LinkedListNode.next = LinkedListNode.next.next

        else:
            self.__remove_value_from_list(value_to_remove, LinkedListNode.next)


    def is_sorted(self, reverse: bool = False) -> bool:
        
        """Checks whether the linked list elements are sorted or not."""

        return self.__is_sorted(self, reverse= reverse)

    
    def __is_sorted(self, LinkedListNode: 'LinkedListElement|LinkedListHead', reverse: bool = False) -> bool:

        """Private method to return a boolean if the list is sorted or not."""

        if LinkedListNode.next == None:
            return True
        
        elif not isinstance(LinkedListNode.value, int):
            return self.__is_sorted(LinkedListNode.next, reverse= reverse)

        elif LinkedListNode.value > LinkedListNode.next.value and not reverse:
            return False

        elif LinkedListNode.value < LinkedListNode.next.value and reverse:
            return False

        else:
            return self.__is_sorted(LinkedListNode.next, reverse= reverse)


    def sort_elements(self) -> None:
        
        """Main sort function. applies some sort of bubblesort to sort the linked list. Sorts as long as the is_sorted() returns true."""

        while True:
            self.__sort_elements(LinkedListNode= self)
            
            if self.is_sorted(reverse= False):
                break


    def __sort_elements(self, LinkedListNode: 'LinkedListElement|LinkedListHead') -> None:
        
        """Private Method to sort the linked list elements"""

        # starts with head node. next pointer points to first linked list element
        if LinkedListNode.next == None or LinkedListNode.next.next == None:
            return
        
        # start -> 8 -> 4 -> 6
        elif LinkedListNode.next.next.value < LinkedListNode.next.value:
   
            tempNextNext = LinkedListNode.next.next # 4
            tempNext = LinkedListNode.next # 8
            tempNext.next = tempNextNext.next # 6 from 4
            tempNextNext.next = tempNext
            LinkedListNode.next = tempNextNext

        else:
            return self.__sort_elements(LinkedListNode.next)


    def reverse_linked_list(self) -> None:

        """Reverses the current linked list and and sorts it in a reversed way.
        3 -> 5 -> 7 becomes 7 -> 5 -> 3 """

        while True:
            self.__reverse_linked_list(LinkedListNode= self)

            if self.is_sorted(reverse= True):
                break


    def __reverse_linked_list(self, LinkedListNode: 'LinkedListElement|LinkedListHead') -> None:
        
        """Reverts the linked list element per element"""

        if LinkedListNode.next == None or LinkedListNode.next.next == None:
            return

        elif LinkedListNode.next.value < LinkedListNode.next.next.value:
    
            tempNext = LinkedListNode.next
            tempNextNext = LinkedListNode.next.next
            tempNextNextNext = tempNextNext.next
            LinkedListNode.next = tempNextNext
            tempNext.next = tempNextNextNext
            tempNextNext.next = tempNext

        else:
            self.__reverse_linked_list(LinkedListNode= LinkedListNode.next)


    def length(self) -> int:
        
        """Calculates the length of the linked list. Counts all elements which are not 'None'"""

        return self.__length(self) - 1  # -1 because of None information node. this node will be ignored

    
    def __length(self, LinkedListNode: 'LinkedListElement|LinkedListHead') -> int:

        """Private method which calculates the length of the linked list. Counts all elements which are not 'None'"""
        
        if LinkedListNode.next == None:
            return 0

        else:
            return 1 + self.__length(LinkedListNode= LinkedListNode.next)


    def create_random_list_values(length_of_list: int, min_value: int, max_value: int) -> 'LinkedListHead':
        
        """Static method to create a linked list filled with random values. 
        Length and value range can be passed in as argument. Returns the linked list head instance."""

        list_head = LinkedListHead()
        length: int = 0

        possible_length = max_value - min_value 
        # max length of the list can be the difference between max value and min value 
        # since there are no double values in the linked list
        # if manually inserted length exceeds the real max length, 
        # the lenght is set to the max possible lenght

        if possible_length < length_of_list:
            length_of_list = possible_length

    
        while length < length_of_list:

            element_to_add = randint(min_value, max_value)

            # element should be unique within the linked list. 
            # if element exists, continue and generate new value to insert.
            if list_head.value_in_list(element_to_add):
                continue
            
            # normale case, insert the value and increase length count
            # to break out of the while loop.
            else:
                list_head.insert_new_value(element_to_add)
                length += 1

        return list_head

