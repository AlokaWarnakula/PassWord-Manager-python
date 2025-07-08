from tkinter import *
from tkinter import messagebox
from PasswordGenerator import PasswordGenerator

from PIL import Image, ImageTk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password_give():
    password_entry.delete(0,END)
    ps = PasswordGenerator()
    random_password = ps.get_password(8,4,4)
    password_entry.insert(0,random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def password_saver():
    web_name_get = website_name_entry.get()
    user_name_get = user_name_entry.get()
    password_get = password_entry.get()

    # Check if any field is empty
    if not web_name_get or not user_name_get or not password_get:
        messagebox.showwarning(title="Incomplete Data", message="Please fill in all the fields.")
        return

    # Ask for confirmation before saving
    is_ok_to_add = messagebox.askokcancel(
        title="Info",
        message=f"Details to add:\n"
                f"Website Name: {web_name_get}\n"
                f"User Name: {user_name_get}\n"
                f"Password: {password_get}\n"
                f"Is it okay to add?"
    )

    if is_ok_to_add:
        # Save to file only after confirmation
        with open("password_log.txt", "a") as password_file_saver:
            password_file_saver.write(f"{web_name_get}  |  {user_name_get}  |  {password_get}\n")
        # Clear the entries after saving
        website_name_entry.delete(0, END)
        user_name_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
# tk object make
window = Tk()
window.title("Password Manager")
window.config(pady=10, padx=10, bg="white")

# Image resize
original_image = Image.open("lock2.png")
resize_image = original_image.resize((200, 200))

# Canvas create
canvas = Canvas(width=866, height=650, bg="white", highlightthickness=0)
bgPicture = ImageTk.PhotoImage(resize_image)
canvas.create_image(433, 200, image=bgPicture)
canvas.grid(column=1, row=0)

# Labels
# Website name
website_name = Label(text="Website : ", highlightthickness=0, fg="black", bg="white", font=("Arial", 15, "bold"))
canvas.create_window(250, 350, window=website_name)
# Email/Username
user_name = Label(text="Username : ", highlightthickness=0, fg="black", bg="white", font=("Arial", 15, "bold"))
canvas.create_window(244, 380, window=user_name)
# Password
password = Label(text="Password : ", highlightthickness=0, fg="black", bg="white", font=("Arial", 15, "bold"))
canvas.create_window(244, 410, window=password)

# Entry
# Website name
website_name_entry = Entry(width=35, bg="white", highlightthickness=0, fg="black")
website_name_entry.focus()
website_name_entry.insert(0, "Example website name")
canvas.create_window(450, 350, window=website_name_entry)
# Username
user_name_entry = Entry(width=35, bg="white", highlightthickness=0, fg="black")
user_name_entry.insert(0, "Example name/email")
canvas.create_window(450, 380, window=user_name_entry)
# password
password_entry = Entry(width=21, bg="white", highlightthickness=0, fg="black")
canvas.create_window(388, 410, window=password_entry)

# Buttons
# Generate Password
generate_password_button = Button(text="Generate Password", fg="black", bg="black", font=("Arial", 12, "bold"),
                                  borderwidth=0, highlightthickness=0, relief=FLAT, bd=0,command=random_password_give)
canvas.create_window(580, 410, window=generate_password_button)
# Add button
add_button = Button(text="Add", fg="black", bg="black", font=("Arial", 12, "bold"), width=40, borderwidth=0,
                    highlightthickness=0, relief=FLAT, bd=0,command=password_saver)
canvas.create_window(450, 440, window=add_button)

window.mainloop()
