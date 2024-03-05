import java.util.*;
class Lv1_대충_만든_자판 {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        String[] abc = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N" ,"O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        
        HashMap<String,Integer> map = new HashMap<>();
        for(int i = 0 ; i < 26 ; i++){
            map.put(abc[i],-1);
        }
        for(int i = 0; i < keymap.length; i++){
            for(int j = 0; j < keymap[i].length() ; j++){
                if(map.get(String.valueOf(keymap[i].charAt(j))) > j+1 || map.get(String.valueOf(keymap[i].charAt(j))) == -1){
                    map.replace(String.valueOf(keymap[i].charAt(j)) , j+1);
                }
            }
        }
        for(int i = 0 ; i < targets.length; i++){
            for(int j = 0; j < targets[i].length(); j++){
                if(map.get(String.valueOf(targets[i].charAt(j))) != -1){
                    answer[i] += map.get(String.valueOf(targets[i].charAt(j)));
                }
                else{
                    answer[i] = -1;
                    break;
                }
            }
        }
        return answer;
    }
}