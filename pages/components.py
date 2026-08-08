import customtkinter as ctk


def create_home_button(parent, page_manager):

    from pages.home import HomePage

    button = ctk.CTkButton(
        parent,
        text="🏠 Home",
        width=200,
        height=40,
        command=lambda: page_manager.show_page(HomePage)
    )

    button.pack(
        pady=(20, 10)
    )

    return button
