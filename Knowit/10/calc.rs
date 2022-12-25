use std::collections::HashMap;

static base: i64 = 10;
static alpha: f64 = 0.2;
static delta: f64 = 83.0;
static beta: f64 = 0.1;
static r_max: f64 = base.pow(6) as f64;
static gamma: f64 = 0.000075;
static n_max: i64 = base.pow(8) as i64;

fn main() {
    let mut r_0: i64 = 125000;
    let mut u_0: i64 = 3500;
    let mut values = HashMap::new();
    values.insert(r_0, u_0);

    for _n in 1..n_max + 1 {
        let u: i64 = U(u_0 as f64, r_0 as f64);
        let r: i64 = R(u_0 as f64, r_0 as f64);

        let hashVal = values.get(&r);
        if hashVal.is_some() {
            if u == *hashVal.unwrap() {
                println!("Found cycle: {}", hashVal.unwrap());
            }
        }



        u_0 = u;
        r_0 = r;
        values.insert(r_0, u_0);
    }

    println!("{}", r_0);
}

fn U(u: f64, r: f64) -> i64 {
    return (u + (gamma * u * r) / delta - beta * u) as i64;
}

fn R(u: f64, r: f64) -> i64 {
    return (r + (alpha * r * (r_max - r)) / r_max - gamma * u * r) as i64;
}
