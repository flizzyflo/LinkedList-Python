from src.linked_list_head.linked_list_head import LinkedListHead


if __name__ == "__main__":

    l = LinkedListHead.create_random_list_values(length_of_list= 7, 
                                                  min_value= 5, 
                                                  max_value= 700)
    l.insert_new_value(1)
    print(l)