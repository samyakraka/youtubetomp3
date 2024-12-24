# YouTube to MP3 Converter

This project is a **YouTube to MP3 Converter** built using Python and Streamlit. It allows users to convert YouTube videos to MP3 audio files and download them easily. 

## Features

- **Download Audio from YouTube**: Users can enter a YouTube video URL and download the audio as an MP3 file.
- **Streamlit Web Interface**: Provides an intuitive and user-friendly interface for the conversion process.
- **Automatic Conversion to MP3**: Converts downloaded audio files to MP3 format for compatibility.
- **Download Link**: After conversion, users can download the MP3 file directly from the web interface.
- **Responsive Design**: Works on desktop, tablet, and mobile devices without the need for additional apps.

## How to Use

1. **Enter the YouTube URL**: Copy the URL of the YouTube video you want to convert and paste it into the provided input box.
2. **Click "Convert to MP3"**: This will download the audio from the provided YouTube link and convert it into MP3 format.
3. **Download the MP3 File**: After the conversion process, a download button will appear. Click it to download the converted MP3 file.

## Prerequisites

- **Python 3.7+**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the repository** (or download the source code):
    ```bash
    git clone https://github.com/samyakraka2908/youtubetomp3
    cd youtube-to-mp3
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Streamlit application, use the following command:
```bash
streamlit run app.py
