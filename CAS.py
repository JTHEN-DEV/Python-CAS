import math
# CALCULATE
def calculate():
    global calc, z
    while (len(calc) != 1):
        #SQRT
        while ('sqrt' in calc):
            try:
                e = calc.index('sqrt')
                calc[e] = math.sqrt(float(calc[e+1]))
                del calc[e+1]
                print(calc)
            except:
                pass
        #IND
        while ('^' in calc):
            try:
               e = calc.index('^')
               calc[e-1] = float(calc[e-1])**float(calc[e+1])
               del calc[e]
               del calc[e]
               print(calc)
            except:
                pass
        #MUL AND DIV
        i = 0
        while(('*' in calc) or ('/' in calc)):
            i = 0
            while(i < len(calc)):
                if (calc[i] == '*'):
                    calc[i-1] = float(calc[i-1])*float(calc[i+1])
                    del calc[i]
                    del calc[i]
                    print(calc)
                    i = 0
                elif (calc[i] == '/'):
                    try:
                        calc[i-1] = float(calc[i-1])/float(calc[i+1])
                        del calc[i]
                        del calc[i]
                        print(calc)
                        i = 0
                    except ZeroDivisionError:
                        z = True
                        return
                i += 1
        #ADD AND SUB
        i = 0
        while(('+' in calc) or ('-' in calc)):
            i = 0
            while (i < len(calc)):
                if (calc[i] == '+'):
                    try:
                        calc[i-1] = float(calc[i-1])+float(calc[i+1])
                        del calc[i]
                        del calc[i]
                        print(calc)
                        i = 0
                    except:
                        pass
                elif (calc[i] == '-'):
                    try:
                        calc[i-1] = float(calc[i-1])-float(calc[i+1])
                        del calc[i]
                        del calc[i]
                        print(calc)
                        i = 0
                    except:
                        pass
                i += 1
    print("FINAL: " + str(round(float(calc[0]), 10)))
    return calc[0]
while (True):
    #INIT
    lex = []
    right = []
    left = []
    calc = []
    prevnum = False
    ans = input("EQUATION: \n")
    brac = False
    val = False
    eq = False
    sqrt = False
    z = False
    bc = False
    #LEX
    i = 0
    while(i < len(ans)):
        if (ans[i] != ' '):
            try:
                val = int(ans[i])
                if (prevnum):
                    lex[-1] = (str(lex[-1]) + ans[i])
                else:
                    lex.append(ans[i])
                    prevnum = True
            except ValueError:
                if (sqrt):
                    lex[-1] = lex[-1] + (ans[i])
                elif (ans[i] == 's'):
                    sqrt = True
                    lex.append(ans[i])
                elif (ans[i] != '.'):
                    lex.append(ans[i])
                if (ans[i] == 't'):
                    sqrt = False
                prevnum = False
                if (ans[i] == '.'):
                    prevnum = True
                    print(prevnum)
                    lex[-1] = lex[-1] + (ans[i])
        i+=1
    print(lex)
    #BRACKETS
    while ('(' in lex or ')' in lex):
        try:
            c = lex.index('(')
            brac = True
        except:
            pass
        if (brac):
            try:
                d = lex.index(')')
                val = True
            except ValueError:
                print("EQUATION DOES NOT INCLUDE CLOSING BRACKET")
                bc = True
                break      
        else:
            try:
                d = lex.index(')')
                print("EQUATION DOES NOT INCLUDE OPENING BRACKET")
                bc = True
                break 
            except:
                pass
        if (val):
            sub = []
            start = 0
            calc = []
            for i in range(len(lex)):
                if lex[i] == '(':
                    sub = []
                    start = i
                elif lex[i] == ')':
                    print(sub)
                    calc = sub
                    print(calc)
                    substitution = calculate()
                    for a in range(i-start+1):
                      del lex[start]
                    str(substitution)
                    lex.insert(start, str(float(substitution)))
                    i = len(lex)
                    print(lex)
                    sub = []
                    break
                else:
                    sub.append(lex[i])
    #LEFT RIGHT
    try:   
        b = lex.index('=')
        eq = True
        left = lex[:b]
        right = lex[b+1:]
    except ValueError:
        eq = False
    #FINISH UP
    if (eq):
        # DO STUFF
        print("EQUATION")
    else:
        calc = lex
        calculate()
        if (z):
                print("CANNOT DIVIDE BY ZERO")
                z = False
                continue
