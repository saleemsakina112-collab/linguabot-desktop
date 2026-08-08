import customtkinter as ctk
from pages.base_page import BasePage
from pages.components import create_home_button
from services.translate_service import translate_text


class TranslatePage(BasePage):

    def __init__(self, app, page_manager):

        self.card = self.create_layout(app)

        title = ctk.CTkLabel(
            self.card,
            text="🌍 Translate",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=(20, 30))

        self.languages = {
            "English": "en",
            "German": "de",
            "French": "fr",
            "Spanish": "es",
            "Italian": "it",
            "Portuguese": "pt",
            "Dutch": "nl",
            "Russian": "ru",
            "Ukrainian": "uk",
            "Polish": "pl",
            "Turkish": "tr",
            "Arabic": "ar",
            "Hindi": "hi",
            "Urdu": "ur",
            "Chinese (Simplified)": "zh-CN",
            "Chinese (Traditional)": "zh-TW",
            "Japanese": "ja",
            "Korean": "ko",
            "Greek": "el",
            "Swedish": "sv",
            "Norwegian": "no",
            "Danish": "da",
            "Finnish": "fi",
            "Czech": "cs",
            "Hungarian": "hu",
            "Romanian": "ro",
            "Bulgarian": "bg",
            "Thai": "th",
            "Vietnamese": "vi",
            "Indonesian": "id",
            "Malay": "ms"
        }

        ctk.CTkLabel(
            self.card,
            text="From"
        ).pack()

        self.source_menu = ctk.CTkOptionMenu(
            self.card,
            values=sorted(self.languages.keys())
        )

        self.source_menu.pack(pady=5)

        ctk.CTkLabel(
            self.card,
            text="To"
        ).pack()

        self.target_menu = ctk.CTkOptionMenu(
            self.card,
            values=sorted(self.languages.keys())
        )

        self.target_menu.set("German")
        self.target_menu.pack(pady=5)

        self.input_box = ctk.CTkTextbox(
            self.card,
            width=500,
            height=80
        )

        self.input_box.pack(pady=10)

        self.translate_button = ctk.CTkButton(
            self.card,
            text="Translate",
            command=self.translate
        )

        self.translate_button.pack(pady=20)

        self.output_box = ctk.CTkTextbox(
            self.card,
            width=500,
            height=80
        )

        self.output_box.pack(pady=10)
        self.output_box.configure(state="disabled")

        create_home_button(
            self.card,
            page_manager
        )

    def translate(self):

        text = self.input_box.get("1.0", "end").strip()

        if not text:
            self.output_box.configure(state="normal")
            self.output_box.delete("1.0", "end")
            self.output_box.insert("1.0", "Please enter some text.")
            self.output_box.configure(state="disabled")
            return

        source = self.languages[self.source_menu.get()]
        target = self.languages[self.target_menu.get()]

        result = translate_text(text, source, target)

        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("1.0", result)
        self.output_box.configure(state="disabled")

        self.input_box.delete("1.0", "end")
