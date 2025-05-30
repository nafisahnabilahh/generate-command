import os

def generate_ffmpeg_command(video_path):
    #check if the video path is exist at the given path
    if not os.path.isfile(video_path):

        #if video is not exist, it will return None for command and below error message
        return None, f"Error: File not found at \"{video_path}\". Please check the path."
        #originally i didn't put the "". But, i add "" just to highlight and differentiate it from normal text error

    #gets the folder path so i know where the video is located
    #The purpose is to help save output images in the same folder
    folder_path = os.path.dirname(video_path)

    #Get the file name without extension (ex: "video.mp4" becomes "video")
    output_name= os.path.splitext(os.path.basename(video_path))[0]

    # set the name pattern for the output images (ex: "video0002.jpg")
    output_pattern = os.path.join(folder_path, f"{output_name}%04d.jpg")

    # Create full ffmpeg command with timestamp and fps
    ffmpeg_command = (
        f'ffmpeg -i "{video_path}" '
        f'-vf "drawtext=text=\'%{{pts\\:hms}}\':fontsize=100:fontcolor=red:x=10:y=10" '
        f'-r 30 "{output_pattern}"'
    )

    # Return the ffmpeg command and None (meaning no error)
    return ffmpeg_command, None


if __name__ == "__main__":

    video_path = [] #store all valid paths entered

    # Keep asking to enter video paths until they type 'done'
    while True:
        video_input = input("Paste the full path to your video file: ").strip()

        # when user input done, the loop will stop
        if video_input.lower() =="done":
            break

        # Generate the command or get error message
        command, error = generate_ffmpeg_command(video_input)

        if error:
            # If error exists (invalid path), print the error and ask again
            print(error)
        else:
            #if valid, save the path
            video_path.append(video_input)
            print("path added. The command will be generated after you finish inputting all the paths and type done")

    #if no valid paths
    if not video_path:
        print("Invalid paths. Please try again.")
    else:
        print("\n=========== FINAL COMMANDS (Copy & Paste) ===========\n")
        combined_command=""

        #list to store each ffmpeg command
        command_list = []
        for path in video_path:
            command, _ = generate_ffmpeg_command(path)
            command_list.append(command)

        #if only 1 command, just use it
        if len(command_list) == 1:
            combined_command=command_list[0]
        else:
            #if more than 1 , combine with '&&' , so they run after one another in terminal
            combined_command += "&&" .join(command_list)

        #show full commands
        print(combined_command)

    #ask whether want to run commands now?
    run_now= input("Do you want to run commands now? (y/n): ").strip().lower()

    if run_now == "y":
        print("Running commands now...")

        #run each command one by one so they all execute even if one fails
        for index, cmd in enumerate(command_list, 1):
            print(f" Running command {index}/{len(command_list)}")
            os.system(cmd)
        print("Finished.")

    else:
        print("Copy and paste the commands above into your terminal to run them manually")