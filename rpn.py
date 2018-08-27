#!/bin/python3
# RPN Calculator by Darrell Harriman  harrimand@gmail.com

import math
class rpn:
    def __init__(self, inStr=''):
        """Create RPN Stack from string"""
        self.stack = []
        self.funs = {
            "h": self.help,
            "+": self.add,
            "*": self.mul,
            "-": self.sub,
            "/": self.div,
            "du": self.dup,
            "dup2": self.dup2,
            "dupn": self.dupn,
            "dr": self.drop,
            "drn": self.dropn,
            "sq": self.sq,
            "sqr": self.sqr,
            "^": self.power,
            "%": self.mod,
            "p": self.pick,
            "pi": self.pi,
            "1/": self.inv,
            "ip": self.ip,
            "fp": self.fp,
            "sh": self.show,
            "sw": self.swap,
            "CLR": self.clr
        }
        self.update(inStr)

    def update(self, inStr):
        """Parse input, push integers and floats or perfrom operation """
        for n in inStr.split():
            if self.isnum(n):
                if '.' in n:
                    self.stack.append(float(n))
                    # print("Push".ljust(15), n.ljust(30), self.stack)
                else:
                    self.stack.append(int(n))
                    # print("Push".ljust(15), n.ljust(30), self.stack)
            else:
                if n in self.funs:
                    self.funs[n]()
        # print()

    def help(self):
        return ("\n"+\
            "? .... display this help\n"+\
            "w .... show welcome page\n"+\
            "+ .... add Level 1 to Level 2\n"+\
            "* .... muliply Level 1 by Level 2\n"+\
            "- .... subract Level 1 from Level 2\n"+\
            "/ .... divide Level 2 by Level 1\n"+\
            "du ... duplicate Level 1\n"+\
            "dup2.. duplicate Level 2 and Level 1\n"+\
            "dupn.. duplicate Level 1 items on stack\n"+\
            "dr ... drop Level 1 from stack\n"+\
            "drn .. drop Level1 items from stack\n"+\
            "sq ... square of Level 1\n"+\
            "sqr... square root of Level 1\n"+\
            "^ .... Level 2 raised to power of Level 1\n"+\
            "% .... Level 2 modulo Level 1\n"+\
            "p .... pick Level defined by Level 1 value\n"+\
            "pi ... push Pi to stack\n"+\
            "1/ ... invert (1/x) Level 1\n"+\
            "ip ... integer part of Level 1\n"+\
            "fp ... fractional part of Level 1\n"+\
            "sh ... Show entire stack\n"+\
            "sw ... swap Level 1 and Level 2\n"+\
            "CLR ... CLEAR stack\n"+\
            "EXIT .. Exit (close) application\n"\
            )

    def help2(self):
        helpStr = "{0:12} {1}\n".format("h", "display this help")+\
            "{0:12} {1}\n".format("dup2", "duplicate Level 2 and Level 1")
        return helpStr


    def getStack(self):
        """Return list of stack contents"""
        # print("GetStack Return: \n" + "\n".join([str(n) for n in self.stack]))
        stLen = len(self.stack)
        retStr = "" + "\n" * max(0, 20 - stLen)
        retStr = retStr + "\n".join([str(min(20, stLen) - i) + "\t" + str(n) for i, n in enumerate(self.stack[-20:])])
        return retStr
