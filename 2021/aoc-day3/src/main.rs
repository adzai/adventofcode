fn main() {
    let input = include_str!("../3.txt")
        .split("\n")
        .filter(|x| *x != "")
        .collect::<Vec<&str>>();
    println!("Part 1: {}", part1(input.clone()));
    println!("Part 2 : {}", part2(input.clone(), input.clone(), 0));
}

fn get_bin(counts: &Vec<u32>, input_len: usize) -> String {
    let target = {
        if input_len % 2 == 0 {
            input_len / 2
        } else {
            input_len / 2 + 1
        }
    };
    counts.iter().fold("".to_string(), |string, val| {
        if *val as usize >= target {
            return format!("{}{}", string, "1");
        }
        return format!("{}{}", string, "0");
    })
}

fn not_string(orig_str: &str) -> String {
    orig_str
        .chars()
        .fold("".to_string(), |string, val| match val {
            '1' => format!("{}{}", string, "0"),
            '0' => format!("{}{}", string, "1"),
            _ => panic!("Expected 0 or 1, got {}", val),
        })
}

fn get_bit_sum(input: &Vec<&str>) -> Vec<u32> {
    let mut counts: Vec<u32> = vec![0; input[0].len()];
    for item in input {
        for (i, char) in item.chars().enumerate() {
            counts[i] += char.to_digit(10).unwrap_or(0);
        }
    }
    counts
}

fn collect_inputs(input: Vec<&str>, most_common: Option<char>, index: usize) -> Vec<&str> {
    if input.len() > 1 {
        let mut ret_input = input.clone();
        ret_input.retain(|&string| Some(string.chars().nth(index)) == Some(most_common));
        ret_input
    } else {
        input
    }
}

fn part1(input: Vec<&str>) -> i32 {
    let input_len = input.len();
    let counts = get_bit_sum(&input);
    let bin = get_bin(&counts, input_len);
    let epsilon = i32::from_str_radix(&not_string(&bin), 2).unwrap();
    let gamma = i32::from_str_radix(&bin, 2).unwrap();
    epsilon * gamma
}

fn part2(gamma_input: Vec<&str>, epsilon_input: Vec<&str>, i: usize) -> i32 {
    let gamma_input_len = gamma_input.len();
    let epsilon_input_len = epsilon_input.len();
    let gamma_counts = get_bit_sum(&gamma_input);
    let epsilon_counts = get_bit_sum(&epsilon_input);
    if gamma_input_len == 1 && epsilon_input_len == 1 {
        let epsilon = i32::from_str_radix(&gamma_input[0], 2).unwrap();
        let gamma = i32::from_str_radix(&epsilon_input[0], 2).unwrap();
        epsilon * gamma
    } else {
        let gamma_input_ret = collect_inputs(
            gamma_input,
            get_bin(&gamma_counts, gamma_input_len).chars().nth(i),
            i,
        );
        let epsilon_input_ret = collect_inputs(
            epsilon_input,
            not_string(&get_bin(&epsilon_counts, epsilon_input_len))
                .chars()
                .nth(i),
            i,
        );
        part2(gamma_input_ret, epsilon_input_ret, i + 1)
    }
}
