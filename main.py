import json
from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
FONT = ('Arial', 8)

screen = Tk()
screen.title('Password Manager')
screen.minsize(width=500, height=500)
screen.config(padx=50, pady=50)

def generate():
	password = generate_password()
	password_entry.delete(0, 'end')
	password_entry.insert(0, password)

def save():
	website = website_entry.get()
	user = user_entry.get()
	password = password_entry.get()
	is_ok = website and user and password
	if is_ok:
		try:
			with open ("passwords.json", "r") as f:
				data = json.load(f)
		except:
			with open("passwords.json", 'w') as f:
				data = {}
		data[website] = {"Email/Username": user, "Password": password}
	
		if messagebox.askyesno(message=f'Do you want to save following information: Website: {website}, Email/Username: {user}, Password: {password}?'):
			with open("passwords.json", "w") as f:
				json.dump(data, f, indent=4)
			website_entry.delete(0, 'end')
			password_entry.delete(0, 'end')
	else:
		messagebox.showinfo(title="WTF?", message='FILL EVERYTHING!!!')

def search():
	website = website_entry.get()
	not_found = True
	try:
		with open ("passwords.json", "r") as f:
			data = json.load(f)
		for web in data:
			if web.lower() == website.lower():
				messagebox.showinfo(title="Search Result", message=f"Email/Username: {data[web]['Email/Username']}\nPassword: {data[web]['Password']}")
				not_found = False
				break
		if not_found:
			messagebox.showinfo(title="Search Result", message="Information Not Found")
	except:
		messagebox.showerror(title="Error", message=f"No Data File Found")

logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

generate_button = Button(text="Search", command=search, width=20)
generate_button.grid(row=1, column=2)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

user_entry = Entry(width=60)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "pakdenis458@gmail.com")

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate, width=20)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=51)
add_button.grid(row=4, column=1, columnspan=2)

screen.mainloop()