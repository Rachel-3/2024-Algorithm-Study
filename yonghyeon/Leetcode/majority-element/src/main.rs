struct Solution;
use std::collections::HashMap;
impl Solution{
    pub fn majority_element(nums:Vec<i32>) -> i32{
        if nums.len() == 0 { return 0;}
        let mut num_hash = HashMap::new();

        for i in nums{
        
            *num_hash.entry(i).or_insert(0) += 1;
           
        }
        //https://stackoverflow.com/questions/63950197/sort-a-hashmap-by-values-in-rust
        let mut nums_vec:Vec<(&i32, &i32)> = num_hash.iter().collect();
        nums_vec.sort_by(|a,b| b.1.cmp(a.1));
        println!("{:?}",nums_vec);
        
        return *nums_vec[0].0;
    }

    pub fn majority_element_major(nums: Vec<i32>) -> i32 {
        let mut count: i32 = 0;
    let mut candidate = 0;

    for num in nums {
        if count == 0 {
            candidate = num;
        }
        if num == candidate {
            count += 1;
        } else {
            count -= 1;
        }
    }

    candidate
    }
}
fn main() {
    let nums:Vec<i32> = vec![3,2,3] ;

    
    let result = Solution::majority_element(nums);
    println!("{}",result);
}
