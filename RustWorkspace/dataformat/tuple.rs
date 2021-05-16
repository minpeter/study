fn main() {
    //ver 1
    let ad = ("hello", 4i32, 'c');

    assert_eq!(ad.0, "hello"); //두 값이 다를경우 컴파일러가 알려줌
    println!("{} and {} and {}",ad.0, ad.1, ad.2)


}