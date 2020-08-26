class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> None:
        
        if len(self.arr) == 0:
            return none
        
        result = self.arr[-1]
        del self.arr[-1]
        
        return result

    def top(self) -> int:
        if len(self.arr) == 0:
            return none
        
        return self.arr[-1]

    def getMin(self) -> int:
        if len(self.arr) == 0:
            return none
        
        min = self.arr[0]
        for idx, ele in enumerate(self.arr):            
            if min > ele:
                min = ele
        
        return min