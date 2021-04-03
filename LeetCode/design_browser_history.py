# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the 
# history number of steps or move forward in the history number of steps.

# Web pages ===> [a, b, c, d, e]
# ptr - 0

# DESIGN BROWSER HISTORY
class BrowserHistory:
    def __init__(self, homepage):
        self.hist = [homepage]
        self.pnt = 0
    
    def visit(self, url):
        while len(self.hist) - 1 > self.pnt:
            self.hist.pop()
        self.hist.append(url)
        self.pnt += 1
    
    def back(self, steps):
        while steps > 0 and self.pnt > 0:
            self.pnt -= 1
            steps -= 1
        return self.hist[self.pnt]

    def forward(self, steps):
        while steps > 0 and self.pnt < len(self.hist) - 1:
            self.pnt += 1
            steps -= 1
        return self.hist[self.pnt]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# homepage = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]

# url = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# # Output: [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# a = BrowserHistory("leetcode.com")

# # print( a. )

