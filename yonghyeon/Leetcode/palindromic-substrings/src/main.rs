/*https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-10
647. Palindromic Substrings [Rust]*/
struct Solution;
impl Solution{
    pub fn count_substrings(s: String) -> i32 {
        let str_len = s.len();
        if str_len == 0 {return 0;}
        //문자열을 배열로 수정
        let s_chars:Vec<char> = s.chars().collect();
        let mut count = 0; 
        
        //문자열 `s`내에서 회문인 모든 하위 문자열 식별 
        for i in 0..str_len{
            //left : [https://miro.medium.com/v2/resize:fit:354/1*5bd_OBT6Nha2Wl05asyqfg.png]
            let mut left:isize= i as isize;//isize로 변환하여 음수 인덱스 처리 
            let mut right =i;
           //짝수 길이 회문을 찾음 -> 같은 위치
            while left >= 0 && right < str_len && s_chars[left as usize] == s_chars[right] {
              
                count += 1;//카운트 증가
                left  -=1;//L 확장
                right +=1;//R 확장 
            }
            //짝수 길이 회문을 찾음 -> 인접한 위치
            let mut left= i as isize;//isize로 변환하여 음수 인덱스 처리 
            let mut right =i+1;
            //왼쪽 또는 오른쪽으로 확장하며 회문 검사
            while left >= 0 && right < str_len && s_chars[left as usize] == s_chars[right] {
                
                count += 1;//카운트 증가
                left  -=1;//L 확장
                right +=1;//R 확장 
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

