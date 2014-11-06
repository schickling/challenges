use std::iter::range_step;

fn main () {
    let mut x = 9i;
    let mut y = 8i;
    for i in range_step(7i, -1, -1) {
        if x > y {
            y = y * 10 + i;
        } else {
            x = x * 10 + i;
        }
    }
    println!("{} {}", x, y);
}
