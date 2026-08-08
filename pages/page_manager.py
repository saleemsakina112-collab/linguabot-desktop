class PageManager:
    def __init__(self, app):
        self.app = app
        self.current_page = None

    def show_page(self, page_class):

        if self.current_page is not None:
            self.current_page.frame.pack_forget()

        self.current_page = page_class(self.app, self)
