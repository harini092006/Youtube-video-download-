Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from pytube import YouTube
... 
... def download_youtube_video(url, save_path="."):
...     try:
...         # Create YouTube object
...         yt = YouTube(url)
... 
...         print(f"Title: {yt.title}")
...         print("Downloading the highest resolution stream...")
... 
...         # Get the highest resolution stream
...         stream = yt.streams.get_highest_resolution()
... 
...         # Download the video
...         stream.download(output_path=save_path)
... 
...         print(f"Download completed! Video saved to: {save_path}")
...     except Exception as e:
...         print(f"An error occurred: {e}")
... 
... if _name_ == "_main_":
...     video_url = input("Enter the YouTube video URL: ")
