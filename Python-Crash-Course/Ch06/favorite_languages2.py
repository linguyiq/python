# A List in a Dictionary
favorite_languages = {
    'jen' : ['python', 'perl'],
    'john' : ['perl'],
    'sarah' : ['c', 'go'],
    'mike' : ['python', 'c++'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is ")
    else:
        print("\n" + name.title() + "'s favorite languages are ")
        for language in languages:
            print("\t" + language.title())