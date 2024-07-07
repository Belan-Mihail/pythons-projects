with open('21-python-projects/story.txt', 'r') as f:
   story = f.read() 

words = set()
start_of_world = -1
target_start = '<'
target_end = '>'


'''
So, the enumerate() function in Python takes a set of data as a parameter and returns an enumerate object.
This object is returned in the format of key-value pairs, where the keys are the corresponding indexes of the elements, 
and the values ​​are the elements themselves from the passed data set.
'''
for i, char in enumerate(story):
   if char == target_start:
      start_of_world = i
   
   if char == target_end and start_of_world != -1:
    #   slice (start index = start_of_world, end index = i + 1)
      word = story[start_of_world: i + 1]
      words.add(word)
      start_of_world = -1

answers = {}

for word in words:
   answer = input('Enter a word for ' + word + ': ' )
   answers[word] = answer