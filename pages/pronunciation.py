import customtkinter as ctk

from pages.base_page import BasePage
from pages.components import create_home_button
from services.pronunciation_service import pronounce_text


class PronunciationPage(BasePage):

    def __init__(self, app, page_manager):

        self.card = self.create_layout(app)

        title = ctk.CTkLabel(
            self.card,
            text="🎤 Pronunciation",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=30)

        self.input_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Type here...",
            width=300
        )
        self.input_entry.pack(pady=10)

        self.languages = {
            "English": "en",
            "German": "de",
            "French": "fr",
            "Spanish": "es",
            "Italian": "it",
            "Portuguese": "pt",
            "Japanese": "ja",
            "Korean": "ko",
            "Chinese": "zh-CN",
            "Hindi": "hi",
            "Urdu": "ur"
        }

        self.language_menu = ctk.CTkOptionMenu(
            self.card,
            values=list(self.languages.keys())
        )

        self.language_menu.pack(pady=10)

        self.pronounce_button = ctk.CTkButton(
            self.card,
            text="Pronounce",
            command=self.pronounce
        )
        self.pronounce_button.pack(pady=20)

        self.message = ctk.CTkLabel(
            self.card,
            text=""
        )

        self.message.pack(pady=10)

        create_home_button(
            self.card,
            page_manager
        )

    def pronounce(self):

        text = self.input_entry.get().strip()

        if not text:
            self.message.configure(
                text="Please enter some text.",
                text_color="orange"
            )
            return

        language = self.languages[self.language_menu.get()]

        success = pronounce_text(text, language)

        if success:
            self.message.configure(
                text="🔊 Pronunciation is playing...",
                text_color="green"
            )
        else:
            self.message.configure(
                text="❌ Pronunciation failed. Please try again.",
                text_color="red"
            )

        self.input_entry.delete(0, "end")
