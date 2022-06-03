from js import console, document

class Calculator:
    def __init__(self, num_first, num_second, sign_click, cal_type):
        self.num_first = num_first
        self.num_second = num_second
        self.sign_click = sign_click
        self.cal_type = cal_type
        
calc = Calculator("", "", "", "")
ans = Element("typing-text")
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
sign = ["equal-to", "reverse", "ac"]

def numbers_clicked(args):
    typed_in = args.target.innerText
    if typed_in in num and calc.sign_click == "":
        ans.element.innerText += typed_in
        calc.num_first = ans.element.innerText
    elif typed_in in num and calc.sign_click != "":
        Element("typing-text").element.innerHTML += typed_in
        calc.num_second += typed_in    
    
def sign_clicked(args):
    if args.target.id == "equal-to":
       calculate()
    elif args.target.id == "reverse":
        clear_all()
    elif args.target.id == "ac":
        clear_all()
    elif args.target.id not in sign:
        calc.cal_type = args.target.id
        calc.sign_click = args.target.innerText
        Element("typing-text").element.innerHTML += "<span>" + calc.sign_click + "</span>"
            
def calculate():
    new_total = 0
    if calc.cal_type == "multiply":
        new_total = float(calc.num_first) * float(calc.num_second)
        Element("answer").element.innerText = new_total
    elif calc.cal_type == "divid":
        new_total = float(calc.num_first) / float(calc.num_second)
        Element("answer").element.innerText = new_total
    elif calc.cal_type == "minus":
        new_total = float(calc.num_first) - float(calc.num_second)
        Element("answer").element.innerText = new_total
    elif calc.cal_type == "plus":
        new_total = float(calc.num_first) + float(calc.num_second)
        Element("answer").element.innerText = new_total   
def clear_all():
    calc.num_first = ""
    calc.num_second = ""
    calc.cal_type = ""
    calc.sign_click = ""
    Element("typing-text").element.innerHTML = ""
    Element("answer").element.innerText = ""