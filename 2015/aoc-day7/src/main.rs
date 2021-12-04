use std::collections::HashMap;
use std::fs;

fn main() {
    let mut registers: HashMap<&str, u16> = HashMap::new();
    let filename = "7.txt";
    let content_string = fs::read_to_string(filename).expect("Couldn't read the file");
    let lines = content_string.lines().collect::<Vec<&str>>();
    let target_len = lines.len();
    loop {
        let mut ctr = 0;
        for line in &lines {
            let split_vec: Vec<&str> = line.split(" -> ").collect();
            let target = split_vec[1];
            let commands: Vec<&str> = split_vec[0].split(' ').collect();
            let res = copy_val(commands, target, &mut registers);
            if res {
                ctr += 1;
            }
        }
        if ctr == target_len {
            break;
        }
    }
    let a_val = registers.get("a").unwrap();
    println!("Part1: {}", a_val);
    let mut registers: HashMap<&str, u16> = HashMap::new();
    loop {
        let mut ctr = 0;
        for line in &lines {
            let split_vec: Vec<&str> = line.split(" -> ").collect();
            let target = split_vec[1];
            let commands: Vec<&str> = split_vec[0].split(' ').collect();
            if target == "b" && commands.len() == 1 {
                if !registers.contains_key("b") {
                    registers.insert("b", *a_val);
                }
                ctr += 1;
                continue;
            }
            let res = copy_val(commands, target, &mut registers);
            if res {
                ctr += 1;
            }
        }
        if ctr == target_len {
            break;
        }
    }
    let new_a_val = registers.get("a").unwrap();
    println!("Part2: {}", new_a_val);
}

fn copy_val<'a>(
    commands: Vec<&'a str>,
    target: &'a str,
    registers: &mut HashMap<&'a str, u16>,
) -> bool {
    let mut final_val: u16;
    match commands.len() {
        1 => {
            if is_string_numeric(commands[0]) {
                let msg = format!("Couldn't parse: {}", commands[0]);
                final_val = commands[0].parse().expect(&msg)
            } else if registers.contains_key(&commands[0]) {
                final_val = *registers.get(&commands[0]).unwrap();
            } else {
                return false;
            }
        }
        2 => {
            let val = commands[1];
            if is_string_numeric(val) {
                let msg = format!("Couldn't parse: {}", val);
                final_val = val.parse().expect(&msg);
            } else if registers.contains_key(&val) {
                final_val = *registers.get(&val).unwrap();
            } else {
                return false;
            }
            final_val = !final_val;
        }
        _ => {
            let (left, operand, right) = (commands[0], commands[1], commands[2]);
            let left_val: u16;
            let right_val: u16;
            if is_string_numeric(left) {
                let msg = format!("Couldn't parse: {}", left);
                left_val = left.parse().expect(&msg);
            } else if registers.contains_key(&left) {
                left_val = *registers.get(&left).unwrap();
            } else {
                return false;
            }
            if is_string_numeric(right) {
                let msg = format!("Couldn't parse: {}", right);
                right_val = right.parse().expect(&msg);
            } else if registers.contains_key(&right) {
                right_val = *registers.get(&right).unwrap();
            } else {
                return false;
            }
            match operand {
                "AND" => final_val = left_val & right_val,
                "OR" => final_val = left_val | right_val,
                "RSHIFT" => final_val = left_val >> right_val,
                "LSHIFT" => final_val = left_val << right_val,
                _ => final_val = 0,
            };
        }
    }
    registers.insert(target, final_val);
    true
}

fn is_string_numeric(str: &str) -> bool {
    for c in str.chars() {
        if !c.is_numeric() {
            return false;
        }
    }
    true
}
