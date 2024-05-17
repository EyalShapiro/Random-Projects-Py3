from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
import argparse

# make a command-line argument parser & add various parameters
parser = argparse.ArgumentParser(description="Python script to add audio to video clip")
parser.add_argument("-v", "--video-file", help="Target video file")
parser.add_argument("-a", "--audio-file", help="Target audio file to embed with the video")
parser.add_argument("-s", "--start", help="Start duration of the audio file, default is 0", default=0, type=int)
parser.add_argument("-e", "--end", help="The end duration of the audio file, default is the length of the video file", type=int)
parser.add_argument("-c", "--composite", help="Whether to add to the existing audio in the video", action="store_true", default=False)
parser.add_argument("-f", "--volume-factor", type=float, default=1.0, help="The volume factor to multiply by the volume of the audio file, 1 means no change, below 1 will decrease volume, above will increase.")
# parse the arguments
args = parser.parse_args()
video_file = args.video_file
audio_file = args.audio_file
start = args.start
end = args.end
composite = args.composite
volume_factor = args.volume_factor
# print the passed parameters, just for logging
print(vars(args))