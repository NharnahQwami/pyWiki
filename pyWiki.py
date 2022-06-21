#remember to pip install wikipedia before use

import wikipedia

search_query = input("Enter your wiki search query ")

results = wikipedia.summary(f"{search_query}")
#result = wikipedia.summary("search query")

print(results)


#still under work... so if its not working, try fixing the code. :)
