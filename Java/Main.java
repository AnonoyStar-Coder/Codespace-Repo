class Person {
    String name;
    int age;

    // Parameterized constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Method to display person information
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a Person object using the parameterized constructor
        Person person1 = new Person("John", 30);
        Person person2 = new Person("Alice", 25);

        // Displaying information for person1
        person1.displayInfo();

        // Displaying information for person2
        person2.displayInfo();
    }
}
