# import gooeypie as gp


# app = gp.GooeyPieApp("Hello!")

# app.width = 600
# app.height = 400
# app.title = "Password Checker"

# app.set_grid(2,1)

# def submit(event):
#     lbl.text = "I work"

# btn = gp.Button(app, "Submit", submit)
# lbl = gp.Label(app, "This is a label")

# app.add(btn, 1,1)
# app.add(lbl,2,1)
# app.run()

# import gooeypie as gp
# from random import choice
# import time

# responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.',
#              'As I see it, yes.', 'Most likely.', 'Outlook good.',
#              'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
#              'Don\'t count on it.', 'My reply is no.', 'My sources say no.']


# def ask(event):
#     thinking_pb.value = 0
#     answer_lbl.text = ''
#     for steps in range(20):
#         thinking_pb.value += 5
#         app.refresh()
#         time.sleep(0.02)
#     answer_lbl.text = choice(responses)
#     question_inp.focus()


# app = gp.GooeyPieApp('Magic 8 Ball')

# question_inp = gp.Input(app)
# question_inp.width = 50
# ask_btn = gp.Button(app, 'Ask', ask)
# thinking_pb = gp.Progressbar(app)
# answer_lbl = gp.StyleLabel(app, '')
# answer_lbl.font_size = 20
# answer_lbl.align = 'center'

# app.set_grid(3, 2)
# app.set_column_weights(1, 0)
# app.add(question_inp, 1, 1, valign='middle')
# app.add(ask_btn, 1, 2, valign='middle')
# app.add(thinking_pb, 2, 1, column_span=2, fill=True)
# app.add(answer_lbl, 3, 1, column_span=2, fill=True)

# app.run()





# import gooeypie as gp

# def on_text_change(event):
#     text = text_box.text
#     print(text)

#     # run the logic for checks
#     # ren check for length
#     if len(text) < 7:
#         label.text = "Password above 7 characters"
#     else:
#         label.text = "Password is accepted"

# # Check against list of common passwords
#     common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "Password", "Admin"]
#     if text in common_passwords:
#         label.text = "This is a common password."
    

#     # Specific name checks
#     if text == "060207":
#         label.text = "No personal dates"
#     elif text == "Gus simmonds":
#         label.text = "No full name"
#     elif text == "Gus":
#         label.text = "Under 10 not accepted no name"
#     elif text == "2007":
#         label.text = "No birth year"
#     # check for symbols
# # Check for invalid symbols
#     invalid_symbols = {'&', '%', '$', '@', '!', '*', '^'}
#     if any(character in invalid_symbols for character in text):
#         label.text = "Not valid use of text (No symbols)."

 


# app = gp.GooeyPieApp('Might be useful code for your assessment')

# text_box = gp.Textbox(app, 60, 10)
# text_box.add_event_listener('change', on_text_change)

# label = gp.Label(app, 'blank')


# # Creating a larger grid size
# app.set_grid(4, 2)  # Changed grid size to 4x1

# # Adding the elements to the grid
# app.add(text_box, 1, 1)
# app.add(label, 2, 1)

# app.run()

import gooeypie as gp
import time

def update_progress_bar():
    thinking_pb.value = 0
    for steps in range(20):
        thinking_pb.value += 5
        app.refresh()
        time.sleep(0.02)

def on_text_change(event):
    text = text_box.text
    print(text)

    # run the logic for checks
    if len(text) < 7:
        label.text = "Password above 7 characters"
    else:
        label.text = "Password is accepted"

    # Check against list of common passwords
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "Password", "Admin"]
    if text in common_passwords:
        label.text = "This is a common password."
    
    # Specific name checks
    if text == "060207":
        label.text = "No personal dates"
    elif text == "Gus simmonds":
        label.text = "No full name"
    elif text == "Gus":
        label.text = "Under 10 not accepted no name"
    elif text == "2007":
        label.text = "No birth year"

    # Check for invalid symbols
    invalid_symbols = {'&', '%', '$', '@', '!', '*', '^'}
    if any(character in invalid_symbols for character in text):
        label.text = "Not valid use of text (No symbols)."

app = gp.GooeyPieApp('Password Checker with Progress Bar')

# Create the components
text_box = gp.Textbox(app, 60, 10)
text_box.add_event_listener('change', on_text_change)
label = gp.Label(app, 'blank')
thinking_pb = gp.Progressbar(app)

# Set up the grid
app.set_grid(3, 2)
app.set_column_weights(1, 0)
app.add(text_box, 1, 1, valign='middle')
app.add(thinking_pb, 2, 1, column_span=2, fill=True)
app.add(label, 3, 1)

app.run()

