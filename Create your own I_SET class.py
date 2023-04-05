

class I_SET:
    def _init_(self):
        self._data = []
        
    def insrting(self, element: int):
        if element not in self._data:
            self._data.append(element)
            
    def is_member(self, element: int) -> bool:
        return element in self._data
    
    def remove(self, element: int):
        if element in self._data:
            self._data.remove(element)
        else:
            raise ValueError(f"{element} not found ")
            
    def get_members(self) -> List[int]:
        return self._data[:]
    
    def get_members_desc(self) -> List[int]:
        return sorted(self._data, reverse=True)
    

s = I_SET()
s.insrting(3)
s.insrting(2)
s.insrting(4)

print(s.get_members())  
print(s.get_members_desc())  

s.remove(2)
print(s.get_members())  
print(s.is_member(3))  
print(s.is_member(2))  