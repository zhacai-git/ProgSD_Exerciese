song_name = input("Please input the first line of your favourite song: ")

print("The length is: " + str(len(song_name)))

splice_index = input("Please input a starting number and an ending number: ")

numbers = splice_index.split(" ")

start = int(numbers[0])
end = int(numbers[1])

print("Split section: " + song_name[start:end])