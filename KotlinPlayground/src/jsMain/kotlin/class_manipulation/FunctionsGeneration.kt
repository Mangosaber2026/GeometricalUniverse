package class_manipulation

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
}