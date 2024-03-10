use std::collections::HashMap;
impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut hash: HashMap<i32, bool> = HashMap::new();
        for i in 0..nums1.len() {
            for j in 0..nums2.len() {
                if nums1[i] == nums2[j] {
                    result.push(nums1[i]);
                }
            }
        }
        result.retain(|&x| hash.insert(x, true).is_none());
        result
    }
}
