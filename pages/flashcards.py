import customtkinter as ctk
import random

from pages.base_page import BasePage
from pages.components import create_home_button
from services.vocabulary_service import load_words


class FlashcardsPage(BasePage):

    def __init__(self, app, page_manager):

        self.card = self.create_layout(app)

        self.words = load_words()

        if not self.words:

            ctk.CTkLabel(
                self.card,
                text="No vocabulary available."
            ).pack(pady=30)

            create_home_button(
                self.card,
                page_manager
            )
            return

        random.shuffle(self.words)

        self.current_index = 0
        self.current_word = self.words[self.current_index]

        title = ctk.CTkLabel(
            self.card,
            text="📚 Flashcards",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=20)

        self.word_label = ctk.CTkLabel(
            self.card,
            text=self.current_word["word"],
            font=("Arial", 36, "bold")
        )

        self.word_label.pack(pady=30)

        self.meaning_label = ctk.CTkLabel(
            self.card,
            text="",
            font=("Arial", 24)
        )

        self.meaning_label.pack(pady=20)

        self.show_button = ctk.CTkButton(
            self.card,
            text="Show Meaning",
            command=self.show_meaning
        )

        self.show_button.pack(pady=10)

        self.next_button = ctk.CTkButton(
            self.card,
            text="Next Card",
            command=self.next_card
        )

        self.next_button.pack(pady=10)

        create_home_button(
            self.card,
            page_manager
        )

    def show_meaning(self):

        self.meaning_label.configure(
            text=self.current_word["meaning"]
        )

    def next_card(self):

        self.current_index += 1

        if self.current_index >= len(self.words):

            random.shuffle(self.words)
            self.current_index = 0

        self.current_word = self.words[self.current_index]

        self.word_label.configure(
            text=self.current_word["word"]
        )

        self.meaning_label.configure(
            text=""
        )
