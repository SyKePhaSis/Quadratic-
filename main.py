from tkinter import *
import numpy as np
import types

# AUTHOR: LEONIDAS CRASSARIS #
# DATE: 27/2/2021 #
# FINISHED #

EQ = []
SOL = []

class window():
    
    def createWin():
        
        global CO_IN_1,CO_IN_2,CO_IN_3, WIN, FONT
        
        ### VARS ### 
        
        HEIGHT = 400
        WIDTH = 400
        FONT = "Courier"
        
        ### CREATE WINDOW ###
        
        WIN = Tk(baseName="ES")
        WIN.geometry("800x400")
        
        ### MODIFY WINDOW ##
        
            # TITLE #
            
        TITLE = Label(WIN, text="EQUATION SOLVER")
        TITLE.config(font=(FONT, 44))
        TITLE.grid(row=0, column=2)

            # COEFFICIENTS #
            
            #1#
            
        CO_LBL = Label(WIN, text="Coefficient 1")
        CO_LBL.config(font=(FONT,15))
        CO_LBL.grid(row=1, column=1)
        
        CO_IN_1 = Entry(WIN, width=10)
        CO_IN_1.grid(row=1, column=2)
        
            #2#
        
        CO_LBL = Label(WIN, text="Coefficient 2")
        CO_LBL.config(font=(FONT,15))
        CO_LBL.grid(row=2, column=1)
        
        CO_IN_2 = Entry(WIN, width=10)
        CO_IN_2.grid(row=2, column=2)
        
            #3#
        
        CO_LBL = Label(WIN, text="Coefficient 3")
        CO_LBL.config(font=(FONT,15))
        CO_LBL.grid(row=3, column=1)

        CO_IN_3 = Entry(WIN, width=10)
        CO_IN_3.grid(row=3, column=2)
        
            # BUTTON #
        
        BUTTON = Button(WIN, text="Create Equation", width=20, command=window.getInput)
        BUTTON.config(font=(FONT,12,'bold'))
        BUTTON.grid(row=4, column=2, pady = 10)
        
            # CREATED EQUATIONS # 
            
        EQ_TITLE = Label(WIN, text="Created Equation")
        EQ_TITLE.config(font=(FONT,30))
        EQ_TITLE.grid(row=5, column=2, pady = 10)
        
        WIN.mainloop()
        
    def getInput():
        CO_EF  = [CO_IN_1.get(), CO_IN_2.get(), CO_IN_3.get()]
        EQ.append(f"{CO_IN_1.get()}x^2 {CO_IN_2.get()}x {CO_IN_3.get()}")
        SOL.append(main.checkComplex(main.estimateRoots(CO_EF)))
        for i in range(len(EQ)):
            EQ_ = Label(WIN, text=f"{EQ[i]}, Roots: {SOL[i]}")
            EQ_.config(font=(FONT,15))
            EQ_.grid(row=6+i, column=2, pady = 5)
        
class main():
    
    def estimateRoots(CO_EF):
        CO_EF = np.array(CO_EF, float)
        ROOTS = np.roots(CO_EF)
        return ROOTS
    
    def checkComplex(ROOTS):
        for n in range(len(ROOTS)):
            ROOTS = list(ROOTS)
            if (str(ROOTS[n]))[-2] == "j":
                ROOT = "Answer is a complex number!"
                ROOTS[n] = ROOT
        return ROOTS
        
if __name__ == "__main__":
    window.createWin()


