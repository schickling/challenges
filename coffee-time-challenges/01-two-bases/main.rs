fn main () {
    for x in range(0i, 9) {
        for y in range(0i, 9) {
            for z in range(0i, 9) {
                if check(x, y, z) {
                    println!("{} {} {}", x, y, z);
                }
            }
        }
    }
}

fn check (x: int, y: int, z: int) -> bool {
    x * 10 * 10 + y * 10 + z == z * 9 * 9 + y * 9 + x
}
