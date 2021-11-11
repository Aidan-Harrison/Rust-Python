fn add(x: i32) -> i32 {
    x + 17
}

fn sub(x: f32, y: f32) -> f32 {
    x - y
}

fn PrintString(s: &String) { // Check!
    println!("{}", s)
}

fn ReturnStringPart(s: &String) -> &str {
    let bytes = s.as_bytes();

    for(i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}

// Check ReverseString and Reverse
fn Reverse(s: &String, start: i32, end: usize) {
    while x < y {
        let temp = s[start]; // Check!
        s[start] = s[end];
        s[end] = temp; // Can't index with usize, have to use i'x'!
        start++;
        end--;
    }
}

fn ReverseString(s: &String) -> &String {
    let mut revStr = s // Check!
    Reverse(&revStr, 0, revStr.len());
    &revStr
}

// Comment
fn main() {
    println!("Hello world!\n");

    let mut guess = String::new();

    let mut testString = String::from("Test String"); // Assign string literal to string

    PrintString(&mut testString);

    let stringPart = ReturnStringPart(&mut testString);
    println!("{}", stringPart);

    ReverseString(&testString); // Fix! If not, continue documentation

    std::io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessd {}", guess);

    let x = 45;
    let y = 10;

    println!("x is {} and y is {}", x, y);

    let a = add(16);
    println!("a is {}", a);

    println!("{}", sub(15.0, 15.0));
}