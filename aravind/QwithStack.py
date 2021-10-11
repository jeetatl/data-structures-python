class QiwithStack:
    def __init__(self) -> None:
        self.stack = []
    
    def enque(self,value):
        self.stack.append(value);
    
    def dequeu(self):

       if self.stack == []:
            return -1
       
       if len(self.stack)==1:
           return self.stack.pop()
       
       popped = self.stack.pop()
       f_popped = self.dequeu() 
       self.stack.append(popped)
       return f_popped

if __name__=="__main__":
    qws = QiwithStack()
    qws.enque(10)
    qws.enque(20)
    qws.enque(30)

    print(qws.dequeu())
    print(qws.dequeu())
    print(qws.dequeu())
    print(qws.dequeu())
    print(qws.dequeu())


