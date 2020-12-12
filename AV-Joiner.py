import argparse
import os


def Joiner(audio, video, output_format):
    os.system("mkdir DUMP")
    os.system("ffmpeg -i {} 2>&1 | grep Duration | sed 's/Duration: \(.*\), start/\\1/g' > DUMP/duration.txt".format(video))
    f = open('DUMP/duration.txt', 'r')
    f = f.read().split()[0][:-1]
    print("[*]MERGING CONTENTS ....")
    os.system("ffmpeg -i {} -i {} DUMP/Myjoin.{} -y 2>DUMP/error.txt ".format(audio, video, output_format))
    os.system("ffmpeg -ss 00:00:00.0 -i DUMP/Myjoin.mp4 -c copy -t {} MyVideo.{} -y 2> DUMP/error.txt  ".format(f,output_format))
    os.system('rm -rf DUMP')
    print("\n[!]Merged Audio and Video Successfully ! .. Stored in file : MyVideo.{}".format(output_format))




def main():
    parser = argparse.ArgumentParser(description=" Bind/Join Audio and video together.")
    parser.add_argument('-v', '--video', metavar='', required=True, help='Video to join')
    parser.add_argument('-a', '--audio', metavar='', required=True, help='Audio to Join ')
    parser.add_argument('-f', '--output_format', metavar='', required=True, help='Final video Format to export in')
    args = parser.parse_args()

    Joiner(args.audio, args.video, args.output_format)


if __name__ == '__main__':
    main()
