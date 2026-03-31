#!/usr/bin/env python3
"""
MFCC Extractor App

This script provides a GUI to extract Mel-Frequency Cepstral Coefficients (MFCC) from an audio file.
"""

import sys
import librosa
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QFrame, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QDragEnterEvent, QDropEvent

class MFCCExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MFCC Extractor')
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        # Instructions
        self.label = QLabel('Drag and drop an audio file here or click "Select File"')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Drop area
        self.drop_area = DropArea()
        self.drop_area.fileDropped.connect(self.process_file)
        layout.addWidget(self.drop_area)

        # Button
        self.select_button = QPushButton('Select File')
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        # Output text
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.wav *.mp3 *.flac *.ogg);;All Files (*)", options=options)
        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        try:
            mfcc, sr = extract_mfcc(file_path)
            output = f"Audio file: {file_path}\n"
            output += f"Sampling rate: {sr} Hz\n"
            output += f"MFCC shape: {mfcc.shape}\n"
            output += "MFCC coefficients (first few frames):\n"
            output += str(mfcc[:, :5])  # First 5 frames
            self.output_text.setText(output)
        except Exception as e:
            self.output_text.setText(f"Error: {str(e)}")

class DropArea(QFrame):
    fileDropped = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setFrameStyle(QFrame.Box)
        self.setAcceptDrops(True)
        self.setMinimumHeight(100)
        self.label = QLabel('Drop audio file here')
        self.label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.fileDropped.emit(file_path)

def extract_mfcc(audio_path, n_mfcc=13, sr=None):
    """
    Extract MFCC features from an audio file.

    Parameters:
    - audio_path: Path to the audio file
    - n_mfcc: Number of MFCC coefficients to extract (default: 13)
    - sr: Sampling rate (default: None, uses file's native rate)

    Returns:
    - mfcc: MFCC features as a numpy array
    - sr: Sampling rate used
    """
    # Load audio file
    y, sr = librosa.load(audio_path, sr=sr)

    # Extract MFCC
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)

    return mfcc, sr

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MFCCExtractor()
    window.show()
    sys.exit(app.exec_())