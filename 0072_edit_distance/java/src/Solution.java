import java.util.stream.IntStream;

class Solution {

    public int minDistance(String word1, String word2) {
        int word1Length = word1.length();
        int word2Length = word2.length();
        int[][] distanceTable = new int[word1Length + 1][word2Length + 1];
        for (int i = 0; i <= word1.length(); i++) {
            distanceTable[i][0] = i;
        }
        for (int j = 0; j <= word2.length(); j++) {
            distanceTable[0][j] = j;
        }

        for (int i = 1; i <= word1Length; i++) {
            for (int j = 1; j <= word2Length; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    distanceTable[i][j] = min(distanceTable[i - 1][j - 1],
                        distanceTable[i - 1][j] + 1,
                        distanceTable[i][j - 1] + 1);
                } else {
                    distanceTable[i][j] = min(distanceTable[i - 1][j - 1] + 1,
                        distanceTable[i - 1][j] + 1,
                        distanceTable[i][j - 1] + 1);
                }
            }
        }
//        for (int i = 0; i <= word1Length; i++) {
//            System.out.println(Arrays.toString(distanceTable[i]));
//        }
        return distanceTable[word1Length][word2Length];
    }

    private int min(int... nums) {
        return IntStream.of(nums).min()
            .orElseThrow(() -> new IllegalArgumentException("invalid input"));
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minDistance("horse", "ros"));
        System.out.println(solution.minDistance("microsoft", "ncsoft"));
        System.out.println(solution.minDistance("zoologicoarchaeologist", "zoogeologist"));
    }
}
