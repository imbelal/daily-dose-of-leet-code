using System;

public class Solution
{
    public void Merge(int[] nums1, int m, int[] nums2, int n)
    {
        if (m == 0)
        {
            int i = 0;
            while (i < nums2.Length)
            {
                nums1[i] = nums2[i];
                i++;
            }
        }
        else if (n > 0)
        {
            int c = n;
            int d = m;
            int i = m + n - 1;

            while (i >= 0)
            {
                if (c == 0) break;
                if ((d == 0 && c != 0) || (nums1[d - 1] < nums2[c - 1]))
                {
                    nums1[i] = nums2[c - 1];
                    c--;
                }
                else
                {
                    nums1[i] = nums1[d - 1];
                    d--;
                    if (d == 0 && c == 0)
                    {
                        nums1[i - 1] = nums2[c - 1];
                    }
                }

                i--;
            }
        }

    }

    static void Main(string[] args)
    {
        Solution solution = new Solution();

        int[] nums1 = { 0, 0, 0, 0, 0 };
        int m = 0;
        int[] nums2 = { 1, 2, 3, 4, 5 };
        int n = 5;

        solution.Merge(nums1, m, nums2, n);

        foreach (var item in nums1)
        {
            Console.WriteLine(item);
        }
    }
}