
>>> from pytube import YouTube
 
 def download_youtube_video(url, save_path="."):
     try:
         yt = YouTube(url)
 
         print(f"Title: {yt.title}")
         print("Downloading the highest resolution stream...")

      
         stream = yt.streams.get_highest_resolution()
 
         
         stream.download(output_path=save_path)
 
         print(f"Download completed! Video saved to: {save_path}")
    except Exception as e:
       print(f"An error occurred: {e}")

if _name_ == "_main_":
    video_url = input("Enter the YouTube video URL: ")
