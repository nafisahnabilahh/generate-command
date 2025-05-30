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
    # uses that folder path to tell ffmpeg exactly where to save the output images
    output_pattern = os.path.join(folder_path, "frame_%04d.jpg")

    # Output images named according to the pattern above
    ffmpeg_command = (
        f'ffmpeg -i "{video_path}" '
        f'-vf "drawtext=text=\'%{{pts\\:hms}}\':fontsize=100:fontcolor=red:x=10:y=10" '
        f'-r 30 "{output_pattern}"'
    )

    # Return the ffmpeg command and None for error since file is valid
    return ffmpeg_command, None


if __name__ == "__main__":
    # Loop until we inputs a valid file path
    while True:
        # Ask  to paste full path to our video file
        video_input = input("Paste the full path to your video file: ").strip()
        # Generate the command or get error message
        command, error = generate_ffmpeg_command(video_input)

        if error:
            # If error exists (invalid path), print the error and ask again
            print(error)
        else:
            # If no error, print the ffmpeg command and exit the loop
            print("\n Here’s your ffmpeg command:\n")
            print(command)
            break