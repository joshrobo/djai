#Takes a path to an .mp3 file as an argument and prints the file's ID3 tag
import sys
import eyed3


audiofile = eyed3.load(sys.argv[1])
print audiofile.tag.artist
print audiofile.tag.title
print audiofile.tag.album
