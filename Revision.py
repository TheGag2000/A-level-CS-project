import tkinter as tk
import random
import sqlite3

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
        self.difficulty_button_frame = tk.Frame(self)

        self.DifficultyLabel = tk.Label(self.difficulty_button_frame, text  ="How did you find this question?")
        self.DifficultyLabel.grid(row =0, column=0, columnspan=3)
        answer_button = tk.Button(button_frame, text="Show Answer", command=lambda: self.show_answer())
        answer_button.grid(row=0, column=0, padx=20)
        next_button = tk.Button(button_frame, text="Next", command=lambda: self.next())
        next_button.grid(row=0, column=1)
        easy_button = tk.Button(self.difficulty_button_frame, text = "Easy", command = lambda: self.update_frequency(1))
        easy_button.grid(row = 1, column = 0)
        medium_button = tk.Button(self.difficulty_button_frame, text = "Medium", command = lambda: self.update_frequency(2))
        medium_button.grid(row = 1, column =1)
        hard_button = tk.Button(self.difficulty_button_frame, text = "Hard", command = lambda: self.update_frequency(3))
        hard_button.grid(row = 1, column = 2)

        # self.questions = [
        #     (("PC"), ("Program counter, contains the address of the next instruction"),(1)),
        #     (("CIR"), ("Current Instruction Register: stores the address of the next instruction currently being executed and decoded"),(2)),
        #     (("MAR"), ("Memory Address Register, holds relevant memory address (to read from or write to)"),(2)),
        #     (("MDR"), ("Memory Data Register, stores data being transferred to and from memory, acts as a buffer"),(3)),
        #     (("ALU"), ("Arithmetic and Logic Unit, does all mathematical calculations and makes all logical decisions"),(2)),
        #     (("Accumulator"), ("A storage register in the ALU that holds data temporarily while the data is processed and before it is transferred to memory."),(1)),
        #     (("RISC"), ("Reduced Instruction Set Computer: Only simple instructions taking one clock cycle are executed - currently more widely used than CISCAdvantages: allows for pipelining, execution will be quicker or as fast as CISC]Disadvantages: Compiler has to do more work, more RAM required"),(3))
        # ]

    def next(self):
        global random_question  # Allows the question to be accessed from the global scope required for multiple functions
        global random_difficulty
        global questions
        #global easy
        #global medium
        #global hard

        self.difficulty_button_frame.pack_forget() #removes difficulty buttons when next question is shown
        self.AnswerLabel.config(text="") # clears previous answer from screen
        population =[1,2,3]
        weights = [0.14,0.29,0.57]
        random_difficulty = random.choices(population,weights)
        #using data base
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        c. execute("SELECT *, rowid FROM flashcards WHERE difficulty = ?", (random_difficulty[0],))
        questions = c .fetchall()

        print(questions)


        conn.commit()
        conn.close()

        #generate random question
        random_question = random.randint(0,len(questions)-1)
        #display random question
        self.QuestionLabel.config(text = questions[random_question][0])




        # using list
        #easy = []
        #medium = []
        #hard = []
        # for i in range(0,(len(self.questions))): # generate list of questions to be selected from
        #     if random_difficulty[0] == 1: #select easy question
        #         if random_difficulty[0] == self.questions[i][2]:
        #             easy.append(self.questions[i]) # create list of easy questions
        #     elif random_difficulty[0] == 2:#select medium questions
        #         if random_difficulty[0] == self.questions[i][2]:
        #             medium.append(self.questions[i]) #create list of medium questions
        #     elif random_difficulty[0] ==3:
        #         if random_difficulty[0] == self.questions[i][2]:
        #             hard.append(self.questions[i]) #create list of hard questions
        #
        # print(random_difficulty)
        # print("easy",easy)
        # print("medium",medium)
        # print("hard",hard)
        #
        # if random_difficulty[0] == 1:
        #     random_question = random.randint(0,len(easy)-1)#chooses random question from easy questions
        #     self.QuestionLabel.config(text=easy[random_question][0]) # updates the tkinter question label
        # elif random_difficulty[0] ==2:
        #     random_question = random.randint(0,len(medium)-1) #chooses random question from medium questions
        #     self.QuestionLabel.config(text=medium[random_question][0])
        # elif random_difficulty[0] == 3:
        #     random_question = random.randint(0,len(hard)-1)#chooses random question from hard questions
        #     self.QuestionLabel.config(text=hard[random_question][0])


    def show_answer(self):
        self.difficulty_button_frame.pack() # shows difficulty buttons when show answer button is pressed
        # displays the correct corresponding answer to the questions when answer button is pressed
        #using database
        self.AnswerLabel.config(text=questions[random_question][1])




        #using lists
        # if random_difficulty[0] == 1: # easy
        #     self.AnswerLabel.config(text=easy[random_question][1]) # updates answer label
        # elif random_difficulty[0] ==2: # medium
        #     self.AnswerLabel.config(text=medium[random_question][1])
        # elif random_difficulty[0] == 3: # hard
        #     self.AnswerLabel.config(text=hard[random_question][1])

    def update_frequency(self, updated_difficulty):
        conn = sqlite3.connect('Users.db')
        c = conn.cursor()
        c.execute("UPDATE flashcards SET difficulty = ? WHERE rowid = ?", (updated_difficulty,questions[random_question][3])) # updates the difficulty of the question by using its rowid

        conn.commit()
        conn.close()
