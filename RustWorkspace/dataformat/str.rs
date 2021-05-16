fn main() {
    // Create a String from a string literal
    let mut hello = String::from("hello, ");  

    // Push a character into our String
    hello.push('w'); //push char
    
    // Push a string literal into our String       
    hello.push_str("orld!"); //push_str string
             
    println!("{}", hello)
}