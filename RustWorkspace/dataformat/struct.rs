fn main() {
    struct Person {
        name: String,
        age: u8,
        likes_oranges: bool

    }

    let person = Person {
        name: String::from("minpeter"),
        age: 17,
        likes_oranges: true
    };
    
    println!("name: {}, age: {}, likes_oranges: {}",person.name,person.age,person.likes_oranges);

}