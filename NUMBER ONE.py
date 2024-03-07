class BrowserStack:
    def __init__(self):
        self.stack = []
        self.current_index = -1



    def navigation(self, uri):
        self.stack = self.stack[:self.current_index + 1]
        self.stack.append(uri)
        self.current_index += 1
        return f"Navigated to {uri}"

    def backward(self):
        if self.current_index > 0:
            self.current_index -= 1
            return f"Backward: Navigated to {self.stack[self.current_index]}"
        else:
            return "Cannot go backward, already at the beginning."

    def forward(self):
        if self.current_index < len(self.stack) - 1:
            self.current_index += 1
            return f"Forward: Navigated to {self.stack[self.current_index]}"
        else:
            return "Cannot go forward, already at the end."


pages = ["www.google.com", "www.github.com", "www.yahoo.com", "www.ucu.com", "www.microsoft.com", "www.skype.com"]

browser = BrowserStack()
output = [browser.navigation(page) for page in pages]

print(output)
print(browser.backward())
print(browser.backward())
print(browser.forward())
print(browser.navigation("www.3wschools.com"))
print(browser.forward()) 

