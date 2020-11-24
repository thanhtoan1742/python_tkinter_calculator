import tkinter as tk

class Calculator:
    BUTTON_WIDTH = 3
    BUTTON_HEIGHT = 2
    NUMBER_KEY = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SIGN_KEY = ['+', '-', '*', '/', '=']
    SPECIAL_KEY = ['Return', 'BackSpace', 'Delete']

    def __init__(self):
        self.result = 0
        self.sign = ''
        self.first = True
        self.inBuffer = ''

    def appendInBuffer(self, c):
        self.inBuffer += c
        self.inBufferField.configure(text=self.inBuffer)

    def clearInBuffer(self):
        self.inBuffer = ''
        self.updateGUI()

    def setSign(self, sign):
        if self.inBuffer != '':
            if self.sign == '' or self.sign == '=':
                self.result = int(self.inBuffer)
            else:
                self.calculate()

        self.sign = sign
        self.clearInBuffer()
        self.updateGUI()

    def calculate(self):
        print(self.result, self.sign, self.inBuffer)
        if self.sign == '+':
            self.result += int(self.inBuffer)
        if self.sign == '-':
            self.result -= int(self.inBuffer)
        if self.sign == '*':
            self.result *= int(self.inBuffer)
        if self.sign == '/':
            self.result //= int(self.inBuffer)

    def keyCallback(self, event):
        if not len(event.char):
            return
            
        if event.char in self.NUMBER_KEY:
            self.appendInBuffer(event.char)

        if event.char in self.SIGN_KEY:
            self.setSign(event.char)
        
        if ord(event.char) == 13:
            self.setSign('=')

        if ord(event.char) == 8 or ord(event.char) == 127:
            self.clearInBuffer()

    def updateGUI(self):
        self.resultField.configure(text=str(self.result))
        self.signField.configure(text=self.sign)
        self.inBufferField.configure(text='')

    def run(self):
        root = tk.Tk()
        root.title('Integer Calculator')
        root.bind('<Key>', self.keyCallback)

        self.resultField = tk.Label(root, text='0')
        self.signField = tk.Label(root)
        self.inBufferField = tk.Label(root)
        button0 = tk.Button(root, text='0', command=lambda: self.appendInBuffer('0'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button1 = tk.Button(root, text='1', command=lambda: self.appendInBuffer('1'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button2 = tk.Button(root, text='2', command=lambda: self.appendInBuffer('2'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button3 = tk.Button(root, text='3', command=lambda: self.appendInBuffer('3'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button4 = tk.Button(root, text='4', command=lambda: self.appendInBuffer('4'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button5 = tk.Button(root, text='5', command=lambda: self.appendInBuffer('5'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button6 = tk.Button(root, text='6', command=lambda: self.appendInBuffer('6'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button7 = tk.Button(root, text='7', command=lambda: self.appendInBuffer('7'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button8 = tk.Button(root, text='8', command=lambda: self.appendInBuffer('8'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        button9 = tk.Button(root, text='9', command=lambda: self.appendInBuffer('9'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonPlus = tk.Button(root, text='+', command=lambda: self.setSign('+'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonMinus = tk.Button(root, text='-', command=lambda: self.setSign('-'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonMultiply = tk.Button(root, text='x', command=lambda: self.setSign('*'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonDivide = tk.Button(root, text='/', command=lambda: self.setSign('/'), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonEqual = tk.Button(root, text='=', command=lambda: self.setSign('='), width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)
        buttonClear = tk.Button(root, text='C', command=self.clearInBuffer, width=self.BUTTON_WIDTH, height=self.BUTTON_HEIGHT)


        self.resultField.grid(row=0, column=0, columnspan=10)
        self.signField.grid(row=1, column=0, columnspan=10)
        self.inBufferField.grid(row=2, column=0, columnspan=10)

        button1.grid(row=3, column=0)
        button2.grid(row=3, column=1)
        button3.grid(row=3, column=2)
        button4.grid(row=4, column=0)
        button5.grid(row=4, column=1)
        button6.grid(row=4, column=2)
        button7.grid(row=5, column=0)
        button8.grid(row=5, column=1)
        button9.grid(row=5, column=2)
        button0.grid(row=6, column=0)
        buttonClear.grid(row=6, column=1)
        buttonEqual.grid(row=6, column=2)
        buttonDivide.grid(row=6, column=3)
        buttonPlus.grid(row=3, column=3)
        buttonMinus.grid(row=4, column=3)
        buttonMultiply.grid(row=5, column=3)

        root.mainloop()



calculator = Calculator()
calculator.run()
