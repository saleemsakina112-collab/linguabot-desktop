import customtkinter as ctk


class BasePage:

    def create_layout(self, app):

        self.frame = ctk.CTkFrame(app)

        self.frame.pack(
            fill="both",
            expand=True
        )

        self.card = ctk.CTkFrame(
            self.frame,
            corner_radius=20
        )

        self.card.pack(
            padx=40,
            pady=30,
            fill="both",
            expand=True
        )

        return self.card