#        return "\n\t".join([str(n) for n in self.stack])
        # return self.stack

    def show(self):
        """Return columns with Level #s and Level Values"""
        stLen = len(self.stack)
        return "\n".join([str(stLen - i) + "\t" + str(n) for i, n in enumerate(self.stack)])

    def isnum(self, n):
        return n.replace('.','',1).isdigit()

    def add(self):
        """Add Level 2 to Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 + n2)
            # print("Add".ljust(15), (str(n1) + ' + ' + str(n2)).ljust(30), self.stack)
        else:
            pass
            # print("Add requires 2 items on Stack")

    def mul(self):
        """Multiply Level 2 by Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 * n2)
            # print("Multiply".ljust(15), (str(n1) + ' * ' + str(n2)).ljust(30), self.stack)
        else:
            pass
            # print("Multiply requires 2 items on Stack")

    def sub(self):
        """Subtract Level 1 from Level 2 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(n1 - n2)
            # print("Subtract".ljust(15), (str(n1) + ' - ' + str(n2)).ljust(30), self.stack)
        else:
            pass
            # print("Subtract requires 2 items on Stack")

    def div(self):
        """Divide Level 2 by Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n2 = self.stack.pop()
            n1 = self.stack.pop()
            self.stack.append(float(n1) / float(n2))
            # print("Divide".ljust(15), (str(n1) + ' / ' + str(n2)).ljust(30), self.stack)
        else:
            pass
            # print("Divide requires 2 items on Stack")

    def dup(self):
        """Duplicate Level 1 on the stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n1)
            # print("Duplicate".ljust(15), str(n1).ljust(30), self.stack)
        else:
            pass
            # print("Stack Empty")

    def dup2(self):
        """Duplicate Level 2 and Level 1 on the stack"""
        if len(self.stack) > 1:
            self.stack = self.stack + self.stack[-2:]
#            dupStr = " ".join([str(i) for i in self.stack[-2:]])
            # print("Dup 2".ljust(15), dupStr.ljust(30), self.stack)
        else:
            pass
            # print("dup2 requires 2 items on the stack")

    def dupn(self):
        """Duplicate Level 1 itmes on the stack"""
        if len(self.stack) > self.stack[-1]:
            n = self.stack.pop()
            self.stack = self.stack + self.stack[-n:]
        else:
            pass
            # print("dup2 requires 2 items on the stack")

    def sq(self):
        """Square Level 1 and place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1 * n1)
            # print("Square".ljust(15), str(n1).ljust(30), self.stack)
        else:
            pass
            # print("Stack Empty")

    def sqr(self):
        """Square Root Level 1 and place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(math.sqrt(n1))
            # print("Square Root".ljust(15), str(n1).ljust(30), self.stack)
        else:
            pass
            # print("Stack Empty")

    def power(self):
        """Raise Level 2 to power of Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2**n1)
            # print("Power".ljust(15), (str(n2) + ' ^ ' + str(n1)).ljust(30), self.stack)
        else:
            pass
            # print("Power requires 2 items on Stack")

    def mod(self):
        """Level 2 modulo Level 1 and place result on stack"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n2%n1)
            # print("Modulo".ljust(15), (str(n2) + ' % ' + str(n1)).ljust(30), self.stack)
        else:
            pass
            # print("Modulo requires 2 items on Stack")

    def pick(self):
        """Pick item from stack selected by Level 1 value + 1"""
        n1 = self.stack.pop()
        if len(self.stack) > (n1 - 2):
            n2 = self.stack[len(self.stack) - n1]
            self.stack.append(n2)
            # print("Pick Level".ljust(15), str(n1).ljust(30), self.stack)
        else:
            self.stack.append(n1)
            # print("Pick Level out of range")

    def pi(self):
        """Place Pi on stack """
        n1 = math.pi
        self.stack.append(n1)
        # print("Push Pi".ljust(15), (str(n1)[:4]+"...").ljust(30), self.stack)

    def inv(self):
        """1 / Level 1 Place result on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(1.0 / float(n1))
            # print("Invert".ljust(15), ("1/"+str(n1)).ljust(30), self.stack)
        else:
            pass
            # print("Stack Empty")

    def ip(self):
        """Place Integer Part of Level 1 on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(int(n1))
        else:
            pass

    def fp(self):
        """Place Fractional Part of Level 1 on stack"""
        if len(self.stack) > 0:
            n1 = self.stack.pop()
            self.stack.append(n1 - int(n1))
        else:
            pass

    def drop(self):
        """Drop Level 1 from stack"""
        if len(self.stack) > 0:
            # print("Drop".ljust(15), str(self.stack.pop()).ljust(30), self.stack)
            self.stack.pop()
        else:
            pass
            # print("Stack Empty")

    def dropn(self):
        """Drop Level 1 from stack"""
        if len(self.stack) > self.stack[-1] and isinstance(self.stack[-1], int):
            n = self.stack.pop()
            self.stack = self.stack[:-n]
            # print("Drop".ljust(15), str(self.stack.pop()).ljust(30), self.stack)
        else:
            pass
            # print("Stack Empty")

    def swap(self):
        """Swap Level 1 with Level 2"""
        if len(self.stack) > 1:
            n1 = self.stack.pop()
            n2 = self.stack.pop()
            self.stack.append(n1)
            self.stack.append(n2)
            # print("Swap".ljust(15), "L1 <-> L2".ljust(30), self.stack)
        else:
            pass
            # print("Swap requires 2 items on Stack")

    def clr(self):
        """Clear (empty) stack"""
        self.stack = []
        # print("Clear Stack".ljust(15), "clr".ljust(30), self.stack)
