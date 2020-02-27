import java.util.Arrays;

public class Solution {

    public int longestCommonSubsequence(String text1, String text2) {
        int text1Length = text1.length();
        int text2Length = text2.length();
        int[][] dpTable = new int[text1Length + 1][text2Length + 1];

        for (int i = 1; i <= text1Length; i++) {
            for (int j = 1; j <= text2Length; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dpTable[i][j] = dpTable[i-1][j-1] + 1;
                } else {
                    dpTable[i][j] = Math.max(dpTable[i-1][j], dpTable[i][j - 1]);
                }
            }
        }
//        for (int i = 0; i <= text1Length; i++) {
//            System.out.println(Arrays.toString(dpTable[i]));
//        }
        return dpTable[text1Length][text2Length];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestCommonSubsequence("abc", "abcde"));
        System.out.println(solution.longestCommonSubsequence("abgfgh", "abcdgfgh"));
    }
}
