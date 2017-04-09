import random as rd
import tkinter as tk

fem_celebs = ["Cher", "Cara Delevigne","Carly Rae Japsen",  "Kylie Jenner", "Caitlyn Jenner", "Kim Kardashian", "Ivanka Trump", "Lady Gaga", "Rihanna", "Angela Merkel", "Melanie Müller", "Lucy Cat", "Aklicia Keys", "Ashley Tisdale", "Adele", "Anne Hathaway", "Beyoncé Knowles", "Britney Spears", "Céline Dion", "Cameron Diaz", "Christina Aguilera", "Courtney Cox", "Marylin Monroe", "Ellen DeGeneres", "Ellen Pompeo", "Emma Roberts", "Fergie", "Halle Berry", "Heidi Klum", "Jennifer Aniston", "Jennifer Lawrence", "Jennifer  Lopez", "Jennifer Hudson", "Jessica Simpson", "Julia Roberts", "Princess Kate", "Kate Moss", "Katy Perry", "Kelly Clarkson", "Khloé Kardashian", "Kourtney Kardashian", "Kristen Stewart", "Katja Krasavice", "Lindsey Lohan", "Madonna", "Michelle Obama", "Megan Fox", " Mariah Carey", "Naomi Campbell", "Natalie Portman", "Pamela Anderson", "P!nk", "Penélope Cruz", "Rihanna", "Sandra Bullock", "Scarlet Johansson", "Selena Gomez", "Shakira", "Taylor Swift", "Victoria Beckham", "Ellie Golding", "Gwen Stefani", "Angelinqa Jolie"]
male_celebs = ["Barack Obama", "Benedict Cumberbatch", "Bruno Mars", "Cee Lo Green", "Chris Pratt", "Christiano Ronlado", "Dennis Rodman", "Derek Jeter", "Drake", "Eddie Murphy", "Adam Sandler", "Donald Trump", "Kanye West", "Prince Charles", "Frank Sinatra", "Eminem", "JayZ", "Kim Jong Un", "Adam Levine", "Andrew Garfield", "Bruce Willis", "Nrad Pitt", "Channing Tatum", "Christian Bale", "Chris Brown", "Charlie Sheen", "Daniel Craig", "Daniel Radcliffe", "David Beckham", "Denzel Washington", "George Clooney", "Heath Ledger", "Hugh Jackman", "James Franco", "Johnny Depp", "Justin Bieber", "Justin Timberlake", "Leonardo DiCaprio", "Liam Hemsworth", "Mark Wahlberg", "Matt Damon", "Orlando Bloom", "Patrick Dempsey", "Prince Harry", "Prince William", "Robert Downey Jr.", "Robert Pattinson", "Ryan Gosling", "Ryan Reynolds", "Tiger Woods", "Tom Brady", "Tom Cruise", "Usher", "Will Snith", "Zac Efron", "Simon Desue", "ApoRed", "Robbie Williams", "Kim Jong Il", "Michael Jordan", "Michael B. Jordan", "Morgan Freeman", "John Cena"]
output = []

def men():
    maximal = len(male_celebs) - 1
    for i in range(3):
            random = rd.randint(0, maximal)
            output.append(male_celebs[random])

    out1["height"] = 2
    out2["height"] = 2
    out3["height"] = 2
    out1["text"] = output[0]
    out2["text"] = output[1]
    out3["text"] = output[2]
    for i in range(3):
        output.remove(output[0])

def women():
    maximal = len(fem_celebs) - 1
    for i in range(3):
        random = rd.randint(0, maximal)
        output.append(fem_celebs[random])

    out1["height"] = 2
    out2["height"] = 2
    out3["height"] = 2
    out1["text"] = output[0]
    out2["text"] = output[1]
    out3["text"] = output[2]
    for i in range(3):
        output.remove(output[0])
    
def generate():
    gender = rd.randint(1, 2)

    if gender == 1:
        men()
        
    elif gender == 2:
        women()
        

main = tk.Tk()
main.configure(bg="yellow")
main.title("Marry Fuck Kill")

inst = tk.Label(main, width="60", height = "2", bg="black", fg="white", text="Click the 'Enter' Button to generate 3 Celebritys")
inst.pack()

out1 = tk.Label(main, width="70", height = "0", bg="yellow")
out1.config(font=("Courier", 15))
out1.pack()

out2 = tk.Label(main, width="70", height = "0", bg="yellow")
out2.config(font=("Courier", 15))
out2.pack()

out3 = tk.Label(main, width="70", height = "0", bg="yellow")
out3.config(font=("Courier", 15))
out3.pack()

enter = tk.Button(main, width="30", height = "2", bg="black", fg="white", text="Random Gender", command = generate)
enter.pack(side="bottom")

only_men = tk.Button(main, width="30", height = "2", bg="black", fg="white", text="Only Men", command = men)
only_men.pack(side="left")

only_women = tk.Button(main, width="30", height = "2", bg="black", fg="white", text="Only Women", command = women)
only_women.pack(side="right")

main.mainloop()
