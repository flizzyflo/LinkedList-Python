class LinkedListElement:

    """List Element Class to represent the value and reference the next element within the linked list."""

    def __init__(self, value: int, next_element: 'LinkedListElement' = None) -> None:
        self.value = value
        self.next = next_element

    def __repr__(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)
