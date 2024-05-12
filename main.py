import gooeypie as gp


app = gp.GooeyPieApp("Hello!")

app.width = 600
app.height = 400
app.title = "Password Checker"

app.set_grid(2,1)

def submit(event):
    lbl.text = "I work"

btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, "This is a label")

app.add(btn, 1,1)
app.add(lbl,2,1)
app.run()