import java.util.Arrays;

public class Solution {
    //solve1. reclusive
//    public int change(int amount, int[] coins){
//        return calculate(0, amount, coins);
//    }
//
//    private int calculate(int index, int amount, final int[] coins){
//        if(amount == 0)
//            return 1;
//        int ways = 0;
//        for(int i = index; i < coins.length; i++){
//            if(coins[i] <= amount){
//                ways += calculate(i, amount - coins[i], coins);
//            }
//        }
//        return ways;
//    }

    //solve2. dp
    public int change(int amount, int[] coins){
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        //coin이 [1, 2, 5] 일 때,
        //1로 만들 수 있는 경우의 수, 1,2로 만들 수 있는 경우의 수, 1,2,5 순서로 누적시키면 됨
        for(int i = 0; i < coins.length; i++){
            for(int amountIndex = coins[i]; amountIndex <= amount; amountIndex++){
                if(coins[i] <= amountIndex){
                    dp[amountIndex] += dp[amountIndex - coins[i]];
                }
            }
        }
        System.out.println(Arrays.toString(dp));
        return dp[amount];
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.change(5, new int[]{1, 2, 5}));
        System.out.println(solution.change(3, new int[]{2}));
        System.out.println(solution.change(10, new int[]{10}));
    }
}
