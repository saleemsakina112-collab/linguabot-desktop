import customtkinter as ctk
from services.vocabulary_service import load_words, add_word
from pages.base_page import BasePage
from pages.components import create_home_button


class VocabularyPage(BasePage):

    def __init__(self, app, page_manager):

        self.card = self.create_layout(app)
        self.words = load_words()

        title = ctk.CTkLabel(
            self.card,
            text="➕ Add Vocabulary",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=(20, 30))

        self.word_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Word",
            width=350
        )
        self.word_entry.pack(pady=10)

        self.meaning_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Meaning",
            width=350
        )
        self.meaning_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(
            self.card,
            text="Add Word",
            command=self.save_word
        )
        self.add_button.pack(pady=20)

        self.message = ctk.CTkLabel(
            self.card,
            text=""
        )
        self.message.pack(pady=10)

        create_home_button(
            self.card,
            page_manager
        )

    def save_word(self):

        word = self.word_entry.get().strip().lower()
        meaning = self.meaning_entry.get().strip().lower()

        if not word or not meaning:
            self.message.configure(
                text="Please enter both a word and its meaning.",
                text_color="orange"
            )
            return

        success = add_word(
            self.words,
            word,
            meaning
        )

        if success:
            self.message.configure(
                text=f"✅ '{word}' added successfully!",
                text_color="green"
            )

            self.word_entry.delete(0, "end")
            self.meaning_entry.delete(0, "end")

        else:
            self.message.configure(
                text="❌ This word already exists.",
                text_color="red"
            )
