from tkinter import *
from random import *
from tkinter import messagebox
import time
import Database

ANIMALS_WORD = ['DRBI', 'DGO', 'OENDYK', 'GFRIEFA', 'GLOILARTA', 'TAC', 'EHSOR', 'OLIN', 'MYOEKN', 'EEB', 'KDUC',
                'RGFO', 'TPNLEHEA', 'ORCDCIELO', 'POLNIHD', 'LARLIGO', 'EMSUO', 'EGTRI', 'ABRITB', 'ATR', ]

ANIMALS_ANSWER = ['BIRD', 'DOG', 'DONKEY', 'GIRAFFE', 'ALLIGATOR', 'CAT', 'HORSE', 'LION', 'MONKEY', 'BEE', 'DUCK',
                  'FROG', 'ELEPHANT', 'CROCODILE', 'DOLPHIN', 'GORILLA', 'MOUSE', 'TIGER', 'RABBIT', 'RAT', ]

ran_num = randrange(0, (len(ANIMALS_WORD)))
jumbled_rand_word = ANIMALS_WORD[ran_num]

points = 0
flag=0

def main():
    def end_game():
    	Database.updatescore('abc',points)
    	lab_img1.destroy()
    	word.destroy()
    	get_input.destroy()
    	submit.destroy()
    	change.destroy()
    	ans.destroy()
    	ans_lab.destroy()
    	ans_lab1.destroy()
    	score.destroy()
    	fscore = Label(
        	text="",
        	pady=10,
        	bg="#e6fff5",
        	fg="#000000",
        	font="Titillium  14 bold"
    	)
    	fscore.pack(anchor="n",pady=(50, 20))
    	Database.show_score()
    	fscore['text']="Your Score is: "+str(Database.score)
    	start_btn1 = Button(
        	text="Restart", #buttom text
        	width=18, #buttom width
        	borderwidth=8, #
        	fg="#000000", #foreground 
        	bg="green", #background
        	font=("", 13), # 1st argument font style  2nd Parameter font size
        	cursor="spider", #mouse cursor shape
        	command=back,  #function calling
    	)
    	start_btn1.pack(pady=(50, 20))
     	
    def back():
        my_window.destroy()
        Database.updatescore('abc',points)
        import main_start
        main_start.start_main_page()

    def change():
        global ran_num,flag
        ran_num = randrange(0, (len(ANIMALS_WORD)))
        word.configure(text=ANIMALS_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
        ans_lab1.configure(text="")
        flag=flag+1
        if flag > 9:
        	flag=0
        	end_game()

    def cheak():
        global points, ran_num,flag #globally decalring variables
        user_word = get_input.get().upper()
        if user_word == ANIMALS_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Keep it Up!")
            ran_num = randrange(0, (len(ANIMALS_WORD)))
            word.configure(text=ANIMALS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
            ans_lab1.configure(text="")
            flag=flag+1
            if flag > 9:
            	flag=0
            	end_game()
            	
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)
            flag=flag+1
            if flag > 9:
            	end_game()

    def show_answer():
        global points,ran_num
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            txt=ANIMALS_ANSWER[ran_num]
            ran_num = randrange(0, (len(ANIMALS_WORD)))
            word.configure(text=ANIMALS_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text=txt)
            ans_lab1.configure(text="Previous Question Answer")
            
        else:
            ans_lab.configure(text='Not enough points')
            ans_lab1.configure(text="")
           
    
    my_window = Tk()
    my_window.geometry("700x700+500+150")
    my_window.resizable(0, 0)
    my_window.title("Jumbled Words Quiz")
    my_window.configure(background="#e6fff5")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='#e6fff5',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        	text="Score:- 0",
        	pady=10,
        	bg="#e6fff5",
        	fg="#000000",
        	font="Titillium  14 bold"
    	)
    score.pack(anchor="n")
    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#e6fff5",
        fg="#000000",
        font="Titillium  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="#99ffd6",
        command=cheak,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    
    ans_lab.pack()
    
    ans_lab1 = Label(
        text="",
        bg="#e6fff5",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab1.pack()
    

    my_window.mainloop()
