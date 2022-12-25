fn main() {
    let base_10: i64 = 10;
    let trip_length: i64 = base_10.pow(6); //10^5 km in 100 meters
    let mut n_packages: i64 = 0;
    let mut counter: i64 = 0;
    let mut laps: i64 = 0;
    let mut total_deers: i128 = 0;

    for _iter in 0..trip_length {
        n_packages += 1;
        if counter == base_10.pow(4) {
            let deer_weight = total_deers * 100 as i128;
            let gift_weight = (n_packages / 10) as i128;
            let weight_on_sled = deer_weight + gift_weight;
            let deers_needed = (weight_on_sled as f64 / 200.0) + 5.0;
            println!("{}", deers_needed);
            total_deers += deers_needed.ceil() as i128;

            laps += 1;
            counter = 0;
        } else {
            counter += 1;
        }
    }

    println!(
        "Ended with, laps={} and n_gifts={}, total deers needed= {}",
        laps, n_packages, total_deers
    );
}
