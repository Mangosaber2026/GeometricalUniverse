package geometry.vectors

import kotlin.math.sqrt

data class Vector2(
    val x: Double,
    val y: Double
) {
    fun magnitude(): Double {
    val squaredMagnitude = x * x + y * y
    return sqrt(squaredMagnitude)
    }


    operator fun plus(other: Vector2): Vector2 {
        return Vector2(
            x = x + other.x,
            y = y + other.y
        )
    }


    operator fun minus(other: Vector2): Vector2 {
        return Vector2(
            x = x - other.x,
            y = y - other.y
        )
    }


    operator fun times(other: Vector2): Double {
        return x * other.x + y * other.y
    }


    operator fun times(scalar: Double): Vector2 {
        return Vector2(
            x = x * scalar,
            y = y * scalar
        )
    }
}


operator fun Double.times(vector2: Vector2): Vector2 {
    return Vector2(
        x = this * vector2.x,
        y = this * vector2.y
    )
}
