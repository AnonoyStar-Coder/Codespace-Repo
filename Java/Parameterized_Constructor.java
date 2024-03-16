class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Parameterized_Constructor {
    public static void main(String[] args) {
        Person person1 = new Person("John", 30);
        Person person2 = new Person("Alice", 25);

        person1.displayInfo();

        person2.displayInfo();
    }
}
