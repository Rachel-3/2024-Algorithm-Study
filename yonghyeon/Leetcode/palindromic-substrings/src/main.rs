/*https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-10
647. Palindromic Substrings [Rust]*/
struct Solution;
impl Solution{
    pub fn count_substrings(s: String) -> i32 {
        let str_len = s.len();
        if str_len == 0 {return 0;}
        
        let s_chars:Vec<char> = s.chars().collect();
        let mut count = 0;

        for i in 0..str_len{
            let mut left:isize= i as isize;
            let mut right =i;
            while left >= 0 && right < str_len && s_chars[left as usize] == s_chars[right] {
              
                count += 1;
                left  -=1;
                right +=1;
            }
            let mut left= i as isize;
            let mut right =i+1;
            while left >= 0 && right < str_len && s_chars[left as usize] == s_chars[right] {
                
                count += 1;
                left  -=1;
                right +=1;
            }
        }
        count
    }
}
fn main() {
    let str1 = String::from("aaa");
    let s =   Solution::count_substrings(str1);
    println!("{}",s);
}

