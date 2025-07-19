public class Solution {
    public int Rob(int[] nums) {
        int[] memo = new int[nums.Length];
        Array.Fill(memo, -1);
        
        int t = Dfs(0);

        int Dfs(int i){
            if(i >= nums.Length)
                return 0;
            if(memo[i] != -1)
                return memo[i];
                
            memo[i] = Math.Max(nums[i] + Dfs(i+2), Dfs(i+1));
            return memo[i];
        }

        return t;
    }
}