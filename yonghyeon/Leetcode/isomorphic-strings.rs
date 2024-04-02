struct Solution;
impl Solution {
    pub fn is_isomorphic (s: String, t:String) -> bool{

        let mut num1:Vec<i32> = vec![0;256];
        let mut num2:Vec<i32> = vec![0;256];
        for c in 0..s.chars().count(){
            //문자를 한 글자씩 출력 
       // println!("{}", s.chars().nth(c).unwrap());
       // println!("{}", t.chars().nth(c).unwrap());
            let s1 = s.chars().nth(c).unwrap() as i32;
            let s2 = t.chars().nth(c).unwrap() as i32;
             println!("s1 : {}",s1);
             println!("s2 : {}",s2);
            if num1[s1 as usize] != num2[s2 as usize] {
                println!("F:{}",num1[s1 as usize]);
                println!("F:{}",num2[s2 as usize]);
                return false;
            }
            num1[s1 as usize] = c as i32+1;
            num2[s2 as usize] = c as i32+1; 
            println!("s:{}",num1[s1 as usize]); 
            println!("s:{}",num2[s2 as usize]); 
        }
        return true           
    }
}

fn main() {
    let str1 = String::from("egg"); 
    let str2 = String::from("add"); 
    let result = Solution::is_isomorphic(str1,str2);
    println!("{}",result);
}

