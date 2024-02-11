# ✅647. Palindromic Substrings 🦀[Rust] 99.98%🔥 
## Intuition
* 문자열 `s`의 substring을 식별하는 것이 목표
* 회문은 앞으로 읽으나 뒤로 읽으나 같음
* 문자열 내의 모든 단일 문작가 회문이라는 점을 인식
## Approach
* 문자열의 각 문자를 반복 각 문자와 인접한 문자 쌍으로 회문의 substring의 중심으로 함
* 중심 주위를 넓혀가며 회문을 확인하고, 각 회문을 찾을 시 `count` 증가
*  인덱스 범위를 벗어나는 문제를 방지하기 위해 `left` 이동을 0보다 작아지지 않게하고, `right`는 문자열의 길이에 범위까지만 이동하게 함

## Complexity

- Time complexity:`O(n^2)` 
    * n:문자열의 길이 
    * 회문을 찾지 못하거나,문자열 길이의 범위까지 `left`,`right` 확장 

- Space complexity:`O(n)` 문자열 s의 벡터

## Code
``` Rust
impl Solution{
    pub fn count_substrings(s: String) -> i32 {
        let str_len = s.len();
        if str_len == 0 {return 0;}
        
        let s_chars:Vec<char> = s.chars().collect();
        let mut count = 0;

        for i in 0..str_len{
            let mut left= i;
            let mut right =i;
            while right < str_len && s_chars[left] == s_chars[right] {
              
                count += 1;
                if left == 0 as usize  { break}
                left  -=1;
                right +=1;
            }
            let mut left= i;
            let mut right =i+1;
            while right < s_chars.len() && s_chars[left] == s_chars[right] {
                
                count += 1;
                if left == 0 as usize  { break}
                left  -=1;
                right +=1;
            }
        }
        count
    }
}
```
