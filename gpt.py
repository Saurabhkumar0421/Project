self.search_entry = Entry(DataFrameRight, font=("arial", 12, "bold"), width=20)
self.search_entry.grid(row=1, column=0, padx=4)

def search_books(event=None):
    search_query = self.search_entry.get().lower()
    listBox.delete(0, END)  
    for item in listBooks:
        if search_query in item.lower():
            listBox.insert(END, item)


self.search_entry.bind("<KeyRelease>", search_books)
