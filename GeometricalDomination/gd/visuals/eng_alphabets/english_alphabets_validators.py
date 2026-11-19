#? ⚓ Anchor for this module: [[english-alphabets-validators-anchor|english_alphabets_validators.py]] 
# [Click here to see module description](./eng_alphabets_docs/english_alphabets_validators.md) 

lazy import functools as ft
lazy import numbers as num

lazy import turtle_extension as tx
lazy import uf


#? ⚓ alphabets_validate anchor: [[alphabets-validate-anchor|alphabets_validate()]] 
#* 📝 [Click here to see function description](./eng_alphabets_docs/english_alphabets_validators.md) 
def alphabets_validate(height, tls):

    uf.ComboValidate(height, name="height")(uf.real_validate(), uf.Positive())

    uf.TypeValidate(tx.ChainTurtle)(tls, name="tls")

    return height, tls


#? ⚓ alphabets_deco anchor: [[alphabets-deco-anchor|alphabets_deco()]] 
#* 📝 [Click here to see function description](./eng_alphabets_docs/english_alphabets_validators.md)  
def alphabets_deco(func):

    @ft.wraps(func)
    def wrapper(height: num.Real, tls: tx.ChainTurtle):

        alphabets_validate(height, tls)
        
        return func(height, tls)
    
    return wrapper