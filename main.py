from src.linked_list_head.linked_list_head import LinkedListHead


if __name__ == "__main__":

    linked_list_head = LinkedListHead.create_random_list_values(length_of_list=10,
                                                                min_value=5,
                                                                max_value=7000)
    linked_list_head.insert_new_value(1)
