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
global score
import gooeypie as gp


def score = score_representation = "- - - - - - - - - -":
for score in password == 100:
    if score == 10 = message += "Secure password"


def check_single_capital(password):
    capital_count = 0
    for char in password:
        if 65 <= ord(char) <= 90:  # ASCII values for 'A' to 'Z'
            capital_count += 1
    return capital_count == 1


def copy_to_clipboard(event):
    if all_conditions_met:
        app.copy_to_clipboard(text_box.text)

def on_text_change(event):
    text = text_box.text
    message = ""
    all_conditions_met = True

    # Initial check for length
    if len(text) < 8:
        message += "Password must be at least 8 characters long.\n"
        all_conditions_met = False
    elif len(text) > 20:
        message += "Password must not exceed 20 characters.\n"
        all_conditions_met = False
    else:
        score = score + 20

    # Check against list of common passwords
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "Password", "Admin"]
    if text in common_passwords:
        message += "This is a common password.\n"
        all_conditions_met = False

    # Specific name checks
    if text == "060207":
        message += "No personal dates.\n"
    elif text == "Gus simmonds":
        message += "No full names.\n"
    elif text == "Gus":
        message += "No short names.\n"
    elif text == "2007":
        message += "No birth years.\n"

    # Check for invalid symbols
    invalid_symbols = {'&', '%', '$', '@', '!', '*', '^', '#', '()'}
    if any(character in invalid_symbols for character in text):
        message += "No symbols allowed in the password.\n"
        all_conditions_met = False

    # Check for exactly one uppercase letter
    if not check_single_capital(text):
        message += "Password must contain exactly one capital letter.\n"
        all_conditions_met = False
    else:
        score = score + 10
    
    


    # Check for number limit
    number_count = sum(char.isdigit() for char in text)
    max_number_count = 3  # Maximum number count parameter
    if number_count > max_number_count:
        message += f"No more than {max_number_count} numbers are allowed.\n"
        all_conditions_met = False


    #score

    if all_conditions_met:
        message = "Password is accepted."
        copy_btn.enabled = True  # Enable the button if all conditions are met
    else:
        copy_btn.enabled = False  # Disable the button if not all conditions are met

    label.text = message.strip()  # Strip any trailing whitespace




app = gp.GooeyPieApp('Password Checker')

# Create the components
text_box = gp.Textbox(app, 30, 5)
text_box.add_event_listener('change', on_text_change)
label = gp.Label(app, 'Welcome to the Password Protection Checker. Please input your password above (must be at least 8 characters long and no personal information).')
copy_btn = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)
copy_btn.enabled = False  # Initially disable the button

# Set up the grid
app.set_grid(3, 2)
app.set_column_weights(1, 0)
app.add(text_box, 1, 1, valign='middle')
app.add(copy_btn, 1, 2, valign='middle')  # Add the copy button next to the text box
app.add(label, 2, 1, column_span=2)

app.run()

