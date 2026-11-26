"""
This module contains the class `EngPunctuation` which contains functions to draw 
numerous punctuations of the English language.
"""
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import numbers as num

import turtle_extension as tx

#* 📝 The type of Real numbers
type RealType = num.Real | float | int

class EngPunctuation:

    @staticmethod
    def space(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Traces an invisible space with a ChainTurtle.

        :param height: to calculate the amount of space

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def dot(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws a dot with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def exclamation(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws an exclamation mark with given height and turtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def question(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws a question mark with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def apostrophe(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws an apostrophe with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def colon(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws a colon with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """


    @staticmethod
    def comma(height: RealType, tls: tx.ChainTurtle) -> None:
        """
        Draws a comma with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """