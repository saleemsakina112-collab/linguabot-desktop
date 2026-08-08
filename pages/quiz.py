import customtkinter as ctk
import random
from pages.base_page import BasePage
from pages.components import create_home_button
from services.vocabulary_service import load_words


import customtkinter as ctk
import random

from pages.base_page import BasePage
from pages.components import create_home_button
from services.vocabulary_service import load_words


class QuizPage(BasePage):

    def __init__(self, app, page_manager):

        self.card = self.create_layout(app)

        self.words = load_words()

        if not self.words:
            label = ctk.CTkLabel(
                self.card,
                text="No vocabulary found. Please add some words first."
            )
            label.pack(pady=40)
            return

        title = ctk.CTkLabel(
            self.card,
            text="📝 Vocabulary Quiz",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=(15, 5))

        quiz_size = min(5, len(self.words))
        self.quiz_words = random.sample(self.words, quiz_size)
        self.question_number = 0
        self.score = 0
        self.answered = False

        self.current_word = self.quiz_words[self.question_number]

        self.question_label = ctk.CTkLabel(
            self.card,
            text=f"Question 1/{len(self.quiz_words)}",
            font=("Arial", 20, "bold")
        )

        self.question_label.pack(pady=(5, 5))

        self.progress = ctk.CTkProgressBar(
            self.card,
            width=280
        )
        self.progress.pack(pady=(0, 8))
        self.progress.set(0)

        self.score_label = ctk.CTkLabel(
            self.card,
            text="Score: 0",
            font=("Arial", 16)
        )
        self.score_label.pack(pady=(0, 15))
        self.word_label = ctk.CTkLabel(
            self.card,
            text=self.current_word["word"],
            font=("Arial", 42, "bold")
        )

        self.word_label.pack(pady=(15, 10))

        self.meaning_label = ctk.CTkLabel(
            self.card,
            text="Meaning:"
        )
        self.meaning_label.pack(pady=(5, 5))

        self.answer_entry = ctk.CTkEntry(
            self.card,
            width=350,
            placeholder_text="Type the meaning..."
        )

        self.answer_entry.pack(pady=10)

        self.check_button = ctk.CTkButton(
            self.card,
            text="Check Answer",
            command=self.check_answer
        )

        self.check_button.pack(
            pady=10,
            padx=100,
            fill="x"
        )

        self.next_button = ctk.CTkButton(
            self.card,
            text="Next Question",
            command=self.next_question
        )
        self.next_button.configure(state="disabled")
        self.next_button.pack(
            pady=10,
            padx=100,
            fill="x"
        )

        self.message = ctk.CTkLabel(
            self.card,
            text=""
        )
        self.message.pack(pady=10)

        create_home_button(
            self.card,
            page_manager
        )

    def check_answer(self):

        if self.answered:
            return

        answer = self.answer_entry.get().strip().lower()

        if not answer:
            self.message.configure(
                text="Please enter an answer.",
                text_color="orange"
            )
            return

        if answer == self.current_word["meaning"].lower():
            self.score += 1

            self.score_label.configure(
                text=f"Score: {self.score}"
            )

            self.message.configure(
                text="✅ Correct!",
                text_color="green"
            )

        else:
            self.message.configure(
                text=f"❌ Incorrect! Correct answer: {self.current_word['meaning']}",
                text_color="red"
            )

        self.answered = True

        self.answer_entry.delete(0, "end")
        self.answer_entry.focus()

        self.check_button.configure(
            state="disabled"
        )

        self.next_button.configure(
            state="normal"
        )

    def next_question(self):

        self.question_number += 1

        if self.question_number >= len(self.quiz_words):
            self.progress.set(1)
            self.word_label.configure(text="Quiz Finished!")

            self.question_label.configure(
                text=f"Final Score: {self.score}/{len(self.quiz_words)}"
            )

            self.message.configure(
                text=f"🎉 You scored {self.score}/{len(self.quiz_words)}!",
                text_color="green"
            )

            self.answer_entry.configure(state="disabled")
            self.check_button.configure(state="disabled")
            self.next_button.configure(state="disabled")

            return

        self.current_word = self.quiz_words[self.question_number]

        self.current_word = self.quiz_words[self.question_number]

        self.question_label.configure(
            text=f"Question {self.question_number + 1}/{len(self.quiz_words)}"
        )

        self.progress.set(
            self.question_number / len(self.quiz_words)
        )

        self.check_button.configure(state="normal")

        self.answered = False
        self.word_label.configure(
            text=self.current_word["word"]
        )

        self.message.configure(text="")

        self.answer_entry.delete(0, "end")
