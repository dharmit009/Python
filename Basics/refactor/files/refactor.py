# USE OF CONTEXT MANAGERS 
# THIS CLOSES THE OPENED FILES AUTOMATICALLY. 
# THIS WORKS WITH THREADS, CONNECTIONS WITH DATABASES AND MUCH MORE. 

with open('test.txt', 'r') as f:
    file_contents = f.read()


words = file_contents.split(' ')
word_count = len(words)
print(word_count)
