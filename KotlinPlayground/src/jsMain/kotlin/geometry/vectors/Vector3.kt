package geometry.vectors

import kotlin.math.sqrt

data class Vector3(
    val x: Double,
    val y: Double,
    val z: Double
) {
    fun magnitude(): Double {
        return sqrt(x * x + y * y + z * z)
    }
}