import java.util.ArrayList;
import java.util.HashSet;

public class OtherSolution-문자열이-몇번-등장하는지-세기{

    public static void main(String[] args) {
        int answer = 0;
        String str = "banana";
        String str2 = "ana";
        
        ArrayList list = new ArrayList(10);
        for(int i = 0; i <= str.length(); i++){
            list.add(str.indexOf(str2, i));
        }

        HashSet<String> hs = new HashSet<String>(list);
        list.clear();
        list.addAll(hs);
        list.remove(Integer.valueOf(-1));
        answer = list.size();
        System.out.println(answer);
    }
}