fn main() {
    println!("1 + 2 = {}", 1u32 + 2);
    println!("1 - 2 = {}", 1i32 - 2);
    //sub try u32
    //println!("1 - 2 = {} (u32)", 1u32 - 2);
    //error: this arithmetic operation will overflow
    //error: aborting due to previous error
    //u* 부호없는 속성으로 1에서 2을 뺴면 음수기에 오버플로 발생

    println!("9 / 2 = {}", 9u32 / 2);
    println!("9.0 / 2.0 = {}", 9.0 / 2.0);
    //부동소수점 형식은 f32와 f64 : def(f64)
    println!("3 * 6 = {}", 3 * 6);
    // 형식을 지정하지 않을경우 기본적으로 i32형식으로 지정


}