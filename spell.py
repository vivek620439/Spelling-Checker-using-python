from spellchecker import SpellChecker
corrector=SpellChecker()

word=input("Enter a Word:")
if word in corrector:
    print("correct")
else:
    correct_word=corrector.correction(word)
    print("Correct Spell is :",correct_word)    