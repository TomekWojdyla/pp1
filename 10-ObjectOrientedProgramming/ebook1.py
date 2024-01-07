class ebook():
    def __init__(self, title,author,number_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = number_of_pages
        self.current_page = 1
        self.is_open = False
    def open_ebook(self):
        self.is_open = True
    def close_ebook(self):
        self.is_open = False
    def change_page_up(self):
        if self.is_open == True and self.current_page < self.no_of_pages:
            self.current_page +=1
        elif self.is_open == True and self.current_page == self.no_of_pages:
            print(f"You are at the last page!")
        else:
            print(f"Book is closed. Cannot change the page.")
    def change_page_down(self):
        if self.is_open == True and self.current_page > 2:
            self.current_page -=1
        elif self.is_open == True and self.current_page == 1:
            print(f"You are at the first page!")
        else:
            print(f"Book is closed. Cannot change the page.")
    def status(self):
        print(f"You are in page: {self.current_page}")