package class_manipulation

import kotlin.math.sin
import kotlin.math.cos
import kotlin.math.PI


private fun Double.toRadians() : Double = 
    this * PI / 180

interface Manipulations {
    fun forward(distance: Double)
    fun move(distance: Double)
    fun rotate(angle: Double)
}

interface Drawable {
    fun draw()
}

data class TurtleState(
    var xCoor: Double = 0.0,
    var yCoor: Double = 0.0,
    var heading: Double = 0.0,
    var color: String = "black"
)

class StandardManipulations(
    private val state: TurtleState
) : Manipulations {

    override fun forward(distance: Double) {
        val radians = state.heading.toRadians()
        
        state.xCoor += cos(radians) * distance
        state.yCoor += sin(radians) * distance
    }    

    override fun move(distance: Double) {
        println("Moving $distance units.")
    }

    override fun rotate(angle: Double) {
        state.heading += (state.heading + angle) % 360
    }
}

class Turtle(
    private val state: TurtleState = TurtleState()
    ) : Manipulations by StandardManipulations(state) {
        
        fun getPosition(): List<Double> {
            return listOf(state.xCoor, state.yCoor)
        }
    }