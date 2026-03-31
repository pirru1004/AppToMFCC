# AppToMFCC

A web-based application to extract Mel-Frequency Cepstral Coefficients (MFCC) from audio files directly in your browser.

## 🌐 Live Demo

Visit the live application at: [https://pirru1004.github.io/AppToMFCC/](https://pirru1004.github.io/AppToMFCC/)

## ✨ Features

- **Browser-based**: No installation required - runs entirely in your web browser
- **Drag and Drop**: Drop audio files directly onto the interface
- **File Selection**: Browse and select audio files via file dialog
- **Real-time Processing**: Extract MFCC features instantly
- **Audio Information**: Display file details, duration, sample rate, and channel info
- **MFCC Visualization**: View the extracted MFCC coefficients

## 🎯 How to Use

1. Open the application in your web browser
2. Drag and drop an audio file onto the upload area, or click "Select Audio File"
3. Wait for processing (may take a few seconds for longer files)
4. View the extracted MFCC coefficients and audio information

## 🔧 Supported Audio Formats

- WAV
- MP3
- OGG
- AAC
- And other formats supported by the Web Audio API

## 🛠️ Technical Details

- Built with vanilla JavaScript
- Uses the Web Audio API for audio processing
- Leverages the Meyda.js library for MFCC extraction
- Responsive design that works on desktop and mobile

## 📁 Project Structure

- `index.html` - Main web application
- `README.md` - This documentation
- `app.py` - Legacy Python desktop version (for reference)
- `requirements.txt` - Python dependencies (for desktop version)

## 🐛 Browser Compatibility

- Chrome 14+
- Firefox 25+
- Safari 6+
- Edge 12+

## 📖 Development

### Running Locally

Simply open `index.html` in your web browser. No server required!

### Legacy Desktop Version

If you prefer the desktop Python version:

1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python app.py`

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve the application!

## 📄 License

This project is open source. Feel free to use and modify as needed.