def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    if lang == 'fr' :
        return 'Bonjour'
    else :
        return 'Hello'
    
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')

def thing() :
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()