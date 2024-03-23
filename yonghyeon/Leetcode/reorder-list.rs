// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        if head.is_none() {
            return;
        }

        // 단계 1: 중앙을 찾아 연결 리스트를 두 부분으로 나눕니다.
        let mut slow = head.clone();
        let mut fast = head.as_ref().unwrap().next.clone();
        while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
            slow = slow.unwrap().next;
            fast = fast.unwrap().next.unwrap().next;
        }

        // 단계 2: 뒤쪽 절반을 뒤집습니다.
        let mut prev = None;
        let mut curr = slow.unwrap().next.take();
        while let Some(mut node) = curr {
            let next_temp = node.next.take();
            node.next = prev;
            prev = Some(node);
            curr = next_temp;
        }

        // 단계 3: 두 리스트를 번갈아 가면서 합칩니다.
        let mut first = head.take();
        let mut second = prev;
        while let (Some(mut f_node), Some(mut s_node)) = (first.take(), second.take()) {
            first = f_node.next.take();
            f_node.next = Some(s_node.clone());
            s_node.next = first.clone();
            if let Some(node) = f_node.next.as_mut() {
                second = node.next.take();
                node.next = first.clone();
            }
            head.get_or_insert(f_node);
        }
    }
}
