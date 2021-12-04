use regex::Regex;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = BufReader::new(File::open("8.txt").unwrap());
    let lines: Vec<_> = file.lines().map(|line| line.unwrap()).collect();

    let mut sum1 = 0;
    let mut sum2 = 0;
    let re_quote = Regex::new(r#"\\""#).unwrap();
    let re_backslash = Regex::new(r"\\\\").unwrap();
    let re_hex = Regex::new(r"\\x[0-9a-fA-F]{2}").unwrap();
    for line in lines.iter() {
        let total_len = line.len();
        let rem_backslash_line = re_backslash.replace_all(line, "x");
        let add_backslash_line = re_backslash.replace_all(line, "xxxx");
        let rem_quote_line = re_quote.replace_all(&rem_backslash_line, "x");
        let add_quote_line = re_quote.replace_all(&add_backslash_line, "xxxx");
        let part1_line = re_hex.replace_all(&rem_quote_line, "x");
        let part2_line = re_hex.replace_all(&add_quote_line, "xxxxx");
        let str_len1 = part1_line.len() - 2; // "" chars
        let str_len2 = part2_line.len() + 4; // "" chars
        sum1 += total_len - str_len1;
        sum2 += str_len2 - total_len;
    }
    println!("Part 1: {}", sum1);
    println!("Part 2: {}", sum2);
}
