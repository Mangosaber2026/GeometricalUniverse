package class_manipulation

class Computer (
    val brand: String,
    var ram: Int
) {
    val id = generateID()
    
    init {
        println("Computer initialized.")
    }
    
    constructor(brand: String) : this(brand, 8) {
        println("Default RAM assigned.")
    }
    
    fun specifications() {
        println("Computer from brand $brand with ${ram}GB RAM.")
    }
    
    companion object {
        private var nextID = 1

        fun generateID(): Int {
            return nextID++
        }
    }
}