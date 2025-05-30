class Logger:

    def __init__(self):
        self.logs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logs:
            if timestamp - self.logs[message] >= 10:
                self.logs[message] = timestamp
                return True
            else:
                return False
        else:
            self.logs[message] = timestamp
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)