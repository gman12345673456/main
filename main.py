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
import re

# Global score variable
global_score = 0

def copy_to_clipboard(event):
    app.copy_to_clipboard(text_box.text)

def on_text_change(event):
    global global_score
    text = text_box.text
    message = ""
    all_conditions_met = True

    # Reset the score
    global_score = 0

    # Initial check for length
    if len(text) < 8:
        message += "Password must be at least 8 characters long.\n"
        all_conditions_met = False
    elif len(text) > 20:
        message += "Password must not exceed 20 characters.\n"
        global_score -= 10  # Deduct 10 points for exceeding 20 characters
    else:
        global_score += 20

    # Check against list of common passwords
    common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "Password", "Admin"]
    if text in common_passwords:
        message += "This is a common password.\n"
        global_score /= 2  # Deduct half of the score if it's a common password
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

    # Check for exactly one uppercase letter
    capital_count = sum(1 for char in text if 'A' <= char <= 'Z')  # Count uppercase letters
    if capital_count == 1:
        global_score += 20
    else:
        message += "Password must contain exactly one capital letter.\n"
        all_conditions_met = False

    # Check for number limit
    number_count = sum(char.isdigit() for char in text)
    max_number_count = 3  # Maximum number count parameter
    if number_count > max_number_count:
        message += f"No more than {max_number_count} numbers are allowed.\n"
        global_score -= 10  # Deduct 10 points for exceeding 3 numbers
    else:
        global_score += 20

    # Check for at least one lowercase letter
    if any(char.islower() for char in text):
        global_score += 10
    else:
        message += "Password must contain at least one lowercase letter.\n"
        all_conditions_met = False

    # Check for special characters
    special_characters = {'&', '%', '$', '@', '!', '*', '^', '#', '()', '[]', '_', '-', '+', '~', '`'}
    if any(character in special_characters for character in text):
        global_score += 10
    else:
        message += "Password must contain at least one special character.\n"
        all_conditions_met = False

    # Cap the global score at 100
    if global_score > 100:
        global_score = 100

    # Prevent negative scores
    if global_score < 0:
        global_score = 0

    # Generate the security message based on the score
    if global_score == 100:
        security_message = "Password is very secure."
    elif global_score >= 80:
        security_message = "Password is secure."
    elif global_score >= 60:
        security_message = "Password is moderately secure."
    elif global_score >= 40:
        security_message = "Password is somewhat secure."
    else:
        security_message = "Password is not secure."

    if all_conditions_met:
        message = f"Password is accepted. {security_message}"
        copy_btn.enabled = True  # Enable the button if all conditions are met
    else:
        copy_btn.enabled = False  # Disable the button if not all conditions are met

    message += f"\nPassword score: {int(global_score)}/100"  # Convert score to int for display
    label.text = message.strip()  # Strip any trailing whitespace

# Create the app
app = gp.GooeyPieApp('Password Checker')

# Create the components
text_box = gp.Textbox(app, 30, 5)
text_box.add_event_listener('change', on_text_change)
label = gp.Label(app, 'Welcome to the Password Protection Checker. Please input your password above ( No Personal information).')
copy_btn = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)
copy_btn.enabled = False  # Initially disable the button

# Set up the grid
app.set_grid(3, 2)
app.set_column_weights(1, 0)
app.add(text_box, 1, 1, valign='middle')
app.add(copy_btn, 1, 2, valign='middle')  # Add the copy button next to the text box
app.add(label, 2, 1, column_span=2)

# Run the app
app.run()

