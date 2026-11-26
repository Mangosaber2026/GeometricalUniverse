#? ⚓ Anchor for this module: [[english-alphabets-anchor|english_alphabets.py]] 
#* [Click here to see module description](./eng_alphabets_docs/english_alphabets.md) 

lazy import uf

lazy from . import english_letters, english_punctuations, english_shapes


#? ⚓ Alphabets anchor: [[EngAlphabets-anchor|class EngAlphabets]] 
#* 📝 [Click here to see class description](./eng_alphabets_docs/english_alphabets.md) 
class EngAlphabets(
    english_letters.EngLetters,
    english_punctuations.EngPunctuation,
    english_shapes.EngShapes
    ):


    #? ⚓ list_alphabets anchor: [[Alphabets-list-alphabets-anchor|list_alphabets()]] 
    #* 📝 [Click here to see function description](./eng_alphabets_docs/english_alphabets.md) 
    @staticmethod
    def list_alphabets():
        return uf.classes_to_dict(
            EngAlphabets,
            english_letters.EngLetters,
            english_punctuations.EngPunctuation,
            english_shapes.EngShapes
            )


def punctuation():
    return english_punctuations.EngPunctuation

def engshapes():
    return english_shapes.EngShapes


#? ⚓ eng_alphabets_dict anchor: [[eng-alphabets-dict-anchor|eng_alphabets_dict()]] 
#* 📝 [Click here to see function description](./eng_alphabets_docs/english_alphabets.md) 
def eng_alphabets_dict():
    return {
    **uf.classes_to_dict(english_letters.EngLetters),
    " ": punctuation().space,
    ".": punctuation().dot,
    "!": punctuation().exclamation,
    "?": punctuation().question,
    "'": punctuation().apostrophe,
    ":": punctuation().colon,
    ",": punctuation().comma,
    "+": engshapes().plus,
    "=": engshapes().equals,
    "*": engshapes().times,
    "-": engshapes().minus,
    "_": engshapes().underline,
    "<": engshapes().heart,
    "#": engshapes().star,
    }