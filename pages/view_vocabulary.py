import customtkinter as ctk
from pages.base_page import BasePage
from pages.components import create_home_button
from services.vocabulary_service import load_words, save_words


class ViewVocabularyPage(BasePage):

    def __init__(self, app, page_manager):

        self.app = app
        self.page_manager = page_manager

        self.card = self.create_layout(app)

        title = ctk.CTkLabel(
            self.card,
            text="📖 View Vocabulary",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=(20, 30))

        self.search_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Search word...",
            width=300
        )

        self.search_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(
            self.card,
            text="🔍 Search",
            command=self.search_words
        )

        self.search_button.pack(pady=10)

        self.search_message = ctk.CTkLabel(
            self.card,
            text=""
        )

        self.search_message.pack(pady=5)

        self.edit_word_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Edit word",
            width=300
        )

        self.edit_word_entry.pack(pady=5)

        self.edit_meaning_entry = ctk.CTkEntry(
            self.card,
            placeholder_text="Edit meaning",
            width=300
        )

        self.edit_meaning_entry.pack(pady=5)

        self.save_edit_button = ctk.CTkButton(
            self.card,
            text="💾 Save Changes",
            command=self.save_edit
        )

        self.save_edit_button.pack(pady=10)

        self.edit_word_entry.configure(
            state="disabled"
        )

        self.edit_meaning_entry.configure(
            state="disabled"
        )
        self.words = load_words()

        if not self.words:

            label = ctk.CTkLabel(
                self.card,
                text="No vocabulary saved yet."
            )

            label.pack(pady=20)

        else:
            self.list_frame = ctk.CTkFrame(
                self.card
            )

            self.list_frame.pack(
                fill="both",
                expand=True,
                pady=10
            )

            for entry in self.words:

                row = ctk.CTkFrame(
                    self.list_frame
                )

                row.pack(
                    pady=5,
                    padx=20,
                    fill="x"
                )

                word_label = ctk.CTkLabel(
                    row,
                    text=f"{entry['word']} : {entry['meaning']}",
                    font=("Arial", 18)
                )

                word_label.pack(
                    side="left",
                    padx=10
                )

                edit_button = ctk.CTkButton(
                    row,
                    text="✏ Edit",
                    width=80,
                    command=lambda e=entry: self.edit_word(e)
                )

                edit_button.pack(
                    side="right",
                    padx=5
                )

                delete_button = ctk.CTkButton(
                    row,
                    text="🗑 Delete",
                    width=80,
                    command=lambda e=entry: self.delete_word(e)
                )

                delete_button.pack(
                    side="right",
                    padx=10
                )

        create_home_button(
            self.card,
            page_manager
        )

    def delete_word(self, entry):

        self.words.remove(entry)

        save_words(self.words)

        self.page_manager.show_page(ViewVocabularyPage)

    def search_words(self):

        query = self.search_entry.get().strip().lower()

        for widget in self.list_frame.winfo_children():
            widget.destroy()

        found = False

        for entry in self.words:

            if (
                query in entry["word"].lower()
                or query in entry["meaning"].lower()
            ):

                found = True

                row = ctk.CTkFrame(
                    self.list_frame
                )

                row.pack(
                    pady=5,
                    padx=20,
                    fill="x"
                )

                label = ctk.CTkLabel(
                    row,
                    text=f"{entry['word']} : {entry['meaning']}",
                    font=("Arial", 18)
                )

                label.pack(
                    side="left",
                    padx=10
                )

                delete_button = ctk.CTkButton(
                    row,
                    text="🗑 Delete",
                    width=80,
                    command=lambda e=entry: self.delete_word(e)
                )

                delete_button.pack(
                    side="right",
                    padx=10
                )

        if found:
            self.search_message.configure(text="")
        else:
            self.search_message.configure(
                text="No matching words found.",
                text_color="orange"
            )

    def edit_word(self, entry):

        self.editing_word = entry

        self.edit_word_entry.configure(
            state="normal"
        )

        self.edit_meaning_entry.configure(
            state="normal"
        )

        self.edit_word_entry.delete(0, "end")
        self.edit_meaning_entry.delete(0, "end")

        self.edit_word_entry.insert(
            0,
            entry["word"]
        )

        self.edit_meaning_entry.insert(
            0,
            entry["meaning"]
        )

    def save_edit(self):

        if not hasattr(self, "editing_word"):
            return

        new_word = self.edit_word_entry.get().strip().lower()
        new_meaning = self.edit_meaning_entry.get().strip().lower()

        if not new_word or not new_meaning:
            return

        self.editing_word["word"] = new_word
        self.editing_word["meaning"] = new_meaning

        save_words(self.words)

        self.edit_word_entry.configure(
            state="disabled"
        )

        self.edit_meaning_entry.configure(
            state="disabled"
        )

        self.page_manager.show_page(ViewVocabularyPage)
