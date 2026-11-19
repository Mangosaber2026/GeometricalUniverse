import turtle_extension as tx

from GeometricalDomination import gd

turtle = tx.ChainTurtle().color("blue")
gd.Shapes.hexaflower_tri(200, turtle)
tx.mainloop()