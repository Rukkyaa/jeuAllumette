
def placement_allumette (canvas, image, number, remove):
    number -= remove
    for i in range (0, number):
        canvas.create_image(50+(i*30), 50, image=image)

def lose():
    widgets = [title, canvas, allumettes]
    actualPlayer = player.cget("text")
    for i in widgets:
        i.grid_forget()

    titlee = tk.Label(main_frame, bg = "grey",fg = "red", text= "Le {} a perdu !".format(actualPlayer), font = ("Helvetica", 25))
    titlee.grid(row = 0, column = 0, pady = 200)