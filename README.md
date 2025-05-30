# generate-command
The previous version "Generating1Cmd.py" could only handle one video link at a time. It could generate the command, but it couldn’t run the command automatically. Users had to copy the generated command and paste it into the terminal manually.

In this version "GeneratingManyCmd.py":
1. Users can enter many video links. The program will keep asking until they type done.
2. If a video path is invalid, the program will ask the user to enter a valid one. It will keep running until done is typed.
3. After entering the links, users can choose to run the commands automatically or copy and run them manually.
4. The program works even if the videos are saved in different folders.
