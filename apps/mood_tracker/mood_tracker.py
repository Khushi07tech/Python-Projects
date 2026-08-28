import time
from datetime import datetime
import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QListWidget
import random
import sqlite3

quotes = [
    "The sky isn't asking you to hurry.",
    "Quiet days still count.",
    "Small steps are still steps.",
    "Begin softly.",
    "Breathe. Then begin.",
    "There is beauty in unfinished things.",
    "Your pace is enough.",
    "Today doesn't have to be perfect.",
    "The moon never rushes to rise.",
    "Little by little is still progress.",
    "Kindness begins with yourself.",
    "One page at a time.",
    "Rest is part of the journey.",
    "You are allowed to start again.",
    "Every sunrise begins in darkness.",
    "Leave room for wonder.",
    "You don't have to bloom overnight.",
    "Tiny moments become memories.",
    "Peace grows quietly.",
    "A gentle heart is a strong heart.",
    "Not every day needs a masterpiece.",
    "Your story is still unfolding.",
    "Some seasons are meant for growing roots.",
    "The stars shine without making noise.",
    "Be where your feet are.",
    "Even the smallest candle holds light.",
    "The world can wait a moment.",
    "Today is a blank page.",
    "Hope is often quiet.",
    "Choose curiosity over pressure.",
]
one_word_labels = [
    "Just be YOU!",
    "One little word...",
    "Today's feeling...",
    "How are you, really?",
    "What's your word today?",
    "Be honest with yourself.",
    "A word, nothing more.",
]
welcome_messages = [
    "Hello",
    "Hi there,",
    "Welcome back,",
    "Good Morning,",
    "Good Afternoon,",
    "Good Evening,",
    "A fresh page for",
    "Today's yours,",
    "It's lovely seeing",
    "Ready when you are,",
    "Another little day for",
    "One gentle step,",
    "Let's begin,",
    "Take your time,",
    "Breathe in,",
    "Slow and steady,",
    "Today's chapter belongs to",
    "A quiet moment for",
    "Here's to you,",
    "Just for you,"
]
names = [
    "Khushi 🌙",
    "Maimunah ♥",
    "Love ✨",
    "Khushbakht 👑",
    "Sunshine ☀",
    "Dreamer ☁",
    "Pookie 🌸",
    "Bestie 🫶",
    "Starlight ✨",
    "Moonchild 🌙",
    "Curious Soul 🌿",
    "Sweetheart 🤍",
    "Little Coder 💻",
    "Future Engineer 🚀",
    "Creative Mind 🎨",
    "Explorer 🧭",
    "Brave Heart 💜",
    "Gentle Soul 🍃",
    "Wonder ✨",
    "Bloom 🌷",
    "Dear One 🤍",
    "Lovely 🌼",
    "Baddie💜",
    "Shining Star ⭐",
    "Spark 🌟",
    "You 🌙",
]

conn = sqlite3.connect("mood.db")
cursor = conn.cursor()

cursor.execute ("""
                    CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        word TEXT NOT NULL
                    )
               """)

class HistoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("History")
        self.setMinimumWidth(500)
        self.resize(500, 650)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.init_widgets()
        self.load_history()
        self.set_layout()
        self.apply_styles()

    def init_widgets(self):
        self.hstry_lbl = QLabel("~ History ~")
        self.hstry_list = QListWidget()

    def load_history(self):
        self.hstry_list.clear()
        cursor.execute("SELECT date, word FROM entries ORDER BY id DESC")
        rows = cursor.fetchall()

        for date, word in rows:
            formatted_time = datetime.fromtimestamp(int(date)).strftime("%Y-%m-%d %H:%M")

            item_text = f"{formatted_time}  ➔  {word}"
            self.hstry_list.addItem(item_text)

    def set_layout(self):
        vbox = QVBoxLayout()

        self.hstry_lbl.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.hstry_lbl)
        vbox.addWidget(self.hstry_list)

        self.centralWidget.setLayout(vbox)

        vbox.setSpacing(20)
        vbox.setContentsMargins(40, 40, 40, 40)

    def apply_styles(self):
        self.hstry_lbl.setObjectName("hstry_lbl")

        self.setStyleSheet("""
                    QMainWindow, QWidget{
                        background-color: #1F232B;
                    }
                    QLabel#hstry_lbl{
                        color: #B6A6FF;
                        font-family: Garamond;
                        font-size: 40px;
                        font-weight: bold;
                    }
                    QListWidget {
                        background-color: #282C34;
                        color: #F1F2F4;
                        font-family: Lato;
                        font-size: 18px;
                        border: 2px solid #B6A6FF;
                        border-radius: 12px;
                        padding: 13px;
                    }
                    QListWidget::item {
                        padding: 10px;
                        border-bottom: 1px solid #3A3F4D;
                    }
                    QListWidget::item:hover,
                    QListWidget::item:selected{
                        background-color: #5865F2;
                        color: #FFFFFF;
                        border-radius: 8px;
                    }
        """)

    def reload_history(self):
        self.load_history()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mood logger")
        self.setMinimumWidth(500)
        self.resize(500, 650)

        # Central Widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Call other functions
        self.init_widgets()
        self.set_layout()
        self.apply_styles()

    def init_widgets(self):
        self.print_word_lbl = QLabel("")

        self.wlcm_lbl = QLabel(random.choice(welcome_messages))
        self.name_lbl = QLabel(random.choice(names))

        # pulls a random quote from the aesthetics text file
        self.top_comma = QLabel("❝")
        self.quote_lbl = QLabel(random.choice(quotes))
        self.quote_lbl.setWordWrap(True)
        self.bottom_comma = QLabel("❞")

        # Allow the user to enter one word for themselves
        self.word_lbl = QLabel(random.choice(one_word_labels))
        self.word_line = QLineEdit()
        self.word_line.setPlaceholderText("Just be YOU!")

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.handle_save_button)

        self.hstry_btn = QPushButton("History")
        self.hstry_btn.clicked.connect(self.handle_history_button)

    def set_layout(self):
        vbox = QVBoxLayout()

        self.print_word_lbl.setAlignment(Qt.AlignRight)
        self.wlcm_lbl.setAlignment(Qt.AlignLeft)
        self.name_lbl.setAlignment(Qt.AlignCenter)
        self.top_comma.setAlignment(Qt.AlignCenter)
        self.quote_lbl.setAlignment(Qt.AlignCenter)
        self.bottom_comma.setAlignment(Qt.AlignCenter)
        self.word_lbl.setAlignment(Qt.AlignCenter)
        self.word_line.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.print_word_lbl)
        vbox.addWidget(self.wlcm_lbl)
        vbox.addWidget(self.name_lbl)
        vbox.addWidget(self.top_comma)
        vbox.addWidget(self.quote_lbl)
        vbox.addWidget(self.bottom_comma)
        vbox.addWidget(self.word_lbl)
        vbox.addWidget(self.word_line)
        vbox.addWidget(self.save_btn)
        vbox.addWidget(self.hstry_btn)

        self.centralWidget.setLayout(vbox)

        vbox.setSpacing(20)
        vbox.setContentsMargins(40, 40, 40, 40)


    def apply_styles(self):
        # Apply object names
        self.print_word_lbl.setObjectName("print_word_lbl")
        self.wlcm_lbl.setObjectName("wlcm_lbl")
        self.name_lbl.setObjectName("name_lbl")
        self.top_comma.setObjectName("top_comma")
        self.quote_lbl.setObjectName("quote_lbl")
        self.bottom_comma.setObjectName("bottom_comma")
        self.word_lbl.setObjectName("word_lbl")
        self.word_line.setObjectName("word_line")
        self.save_btn.setObjectName("save_btn")
        self.hstry_btn.setObjectName("hstry_btn")

        # Apply styles to the objects
        self.setStyleSheet("""
            QMainWindow, QWidget{
                background-color: #1F232B;
            }
            QLabel#print_word_lbl{
                color: #B6A6FF;
                font-family: Garamond;
                font-size: 40px;
                font-weight: bold;
            }
            QLabel#wlcm_lbl{
                color: #F1F2F4;
                font-family: Quicksand;
                font-size: 35px;
            }
            QLabel#name_lbl {
                color: #F1F2F4; 
                font-family: Quicksand;
                font-size: 48px;
                font-weight: bold;
            }
            QLabel#top_comma, QLabel#bottom_comma {
                color: #A8B0BC;
                font-weight: bold;
                font-size: 48px;
            }
            QLabel#quote_lbl{
                color: #A8B0BC;
                font-family: Garamond;
                font-size: 17px;
                padding: 0px;
                font-style: italic;
            }
            QLabel#word_lbl{
                color: #B6A6FF;
                font-family: Lato;
                font-size: 18px;
            }
            QLineEdit{
                font-size: 20px;
                color: #F1F2F4;
                font-family: Lato;
                border-radius: 17px;
                border: 2px solid #B6A6FF;
                padding: 5px;
            }
            QLineEdit:placeholder{
                color:#7A8290;
            }   
            QPushButton{
                background-color: #5865F2;
                color: #F1F2F4;
                font-weight: bold;
                font-size: 23px;
                border-radius: 17px;
                border: none;
                padding: 9px;
            }
            QPushButton:hover{
                background-color: #6A75F5;
            }
        """)

    def handle_save_button(self):
        separators = [" ", ",", "/", "-", "\\", "\t", "\n"]
        date = int(time.time())
        user_input = self.word_line.text().strip().lower()

        # Validate the input string
        if not user_input:
            self.print_word_lbl.setText("Write a word first! 🌸")
            return

        if any(sep in user_input for sep in separators):
            self.print_word_lbl.setText("One word only 🎀")
            return

        if len(user_input) > 20:
           self.print_word_lbl.setText("Too long for one word! 💫")
           return

        # Success Path (Input is 100% valid)
        cursor.execute("INSERT INTO entries (date, word) VALUES (?, ?)", (date, user_input))
        conn.commit()
        self.print_word_lbl.setText(user_input)
        self.word_line.clear()

        if hasattr(self, "history_window") and self.history_window.isVisible():
            self.history_window.reload_history()



    def handle_history_button(self):
        self.history_window = HistoryWindow()
        self.history_window.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit_code = app.exec_()
    conn.close()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
