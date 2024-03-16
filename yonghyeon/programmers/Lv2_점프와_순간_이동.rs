
struct Solution; 
impl Solution{
    fn solution( mut n:i32) -> i32{
        let mut result = 0;
        while n > 0{
            result += n%2;
            n /= 2;
        }
        result 
    }
}

fn main(){
    let  n:i32 = 5000;
    println!("{}",Solution::solution(n));

}
