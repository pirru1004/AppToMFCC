# AppToMFCC

A Python GUI application to extract Mel-Frequency Cepstral Coefficients (MFCC) from audio files.

## Features

- **Graphical User Interface**: Easy-to-use interface with drag-and-drop support
- **File Selection**: Browse and select audio files via file dialog
- **Drag and Drop**: Drop audio files directly onto the application
- **MFCC Extraction**: Extract configurable MFCC features from audio files
- **Real-time Output**: View MFCC results immediately in the application

## Installation

1. Clone or download this repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python app.py
```

### How to Use

1. **Select File**: Click the "Select File" button to browse and choose an audio file.
2. **Drag and Drop**: Drag an audio file from your file manager and drop it onto the designated drop area.
3. **View Results**: The MFCC information will be displayed in the text area below, including:
   - File path
   - Sampling rate
   - MFCC shape
   - First few MFCC coefficients

## Supported Formats

- WAV
- MP3
- FLAC
- OGG
- And other formats supported by librosa

## Dependencies

- librosa: For audio processing and MFCC extraction
- numpy: For numerical operations
- matplotlib: Included for potential future features
- PyQt5: For the graphical user interface

## Troubleshooting

- Ensure your audio file is in a supported format
- If you encounter import errors, make sure all dependencies are installed
- For large audio files, processing may take some time
- Make sure you have a display environment for the GUI (works in desktop environments)