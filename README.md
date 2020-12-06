# SCAV-Lab3
Lab 3 for SCAV subject at UPF

Tis readme intents to explain the third lab session in the SCAV subject for the video part.

This repository consists in:

**Pdf:** Pdf file containing screenshots of exercises with results. Plus a link in the header to the *git repository*.

**Python exercises:** Containing the code for all the different exercises needed to compute this lab. Run *ex4* containing the menu of all the lab for a full experience. Run each exercise independently if desired.

-   **NOTE:** The subtitles used are for the video *Big Buck Bunny* but I have used a different video as we can see in the lines below, therefore the subtitles do not match with the video, please take that into account.

**ex1:** For the first exercise, we have to cut 1 minute of a video. The video I decided to use is the following: *Real Madrid vs FC Barcelona 2 - 3 All Goals and Full Highlights*. Therefore:

-   **First:** Using basic ffmpeg commands learned through the course we cut 1 minut of the video, precisely, from **16:57** to **17:57**.

-   **Second:** Using basic ffmpeg commands, we extract the audio from the video and store it into an *.mp3* file with a mono track audio. 

-   **Third:** We downsample the video into a lower bitrate, if we listen to it, we will notice the lower quality in comparisson to the first one.

-   **Fourth** We put the subtitles, audio tunes and video altogether into one container.

**ex2:** In this exercise, we ask for a number of files and it's name, and then stores it into a container file with *.mp4* format extension


**ex3:** In this exercise, we pass a file in *.mp4* format and it returns us which broadcasting standars would fit. We first insert the name, then get the name and the output looks for the important information (i.e.) *.h264, mpeg2, aac, ac3* etc... and then with that information, we compare it with a list which contains all the types of broadcasting (i.e) *DVB, ISBD, ATSC, DTMB* etc... and returns with whic type the file is compatible or if there is none it returns *ERROR*.


**ex4:** This exercise asks to create some containers. In order to do that we just do a little menu that lets you launch the previouse exercises.


**ex5:** This exercise it is just a simple menu that allows you to run an exercise desired.
