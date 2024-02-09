# 368. Largest Divisible Subset
## Intuition
* 요소 쌍이 나눙어 떨어지는 가장 큰 부분집합을 찾기
* 요소들이 나누어 떨어지는 관계를 확인하여 이를 기반으로 부분집합을 구성
* 동적 프로그래밍을 이용하여 각 단계에서의 최적의 해결책을 구축하여 접근 함

## Approach
* 정렬 : 배열을 오름차순으로 정렬
* 동적 프로그래밍(DP) 초기화 : 각 요소들 사이의 나누어 떨어지는 가장 큰 부분집합의 길이를 저장하는 배열 `dp`를 초기화
* 부분집합 구성 : 각 모든 요소들의 비교하여 나누어 떨어지는 관계를 확인 만약 요소가 `nums[i]`가 `nums[j]`로 나누어 떨어진다면 dp[i]는 dp[j]+1로 업데이트하고 prev[i]는 Some(j)로 이전 요소의 인덱스를 저장함 ( 현재 요소의 인덱스는 max_index로 저장하고 있으며,그 전 요소의  인덱스는 전부 prev에 저장)
* 최대 부분집합 찾기 : `dp` 배열을 통해 max_index를 현재 인덱스의 값으로 업데이트 함
* 역추적 :  `result`배열에 최초 `current`는 max_index의 값을 벡터에 저장하고, `prev`배열은  Some 값을 가질 때만  저장하고 이를 반복함

## Complexity
- Time complexity: O(n^2)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n){`dp` 배열, `prev` 배열,`result`배열 }
- 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## Code 
```
struct  Solution;

impl Solution {
    pub fn largest_divisible_subset(mut nums: Vec<i32>) -> Vec<i32> {
    
        // 빈 벡터인 경우, 빈 벡터를 반환.
        if nums.is_empty() { return vec![]; }
        // nums 벡터를 오름차순으로 정렬합니다.
        nums.sort_unstable();

            let nums_size = nums.len();

           // dp 배열을 초기화 -> 각 요소는 자신을 포함하는 최대 부분집합의 길이를 저장합니다.dp[1,1,1,1]
           let mut dp = vec![1; nums_size];

            //// prev 배열을 초기화 -> 각 요소는 부분집합에서 이전 요소의 인덱스를 저장 prev[None,None,None,None]
            let mut prev = vec![None; nums_size];
            // 최대 부분집합의 길이를 추적합니다.
            let mut max_size = 1;
            // 최대 부분집합의 마지막 요소의 인덱스를 추적합니다.
            let mut max_index = 0;
        /*동적 프로그래밍:
        i = 1 (nums[1] = 2)일 때, j = 0 (nums[0] = 1)을 확인, 2 % 1 == 0이므로, dp[1]을 dp[0] + 1 = 2로 업데이트함  prev[1] = 0.
        i = 2 (nums[2] = 4)일 때, j = 0과 1을 확인, 4 % 1 == 0이고 4 % 2 == 0이므로, dp[2]를 dp[1] + 1 = 3로 업데이트함 prev[2] = 1.
        i = 3 (nums[3] = 8)일 때, j = 0, 1, 2를 확인, 8 % 1 == 0, 8 % 2 == 0, 8 % 4 == 0이므로, dp[3]를 dp[2] + 1 = 4로 업데이트함. prev[3] = 2. */
        for i in 1..nums_size{
            for j in 0..i{
                println!("dp {:?}",dp);
                println!("prev {:?}",prev);
                println!("max_size:{}",max_size);
                println!("max_index:{}",max_index);
                if nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i] { 
                    dp[i] = dp[j]+1; // nums[i]가 nums[j]로 나누어 떨어지면, dp[i]를 업데이트함
                    prev[i] = Some(j); // 이전 요소의 인덱스를 저장
                }
            }
            //각 nums[i]에 대해, 가능한 모든 j (j < i)를 확인하여 dp[i]와 prev[i]를 업데이트함
            if dp[i] >max_size{
                max_size  = dp[i];
                max_index = i;
            }
        }
        println!(" 결과 과정");
        println!("dp {:?}",dp);
        println!("prev {:?}",prev);
        println!("max_size:{}",max_size);
        println!("max_index:{}",max_index);
      
        //역추적
       // result 벡터를 max_size(usize) 용량으로 초기화합니다.
    let mut result = Vec::with_capacity(max_size);
     // 역추적을 시작하여 결과 벡터를 구성합니다.
    let mut current = Some(max_index);
//while let Some(idx) = current 구문을 사용하여 current가 Some 값을 가질 때만 반복하여 current변수가 유효한 인덱스가 없을 경우 자동으로 루프 종료
        while let Some(idx) = current{
            println!("result {:?}",result);
            result.push(nums[idx]);
            current = prev[idx];
            
        }

       // 결과 벡터의 순서를 뒤집어서 정렬된 순서로 만듬
        result.reverse();
        result// 최종 결과를 반환
    }
}

fn main() {
    let nums: Vec<i32> = vec![1,2,3,4];
    let subset = Solution::largest_divisible_subset(nums);
    println!("{:?}", subset); // 출력하여 확인
}

```
