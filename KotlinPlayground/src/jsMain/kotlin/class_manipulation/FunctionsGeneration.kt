package class_manipulation


import kotlin.math.sqrt

abstract class FunctionsGenerator {
    abstract fun evaluate(x: Double): Double
    
    fun generateValues(
        start: Double,
        end: Double,
        samples: Int
    ): List<Pair<Double, Double>> {
        
        require(samples >= 2)
        
        val interval = (end - start) / (samples - 1)

        return (0 until samples).map { index ->
            val x = start + index * interval
            x to evaluate(x)
        }
    }
}

interface FunctionGenerator {
    fun evaluate(x: Double): Double
    
    fun generateValues(
        start: Double,
        end: Double,
        samples: Int
    ): List<Pair<Double, Double>> {
        
        require(samples >= 2)
        
        val interval = (end - start) / (samples - 1)

        return (0 until samples).map { index ->
            val x = start + index * interval
            x to evaluate(x)
        }
    }
}

sealed class QuadraticFctResults {
    data class TwoRealRoots(val values: List<Double>) : QuadraticFctResults()
    data class OneRealRoot(val value: Double) : QuadraticFctResults()
    data object NoRealRoots : QuadraticFctResults()
}

class LinearFct(
    val gradient: Double,
    val yIntercept: Double
): FunctionGenerator {
    
    override fun evaluate(x: Double): Double {
        return gradient * x + yIntercept
    }
}


class QuadraticFct(
    val varA: Double,
    val varB: Double,
    val varC: Double
): FunctionGenerator {

    override fun evaluate(x: Double): Double {
        return varA*x*x + varB*x + varC
    }

    fun getXIntercepts() : QuadraticFctResults {
        if (varA == 0.0) {
            return QuadraticFctResults.NoRealRoots
        }
        
        var discriminant = varB*varB - 4 * varA * varC
            
        if (discriminant > 0) { 
            val result1 = (-varB + sqrt(varB*varB - 4 * varA * varC)) / (2 * varA)
            val result2 = (-varB - sqrt(varB*varB - 4 * varA * varC)) / (2 * varA)
            val results = listOf(result1, result2)
                
            return QuadraticFctResults.TwoRealRoots(results)
        }

        if (discriminant == 0.0) {
            val result = -varB / (2 * varA)

            return QuadraticFctResults.OneRealRoot(result)
        }

        if (discriminant < 0) {
            return QuadraticFctResults.NoRealRoots
        }
        
        return QuadraticFctResults.NoRealRoots
    }
}