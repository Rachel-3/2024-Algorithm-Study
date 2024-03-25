public class level_0_특정_문자열로_끝나는_가장_긴부분_문자열_찾기  {
	public static void main (String myString, String pat) {
		String longestSubstring = "";
		for (int i = 0; i < myString.length(); i++) {
			for (int j = i + 1; j <= myString.length(); j++) {
				String substring = myString.substring(i, j);
				if (substring.endsWith(pat) && substring.length() >= longestSubstring.length()) {
					longestSubstring = substring;
				}
			}
		}
		return longestSubstring;
	}
}