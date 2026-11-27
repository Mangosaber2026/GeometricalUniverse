import geometry.vectors.times

data class NumberAnalysis(
    val original: List<Int>,
    val even: List<Int>,
    val squared: List<Int>,
    val sum: Int
)

fun analyzeNumbers(numbers: List<Int>): NumberAnalysis {
    val evenNumbers = numbers.filter { it % 2 == 0 }
    val evenSquared = evenNumbers.map { it * it }
    val sum = evenSquared.sum()

    return NumberAnalysis(
        original = numbers,
        even = evenNumbers,
        squared = evenSquared,
        sum = sum
    )
}

fun executeVectors() {
    val numbers = mutableListOf<Int>(1, 2, 3, 4, 5, 6)

    val result = analyzeNumbers(numbers)

    val original = result.original
    val even = result.even
    val squared = result.squared
    val sum = result.sum

    println("Here is the latest result of the calculation:")

    println("Original: $original")
    println("Even numbers: $even")
    println("Squared even numbers: $squared")
    println("Sum of squared even numbers: $sum")

    val vector2 = geometry.vectors.Vector2(
        3.0, 4.0
        )
    val anotherVector2 = geometry.vectors.Vector2(
        x = 2.0, y = 3.0
        )
    val vector3 = geometry.vectors.Vector3(
        2.0, 3.0, 6.0
        )

    println("2D Vector: $vector2")
    println("2D Magnitude: ${vector2.magnitude()}")
    println("Dot product of $vector2 and $anotherVector2: ${vector2 * anotherVector2}")
    println("$vector2 times a scalar quantity of 3: ${vector2 * 3.0}")
    println("$anotherVector2 times a scalar quantity of 4: ${4.0 * anotherVector2} ")

    println("3D Vector: $vector3")
    println("3D Magnitude: ${vector3.magnitude()}")
}

fun main() {
    
    val turtle = class_manipulation.Turtle()
    
    turtle.forward(100.0)
    turtle.rotate(90.0)
    turtle.forward(50.0)
    
    val position = turtle.getPosition()
    
    val quadraticFct1 = class_manipulation.QuadraticFct(2.0, -8.0, 2.0)
    
    println("Position of turtle at: (${position[0]}, ${position[1]})")
    
    println("Y intercepts of quadratic function is/are = ${quadraticFct1.getXIntercepts()}")
    
    println("Finished successfully! 🎉")
}