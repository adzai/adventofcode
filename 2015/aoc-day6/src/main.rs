use std::fs;

#[derive(Debug)]
struct Light {
    on: bool,
}

fn main() {
    let content_string = fs::read_to_string("6.txt").expect("Couldn't read the file");
    let input_split = content_string.split("\n");
    let mut lights = init_lights();
    for command in input_split {
        if command == "" {
            continue;
        }
        let mut cmd = command.replace("turn ", "");
        cmd = cmd.replace(" through", "");
        let cmd_split: Vec<&str> = cmd.split(" ").collect();
        let mut range1 = cmd_split[1].split(",").collect::<Vec<&str>>();
        let mut range2 = cmd_split[2].split(",").collect::<Vec<&str>>();
        let tmp = range1[1];
        range1[1] = range2[0];
        range2[0] = tmp;
        let mut r1: Vec<usize> = range1
            .into_iter()
            .map(|elem| elem.parse().unwrap())
            .collect();
        let mut r2: Vec<usize> = range2
            .into_iter()
            .map(|elem| elem.parse().unwrap())
            .collect();
        r1.sort();
        r2.sort();
        for x in r1[0]..=r1[1] {
            for y in r2[0]..=r2[1] {
                match cmd_split[0] {
                    "on" => lights[x][y] += 1,
                    "off" => {
                        if lights[x][y] > 0 {
                            lights[x][y] -= 1;
                        }
                    }
                    _ => lights[x][y] += 2,
                };
            }
        }
    }
    let mut acc = 0;
    for inner in lights {
        for light in inner {
            acc += light;
        }
    }
    println!("Res: {}", acc);
}

fn init_lights() -> Vec<Vec<i32>> {
    let mut ret: Vec<Vec<i32>> = Vec::new();
    for _ in 0..1000 {
        let mut new_vec: Vec<i32> = Vec::new();
        for _ in 0..1000 {
            new_vec.push(0);
        }
        ret.push(new_vec);
    }
    ret
}
