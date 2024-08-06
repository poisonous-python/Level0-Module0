from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    q1=simpledialog.askstring(title= "Question 1/10", prompt= "How many days are there in a year?")
    #      // 3.  Use an if statement to check if their answer is correct
    if q1=="365":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: 365")
    #      // 4.  if the user's answer was correct, add one to their score 
    q2= simpledialog.askstring(title="Question 2/10", prompt= "How many moons does Jupiter have?")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    if q2=="95":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message= "Uh oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: 95")
    q3=simpledialog.askstring(title="Question 3/10", prompt="What is the tallest mountain in the world?\n"+"(remember to capitalize!)")
    if q3=="Mount Everest":
        score+=1
        messagebox.showinfo(message="Correct\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: Mount Everest")
    q4=simpledialog.askstring(title="Question 4/10", prompt="Where are the 2028 Olympics being held?\n"+"(Don't Abbreviate!)")
    if q4=="Los Angeles":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: Los Angeles")
    q5=simpledialog.askstring(title="Question 5/10", prompt="What is the density of water?\n"+"(use g/mL format)")
    if q5=="1 g/mL":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer\n"+"-1 point\n"+"Correct Answer: 1 g/mL")
    q6=simpledialog.askstring(title="Question 6/10", prompt="what is the equation for density?\n"+"(spell it out, no capitals)")
    if q6=="mass/volume":
        score+=1
        messagebox.showinfo(message="Correct!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: mass/volume")
    q7=simpledialog.askstring(title="Question 7/10", prompt="Which planet in our solar system is closest to the sun?")
    if q7=="Mercury":
        score+=1
        messagebox.showinfo(message="Correct Answer!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: Mercury")
    q8=simpledialog.askstring(title="Question 8/10", prompt="What is the smallest state in the United States of America?")
    if q8=="Rhode Island":
        score+=1
        messagebox.showinfo(message="Correct Answer!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: Rhode Island")
    q9=simpledialog.askstring(title="Question 9/10", prompt="what is the speed of sound in air?\n"+"(m/s format)")
    if q9=="343 m/s":
        score+=1
        messagebox.showinfo(message="Correct Answer!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point"+"Correct Answer: 343 m/s")
    q10=simpledialog.askstring(title="Question 10/10", prompt="What planet is farthest from the EARTH?")
    if q10=="Neptune":
        score+=1
        messagebox.showinfo(message="Correct Answer!\n"+"+1 point")
    else:
        score-=1
        messagebox.showinfo(message="Uh Oh! Wrong Answer!\n"+"-1 point\n"+"Correct Answer: Neptune")
    bonus=simpledialog.askstring(title="Bonus Question worth 5 pts", prompt="What is the speed of light?\n"+"(m/s format)")
    if bonus=="299,792,458 m/s":
        score+=5
        messagebox.showinfo(message="WOW! Correct Answer!\n"+"+5 points!")
    else:
        messagebox.showinfo(message="Wrong Answer!\n"+"No penalty\n"+"Correct Answer: 299,792,458 m/s")

    messagebox.showinfo(message="Finish!\n"+"Your score is:\n"+str(score)+"/10"+"\nGood Job!")
    window.mainloop()
    # After all the questions have been asked, tell the use their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
