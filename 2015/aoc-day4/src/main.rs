use md5;

fn main() {
    let input = "bgvyzdsv";
    // first 2 bytes must be zero and third must be < 16 so that the
    // third byte's hex starts with 0
    let num1 = find_zeroes(input, &[0, 0], 1); // starts with 5 zeroes
    // first 3 bytes must all be zero
    let num2 = find_zeroes(input, &[0, 0, 0], num1); // starts with 6 zeroes
    println!("Part 1: {}", num1);
    println!("Part 2: {}", num2);
}

fn find_zeroes(input: &str, zeroes: &[u8], starting_num: i32) -> i32 {
    let mut num = starting_num;
    loop {
        let digest = md5::compute(format!("{}{}", input, num));
        // digest[2] checks the 3rd byte for Part 1
        if digest.starts_with(zeroes) && digest[2] < 16 {
            break num;
        } else {
            num += 1;
        }
    }
}
