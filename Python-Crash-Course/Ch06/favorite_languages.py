favorite_languages = {
    'jen' : 'python',
    'john' : 'perl',
    'sarah' : 'c',
    'mike' : 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())