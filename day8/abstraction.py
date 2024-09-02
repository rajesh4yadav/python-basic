from abc import ABC, abstractmethod

class computer(ABC):
    
    @abstractmethod
    def process(self,app):
        pass
    
    def run(self,app):
        self.process(app)
        
        
class laptop(computer):
    def process(self, app):
        print(f"laptop is running {app}")
class mobile(computer):
    def process(self, app):
        print(f"mobile is running {app}")

dell=laptop()
dell.run("pubg")
mobile=mobile()
mobile.run("free fire")

    
    
