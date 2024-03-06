class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, value=None):
        if len(value) > 20:
            raise ValueError
        self.current = Node(value)

    def visit(self, value):
        new_page = Node(value=value, prev=self.current)
        self.current.next = new_page
        self.current = new_page
        return new_page.value

    def back(self, steps):
        if steps > 0:
            for _ in range(steps):
                if self.current.prev is None:
                    break
                self.current = self.current.prev
        print(self.current.value)
        return self.current

    def forward(self, steps):
        if steps > 0:
            for _ in range(steps):
                if self.current.next is None:
                    break
                self.current = self.current.next
        print(self.current.value)
        return self.current


def run():
    browser_history = BrowserHistory("leetcode.com")
    browser_history.visit("google.com")
    browser_history.visit("facebook.com")
    browser_history.visit("youtube.com")
    browser_history.back(1)
    browser_history.back(1)
    browser_history.forward(1)
    browser_history.visit("linkedin.com")
    browser_history.forward(2)
    browser_history.back(2)
    browser_history.back(7)


run()
