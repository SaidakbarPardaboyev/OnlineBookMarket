from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout

class LongStringApp(QWidget):
    def __init__(self, long_string):
        super().__init__()

        layout = QVBoxLayout()

        text_edit = QTextEdit()
        text_edit.setPlainText(long_string)
        text_edit.setReadOnly(True)  # To make it read-only
        layout.addWidget(text_edit)

        self.setLayout(layout)
        self.setWindowTitle("Long String Example")

if __name__ == "__main__":
    app = QApplication([])

    # Example long string
    long_string = "This is a very long string that you want to display in a flexible way."

    window = LongStringApp(long_string)
    window.show()

    app.exec_()
