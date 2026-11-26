package class_manipulation

class Person(
    val name: String,
    var age: Int
) {
    fun introduce(): String {
        return "My name is $name and I am $age years old."
    }

    fun haveBirthday() { 
        age++ 
    }
}

fun runClassManipulation() {
    val person = Person(
        name = "Alex",
        age = 16
    )
    
    val secondPerson = Person(
        name = "Benjamin",
        age = 18
    )

    println(person.name)
    println(person.age)

    println(person.introduce())

    person.haveBirthday()

    println(person.introduce())
    
    println(secondPerson.name)
    println(secondPerson.age)
    
    println(secondPerson.introduce())
    
    secondPerson.haveBirthday()
    
    println(secondPerson.introduce())
}