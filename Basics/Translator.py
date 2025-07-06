def fn_Translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in ("AEIOUaeiou"):
            translation = translation + "H"
        else:
            translation = translation + letter
    return translation

print(fn_Translate(input("Enter a phras")))
'''
Multiple line comments

'''