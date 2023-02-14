import tkinter as tk
from random import randint


class RevisionWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # labels
        self.QuestionLabel = tk.Label(self, text="Click next to start", font=(36))
        self.QuestionLabel.pack(pady=50)
        self.AnswerLabel = tk.Label(self, text="")
        self.AnswerLabel.pack(pady=50)
        # buttons
        button_frame = tk.Frame(self)
        button_frame.pack()
        answer_button = tk.Button(button_frame, text="Show Answer", command=lambda: self.show_answer())
        answer_button.grid(row=0, column=0, padx=20)
        next_button = tk.Button(button_frame, text="Next", command=lambda: self.next())
        next_button.grid(row=0, column=1)

        self.questions = [
            (("PC"), ("Program counter, contains the address of the next instruction")),
            (("CIR"), (
                "Current Instruction Register: stores the address of the next instruction currently being executed and decoded")),
            (("MAR"), ("Memory Address Register, holds relevant memory address (to read from or write to)")),
            (("MDR"), ("Memory Data Register, stores data being transferred to and from memory, acts as a buffer")),
            (
            ("ALU"), ("Arithmetic and Logic Unit, does all mathematical calculations and makes all logical decisions")),
            (("Accumulator"), (
                "A storage register in the ALU that holds data temporarily while the data is processed and before it is transferred to memory.")),
            (("RISC"), (
                "Reduced Instruction Set Computer: Only simple instructions taking one clock cycle are executed - currently more widely used than CISCAdvantages: allows for pipelining, execution will be quicker or as fast as CISC]Disadvantages: Compiler has to do more work, more RAM required"))
        ]

    def next(self):
        global random_question  # Allows the question to be accessed from the global scope required for multiple functions
        self.AnswerLabel.config(text="") # clears previous answer from screen
        random_question = randint(0, len((self.questions)) - 1)  # Selects random question
        self.QuestionLabel.config(text=self.questions[random_question][0])  # Updates question label with new question

    def show_answer(self):
        self.AnswerLabel.config(text=self.questions[random_question][1])  # updates answer label with new answer
