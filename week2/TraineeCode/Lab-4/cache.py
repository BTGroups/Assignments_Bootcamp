class Cache:
    _MAX_CAPACITY = 0

    """
    The MAX_CAPACITY value is initialized only during the first call to the static getter method and reused for subsequent calls.
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        if Cache._MAX_CAPACITY == 0:
            while True:
                try:
                    value = int(input("Enter Max Capacity: "))
                    if value > 0:
                        Cache._MAX_CAPACITY = value 
                        break
                except ValueError:
                    print("Enter a positive integer")
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
