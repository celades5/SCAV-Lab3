import os


def ex1():

    # Cut a minut of video
    os.system("ffmpeg -i messi_goat.mp4 -ss 00:16:57 -t \
            00:01:00 -c copy messi1.mp4")

    # Extract the audio and store it into mono type
    os.system("ffmpeg -i messi1.mp4 -ac 1 -vn messi1_mono.mp3")

    # Get the new audio with a lower bit rate
    os.system("ffmpeg -i messi1.mp4 -b:a 16k -vn messi1_br16k.mp3")

    # Create the subtitles
    os.system("ffmpeg -i subtitles.srt subs.ass")  # messi1.mp4

    # Addinng subtitles
    os.system('ffmpeg -i messi1.mp4 -vf "ass=subs.ass" messi1_sub.mp4')
    # os.system("ffmpeg -i messi1.mp4 -i infile.srt -c:v copy \
# -c:a copy -c:s messi1_sub.mp4")

    # Add the video, audio tunes and subtitles altogether in one container
    os.system('ffmpeg -i messi1.mp4 -i messi1_mono.mp3 -i messi1_br16k.mp3 \
            -map 0:0 -map 0:1 -map 1:0 -map 2:0 -vf \
            "ass=subs.ass" messi1_container.mp4')


if __name__ == "__main__":
    ex1()
