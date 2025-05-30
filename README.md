## Overview
This tool was created to make slicing videos using FFmpeg easier, especially when dealing with a large number of files.

### Why I created this
I needed to slice **hundreds of videos** to compare **end-to-end latency** of messages between different apps. For each video, I had to:

1. Copy the slicing command from my notes.
2. Manually replace the old video path with the new one.
3. Copy the updated command.
4. Paste it into the terminal to run.

This process was:
- **Slow** and repetitive.
- **Frustrating**, because I often made **typing mistakes** like accidentally deleting a character or pasting in the wrong spot.
- **Error-prone**, especially when I was tired or working quickly.

Even a small mistake could break the command, forcing me to check everything again.

### The solution
So, I created this Python program to make my work faster and safer:
- I can now **enter multiple video file paths** directly.
- The program **automatically generates the correct FFmpeg slicing command** for each video.
- It works even if the videos are in **different folders**.
- I can choose to **run the commands immediately** or just **copy them easily** without worrying about formatting errors.

### Purpose slicing video?
Slicing lets me cut out just the important parts of a video (e.g. the moment a message appears) to measure delays across different apps. It’s a key step when testing and comparing **latency** during performance analysis.


