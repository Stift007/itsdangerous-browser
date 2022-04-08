```py
import requests
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Itsda:

    def __init__(self) -> None:

        self.window = QWidget()
        self.window.setWindowTitle("ItsDangerous Webbrowser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.browser = QWebEngineView()
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.clicked.connect(self.browser.back)
        
        self.fwd_btn = QPushButton(">")
        self.fwd_btn.setMinimumHeight(30)
        self.fwd_btn.clicked.connect(self.browser.forward)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.fwd_btn)


        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self,url):
        if not url.startswith("http://"):
            url = "http://"+ url
            self.url_bar.setText(url)
        if url.startswith("http://"):
            self.url_bar.setText(url)
        safe = requests.get("https://itsdangerous.stift007.repl.co/api",json={"url":url.replace("https://","").replace("http://","")}).text
        print(safe)
        if "false" in safe.lower():
            self.browser.setUrl(QUrl(url))
        else:
            self.browser.setUrl(QUrl(f'https://itsdangerous.stift007.repl.co/linkfilter?url={url.replace("https://","").replace("http://","")}'))



app = QApplication(sys.argv)
window = Itsda()
sys.exit(app.exec_())
```
