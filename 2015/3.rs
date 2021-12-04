use std::collections::HashSet;
use std::fs;

#[derive(Eq, PartialEq, Hash, Clone)]
struct Coordinates {
    x: i32,
    y: i32,
}

enum DeliveryPerson {
    Santa,
    RoboSanta,
}

fn main() {
    let contents = fs::read_to_string("3.txt").expect("Couldn't read the file");
    let part1_result = part1(&contents);
    let part2_result = part2(&contents);
    println!("Part 1: {}", part1_result);
    println!("Part 2: {}", part2_result);
}

fn process_instruction(symbol: &char, coordinates: &mut Coordinates) {
    match symbol {
        'v' => coordinates.y -= 1,
        '>' => coordinates.x += 1,
        '<' => coordinates.x -= 1,
        '^' => coordinates.y += 1,
        _ => (),
    }
}

fn part1(contents: &str) -> usize {
    let mut visited = HashSet::new();
    let mut santa_coordinates = Coordinates { x: 0, y: 0 };
    for c in contents.trim().chars() {
        process_instruction(&c, &mut santa_coordinates);
        visited.insert(santa_coordinates.clone());
    }
    visited.len()
}

fn part2(contents: &str) -> usize {
    let mut visited = HashSet::new();
    let mut santa_coordinates = Coordinates { x: 0, y: 0 };
    let mut robo_santa_coordinates = Coordinates { x: 0, y: 0 };
    let mut delivery = DeliveryPerson::Santa;
    for c in contents.trim().chars() {
        match delivery {
            DeliveryPerson::Santa => {
                process_instruction(&c, &mut santa_coordinates);
                visited.insert(santa_coordinates.clone());
                delivery = DeliveryPerson::RoboSanta;
            }
            _ => {
                process_instruction(&c, &mut robo_santa_coordinates);
                visited.insert(robo_santa_coordinates.clone());
                delivery = DeliveryPerson::Santa;
            }
        }
    }
    visited.len()
}
