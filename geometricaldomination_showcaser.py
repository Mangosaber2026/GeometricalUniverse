import turtle_extension as tx

from GeometricalDomination import gd

turtle = tx.ChainTurtle().color("indigo")
gd.Shapes.polygon_fill(100, 10, turtle)
tx.mainloop()