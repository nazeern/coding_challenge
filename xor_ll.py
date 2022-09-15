import ctypes


class NodeXORLL():

    def __init__(self, val=0, both=0):
        self.val = val
        self.both = both


class XORLL():

    def __init__(self):
        self.head = None

    def get(self, index):
        """Return the node at INDEX."""
        if self.head == None:
            print("Null Linked List")
            return

        curr = self.head
        prev = None

        while index > 0 and curr.both ^ get_ptr(prev) != get_ptr(None):
            if curr.both ^ get_ptr(prev) == get_ptr(None):
                print("Index out of bounds error")
            else:
                prev, curr = curr, dereference_ptr(curr.both ^ get_ptr(prev))

        return curr.val


    def add(self, element):
        """Add ELEMENT to the end of the Linked List."""
        if self.head == None:
            self.head = NodeXORLL(element, get_ptr(None))

        curr = self.head
        prev = None
        while curr.both ^ get_ptr(prev) != get_ptr(None):
            prev, curr = curr, dereference_ptr(curr.both ^ get_ptr(prev))

        child = NodeXORLL(element, both=get_ptr(curr))
        curr.both = curr.both ^ get_ptr(child)



def get_ptr(obj):
    return id(obj)

def dereference_ptr(addr):
    return ctypes.cast(addr, ctypes.py_object).value


if __name__ == "__main__":
    print("Running tests:")
    my_list = XORLL()
    for i in range(5):
        print(f"Adding {i}")
        my_list.add(i)
    
    for i in range(5):
        print(f"Index {i} = {my_list.get(i)}")