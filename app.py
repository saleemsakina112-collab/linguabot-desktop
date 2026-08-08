import customtkinter as ctk

from pages.home import HomePage
from pages.page_manager import PageManager


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


app = ctk.CTk()

app.title("LinguaBot")
app.geometry("1000x750")
app.minsize(900, 700)

page_manager = PageManager(app)

page_manager.show_page(HomePage)


app.mainloop()
