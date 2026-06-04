#counts how many times the pattern appeared in the text

count = 0
text = input("Enter the text: ")
pattern = input("Enter the pattern: ")
for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)] == pattern:
        count += 1 
            
print (count)