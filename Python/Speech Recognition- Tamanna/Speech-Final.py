from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QComboBox,
    QTextEdit, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
)
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import tempfile
import sys

class SpeechApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎤 Speech Recognition")
        self.setGeometry(100, 100, 900, 600)

        self.language_codes = {"English": "en", "Hindi": "hi", "Punjabi": "pa"}
        self.is_dark_mode = False
        self.player = QMediaPlayer()

        self.initUI()
        self.apply_light_theme()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Fonts
        font_title = QFont("Segoe UI Semibold", 20)
        font_label = QFont("Segoe UI", 13)
        font_btn = QFont("Segoe UI Semibold", 11)
        font_trans = QFont("Segoe UI", 12)

        # # Sidebar layout
        # sidebar = QVBoxLayout()
        # sidebar.setSpacing(15)

        # Main layout
        main_layout = QVBoxLayout()

        # Title
        self.label = QLabel("🧠 Speech Recognition & Translation")
        self.label.setFont(font_title)
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        # Language Selection
        lang_layout = QHBoxLayout()
        self.lang_label = QLabel("Language:")
        self.lang_label.setFont(font_label)
        self.lang_combo = QComboBox()
        self.lang_combo.setFont(font_label)
        self.lang_combo.addItems(self.language_codes.keys())
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)
        main_layout.addLayout(lang_layout)

        # Text Area (reduced height)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont("Segoe UI Variable", 12))
        self.text_box.setFixedHeight(140)
        main_layout.addWidget(self.text_box)

        # Translated Output (moved above buttons)
        self.translated_label = QLabel("Translation will appear here.")
        self.translated_label.setWordWrap(True)
        self.translated_label.setFont(font_trans)
        self.translated_label.setAlignment(Qt.AlignTop)
        main_layout.addWidget(self.translated_label)

        # Buttons
        button_layout = QHBoxLayout()
        self.recognize_btn = QPushButton("🎧 Recognize")
        self.translate_btn = QPushButton("🌐 Translate")
        self.speech_btn = QPushButton("🔊 Speak")
        self.toggle_theme_btn = QPushButton("🌓 Theme")

        for btn in [self.recognize_btn, self.translate_btn, self.speech_btn, self.toggle_theme_btn]:
            btn.setFont(font_btn)
            btn.setFixedHeight(40)
            button_layout.addWidget(btn)

        self.recognize_btn.clicked.connect(self.recognize_speech)
        self.translate_btn.clicked.connect(self.translate_text)
        self.speech_btn.clicked.connect(self.text_to_speech)
        self.toggle_theme_btn.clicked.connect(self.toggle_theme)

        main_layout.addLayout(button_layout)

        # Final layout combo
        layout = QHBoxLayout()
        # sidebar_widget = QWidget()
        # sidebar_widget.setLayout(sidebar)
        # sidebar_widget.setFixedWidth(140)

        content_widget = QWidget()
        content_widget.setLayout(main_layout)

        # layout.addWidget(sidebar_widget)
        layout.addWidget(content_widget)

        central_widget.setLayout(layout)

    def apply_light_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #fefefe;
            }
            QLabel {
                color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QTextEdit {
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 6px;
                font-family: 'Segoe UI Variable';
                font-size: 13px;
            }
            QComboBox {
                padding: 4px;
                font-size: 13px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QLabel {
                color: #f1f1f1;
            }
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QTextEdit {
                background-color: #2b2b2b;
                color: #f1f1f1;
                border: 1px solid #555;
                border-radius: 6px;
                padding: 6px;
                font-family: 'Segoe UI Variable';
                font-size: 13px;
            }
            QComboBox {
                background-color: #2b2b2b;
                color: #f1f1f1;
                border-radius: 6px;
                border: 1px solid #555;
                padding: 4px;
            }
        """)

    def toggle_theme(self):
        if self.is_dark_mode:
            self.apply_light_theme()
            self.is_dark_mode = False
        else:
            self.apply_dark_theme()
            self.is_dark_mode = True

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.label.setText("🎙️ Listening...")
            try:
                audio = recognizer.listen(source)
                selected_lang = self.lang_combo.currentText()
                lang_code = self.language_codes[selected_lang]
                text = recognizer.recognize_google(audio, language=lang_code)
                self.text_box.setText(text)
                self.label.setText("✅ Speech recognized.")
            except sr.UnknownValueError:
                QMessageBox.critical(self, "Error", "Could not understand the audio.")
            except sr.RequestError:
                QMessageBox.critical(self, "Error", "Could not request results; check internet connection.")

    def translate_text(self):
        translator = Translator()
        input_text = self.text_box.toPlainText()
        if input_text:
            translated = translator.translate(input_text, dest='en')
            self.translated_label.setText(f"Translation: {translated.text}")
        else:
            QMessageBox.warning(self, "Warning", "Please enter or recognize text first.")

    def text_to_speech(self):
        text = self.text_box.toPlainText()
        if text:
            selected_lang = self.lang_combo.currentText()
            lang_code = self.language_codes[selected_lang]
            tts = gTTS(text=text, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fp.name)))
                self.player.play()
        else:
            QMessageBox.warning(self, "Warning", "Please enter or recognize text first.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpeechApp()
    window.show()
    sys.exit(app.exec_())
