import customtkinter as ctk
from pages.translate import TranslatePage
from pages.vocabulary import VocabularyPage
from pages.quiz import QuizPage
from pages.pronunciation import PronunciationPage
from pages.view_vocabulary import ViewVocabularyPage
from pages.flashcards import FlashcardsPage


class HomePage:
    def __init__(self, app, page_manager):

        self.frame = ctk.CTkFrame(app)

        self.page_manager = page_manager

        self.frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=40
        )

        self.title = ctk.CTkLabel(
            self.frame,
            text="LinguaBot",
            font=("Arial", 32, "bold")
        )

        self.title.pack(pady=(20, 40))

        buttons = {
            "➕ Add Vocabulary": VocabularyPage,
            "📖 View Vocabulary": ViewVocabularyPage,
            "📚 Flashcards": FlashcardsPage,
            "📝 Take Quiz": QuizPage,
            "🌍 Translate": TranslatePage,
            "🎤 Pronunciation": PronunciationPage
        }

        for text, page in buttons.items():
            button = ctk.CTkButton(
                self.frame,
                text=text,
                command=lambda page=page: self.page_manager.show_page(page),
                height=45
            )

            button.pack(
                pady=12,
                padx=50,
                fill="x"
            )
