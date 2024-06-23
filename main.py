import gooeypie as gp  # Assuming gooeypie library is used for GUI

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
        global_score = 0  # Reset score to 0 if password is over 20 characters
        all_conditions_met = False
    else:
        global_score += 20

    # Check against list of common passwords
    common_passwords = [ 
        "Password", "password", "Qwerty12", "Abcdefg1", "Letmein1", "Monkey12", "Sunshine", 
        "Admin123", "Welcome1", "Iloveyou", "Princess", "Football", "Dragon12", 
        "Shadow12", "Master12", "Trustno1", "Whatever", "Freedom1", "Qwertyui", 
        "Starwars", "Hello123", "Secret12", "Baseball", "Cheese12", "Jessica1", 
        "Magic123", "Charlie1", "Michael1", "Cookie12", "Banana12", "Maggie12" 
    ]

    if text in common_passwords:
        message += "This is a common password.\n"
        global_score -= 30  # Deduct 30 points for common passwords
        all_conditions_met = False

    # Check for exactly one uppercase letter
    capital_count = sum(1 for char in text if 'A' <= char <= 'Z')  # Count uppercase letters
    if capital_count == 1:
        global_score += 20
    else:
        message += "Password must contain exactly one capital letter.\n"
        all_conditions_met = False

    # Check for number limit (up to 3 digits)
    number_count = sum(char.isdigit() for char in text)
    if number_count <= 3:
        global_score += 20
    else:
        message += "No more than 3 digits are allowed.\n"
        global_score = 0  # Reset score to 0 if more than 3 digits
        all_conditions_met = False

    # Check for at least one lowercase letter
    if any(char.islower() for char in text):
        global_score += 20
    else:
        message += "Password must contain at least one lowercase letter.\n"
        all_conditions_met = False

    # Check for at least one special character
    special_characters = {'&', '%', '$', '@', '!', '*', '^', '#', '()', '[]', '_', '-', '+', '~', ''}
    if any(character in special_characters for character in text):
        global_score += 20
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
        copy_btn.enabled = True  # Enable the button if score is exactly 100
    elif global_score >= 80:
        security_message = "Password is secure."
        copy_btn.enabled = True  # Enable the button if score is between 80-99
    elif global_score >= 60:
        security_message = "Password is moderately secure."
        copy_btn.enabled = False  # Disable the button if score is less than 80
    elif global_score >= 40:
        security_message = "Password is somewhat secure."
        copy_btn.enabled = False  # Disable the button if score is less than 80
    else:
        security_message = "Password is not secure."
        copy_btn.enabled = False  # Disable the button if score is less than 80

    if all_conditions_met and global_score >= 80:
        message = f"Password is accepted. {security_message}"
    else:
        copy_btn.enabled = False  # Disable the button if not all conditions are met

    message += f"\nPassword score: {int(global_score)}/100"  # Convert score to int for display
    label.text = message.strip()  # Strip any trailing whitespace

app = gp.GooeyPieApp('Password Checker')
app.width = 300
app.height = 450  # Adjusted height to make it more like a portrait rectangle

# Create the components
text_box = gp.Textbox(app, 30, 5)
text_box.add_event_listener('change', on_text_change)
label = gp.Label(app, 'Welcome to the Password Protection Checker 🔒.')
copy_btn = gp.Button(app, 'Copy to Clipboard', copy_to_clipboard)
copy_btn.enabled = False  # Initially disable the button

# Set up the grid
app.set_grid(4, 1)
app.set_column_weights(1)
app.add(label, 1, 1, align='center')
app.add(text_box, 2, 1, align='center')
app.add(copy_btn, 3, 1, align='center')

# Run the app
app.run()



