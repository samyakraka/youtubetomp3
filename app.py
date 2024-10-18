import os
import yt_dlp
from moviepy.editor import AudioFileClip
import streamlit as st

def download_youtube_audio(video_url, output_audio_path="audio.webm"):
    """Download the audio from a YouTube video."""
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_audio_path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Downloaded audio as: {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"An error occurred during download: {e}")
        return None

def convert_to_mp3(audio_path, output_mp3_path="audio.mp3"):
    """Convert the downloaded audio to MP3 format."""
    try:
        audio_clip = AudioFileClip(audio_path)
        audio_clip.write_audiofile(output_mp3_path, codec='mp3')
        audio_clip.close()  # Close the file to release resources
        return output_mp3_path
    except Exception as e:
        print(f"Error converting audio: {e}")
        return None

# Streamlit UI
st.markdown(
    """
    <h1 style='text-align: center;'> 
        <span style='color: red;'>YouTube</span> to MP3 Converter
    </h1>
    """, 
    unsafe_allow_html=True
)

# Input for the YouTube link
video_url = st.text_input("Enter YouTube Video URL:")

# Button to trigger download and conversion
start_button = st.button("Convert to MP3")

if start_button and video_url:
    st.write("Downloading audio...")
    audio_path = download_youtube_audio(video_url)
    if audio_path:
        st.write("Converting audio to MP3...")
        mp3_path = convert_to_mp3(audio_path)
        if mp3_path and os.path.exists(mp3_path):
            st.write("Conversion successful! Download your MP3 below:")
            # Provide a download link for the MP3 file
            with open(mp3_path, "rb") as audio_file:
                st.download_button(
                    label="Download MP3",
                    data=audio_file,
                    file_name="audio.mp3",
                    mime="audio/mp3"
                )
            
            # Clean up the MP3 file after download
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
                
        # Clean up the original audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)

st.write(
    """
    **Our YouTube to MP3 Converter allows you to convert your favorite YouTube videos to MP3 (audio) or MP4 (video) files and download them for FREE.** Y2Mate works on your desktop, tablet, and mobile device without the installation of any additional apps. The usage of Y2Mate is free and safe!
    """
)

st.write(
    """
    **How to download YouTube videos?**
    1. Go to [YouTube.com](https://www.youtube.com) and search for a video you would like to download. Then copy the video URL from the browser address bar (youtube.com/watch?v=id).
    2. Paste the video URL in our YouTube Converter below, and choose your preferred download format. You can choose between MP3 or MP4. If you do not choose any format, the video will be converted by default to MP3. Click on the "Convert" button.
    3. The conversion of the video will start, and it may take some time. Please note that it is only possible to download YouTube videos with a maximum length of 90 minutes. As soon as the conversion is completed, you will be able to download the converted video.

    By using Y2Mate, you accept our [Terms of Use](#). Thank you for using our YouTube to MP3 Converter.
    """, 
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <hr>
    <footer style='text-align: center;'>
        &copy; 2024 EzMP3. All rights reserved.<br>
        <a href='#' target='_blank'>Contact</a> |
        <a href='#' target='_blank'>Copyright</a> |
        <a href='#' target='_blank'>Terms</a> |
        <a href='#' target='_blank'>Privacy</a>
    </footer>
    """, 
    unsafe_allow_html=True
)
