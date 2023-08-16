# feynmen = {
#     'genreators,':'genarators are an objects that behave as an iterable',
#     "list comprehension,": " its a different way to write lists and for loops it got another name which is one line for loop ",
# }

# #for k,v in feynmen.items():
#     #print(k,v)

# print(feynmen)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

new_names = ["edward","phil"]

for names,lan in favorite_languages.items(): 
    if names in new_names:
        print(f"Hello {names.title()}")
    else:
        print(f"please {names.title()} take the poll")
        