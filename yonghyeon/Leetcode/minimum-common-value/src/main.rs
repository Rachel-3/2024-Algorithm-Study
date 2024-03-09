struct Solution;
impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut i = 0;
        let mut j = 0;

        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                result = nums1[i];
                break;
            } else if nums1[i] < nums2[j] {
                i += 1;
            } else {
                j += 1;
            }
        }
        if result != 0 {
            result
        } else {
            -1
        }
    }
}
fn main() {
    let nums1 = vec![1, 2, 3];
    let nums2 = vec![2, 3, 4];
    let result = Solution::get_common(nums1, nums2);
    println!("{}", result);
    println!("Hello, world!");
}
