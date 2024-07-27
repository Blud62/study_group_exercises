lang = 'fr'
#print(id(lang))

# setting user language
def set_language():
    # lang = 'en' # variable shadowing
    # # print(id(lang))
    print('Please select either en, fr, es, de')
    lang = input()

    while lang not in ['en', 'fr', 'es', 'de']:
        lang = 'en'
        print('language not supported, please select another language')
        print('Please select either en, fr, es, de')
        lang = input()

    return lang

lang = set_language()

print(lang)
