#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 노드 정의
typedef struct _node {
    int idx; // 선수의 인덱스
    struct _node* nx[26]; // 알파벳에 대응하는 다음 노드 포인터 배열
} node;

// 노드 생성 함수
node* create_node() {
    node* np = (node*)malloc(sizeof(node));
    for(int i = 0; i < 26; i++) np->nx[i] = NULL; // 모든 자식 노드 초기화
    return np;
}

// 노드 삭제(재귀적으로 자식 노드도 삭제)
void delete_node(node* np) {
    for(int i = 0; i < 26; i++) {
        if(np->nx[i]) delete_node(np->nx[i]);
    }
    free(np); // 메모리 해제
}

// 선수 이름을 트라이에 추가하는 함수
void add_node(node* root, char* str, int idx) {
    node* np = root;
    while(*str) {
        int i = *str++ - 'a'; // 현재 문자에 해당하는 인덱스
        if(!np->nx[i]) np->nx[i] = create_node(); // 해당 자식 노드가 없으면 생성
        np = np->nx[i]; // 다음 노드로 이동
    }
    np->idx = idx; // 마지막 노드에 선수의 인덱스 저장
}

// 이름에 해당하는 선수의 인덱스를 찾는 함수
int find_idx(node* root, char* str) {
    node* np = root;
    while(*str) {
        int i = *str++ - 'a'; // 현재 문자에 해당하는 인덱스
        np = np->nx[i]; // 다음 노드로 이동
    }
    return np->idx; // 마지막 노드의 인덱스 반환
}

// 두 문자열 포인터의 값을 교환하는 함수
void swap(char** a, char** b) {
    char* tmp = *a;
    *a = *b;
    *b = tmp;
}

// 메인 솔루션 함수
char** solution(const char* players[], size_t players_len, const char* callings[], size_t callings_len) {
    char** answer = (char**)malloc(players_len * sizeof(char*)); // 결과 배열 동적 할당
    node* root = create_node(); // 트라이의 루트 노드 생성
    for(int i = 0; i < players_len; i++) {
        answer[i] = (char*)malloc((strlen(players[i]) + 1) * sizeof(char)); // 선수 이름 저장 공간 할당
        strcpy(answer[i], players[i]); // 선수 이름 복사
        add_node(root, players[i], i); // 선수 이름을 트라이에 추가
    }
    for(int i = 0; i < callings_len; i++) {
        int idx = find_idx(root, callings[i]); // 호출된 선수의 인덱스 찾기
        if(idx > 0){ // 첫 번째 선수가 아니라면 교환
            add_node(root, answer[idx], idx - 1);
            add_node(root, answer[idx - 1], idx);
            swap(&answer[idx], &answer[idx - 1]); // 선수 위치 교환
        }
    }

    delete_node(root); // 트라이 메모리 해제
    return answer; // 최종 순위 배열 반환
}
