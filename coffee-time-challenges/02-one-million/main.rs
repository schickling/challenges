fn main () {
    let mut a: int = 1;
    loop {
        if 1000000 % a == 0 {
            let b = 1000000 / a;
            if a % 10 != 0 && b % 10 != 0 {
                return println!("{} {}", a, b);
            }
        }
        a += 1;
    }
}
