#remember to pip install wikipedia b4 use

import wikipedia

x = input("Enter your wiki search query ")
result = wikipedia.summary(f"{x}")
#result = wikipedia.summary("search query")

print(result)


#still uder work... so if its not working, fix the code. :)
