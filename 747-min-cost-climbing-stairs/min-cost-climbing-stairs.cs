public class Solution {
    public int MinCostClimbingStairs(int[] cost) {
        int n = cost.Length;
        int[] memo = new int[n];
        Array.Fill(memo, -1);

        int cc = Math.Min(Dfs(0), Dfs(1));
        int Dfs(int i){
            if(i>=n)
                return 0;
            if(memo[i] != -1)
                return memo[i];

            memo[i] = cost[i] + Math.Min(Dfs(i+1), Dfs(i+2));
            return memo[i];
        }

        return cc;
    }
}