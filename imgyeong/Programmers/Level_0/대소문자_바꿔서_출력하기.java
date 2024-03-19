import java.util.Scanner;

public class 대소문자_바꿔서_출력하기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String str = "";
		for (int i = 0; i < a.length(); i++) {
			char ch = a.charAt(i);
			if (ch >= 65 && ch <= 90) {
				str += String.valueOf(ch).toLowerCase();
			} else {
				str += String.valueOf(ch).toUpperCase();
			}
		}
		System.out.println(str);
	}
}
