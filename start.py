from app.app import App

if __name__ == "__main__":
    app = App()
    app.title("University Database")
    app.mainloop()
    app.db.close_conn()
