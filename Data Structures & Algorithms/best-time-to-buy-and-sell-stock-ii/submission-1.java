class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        for(int i=0; i<prices.length-1; i++)
        {
            int t = prices[i+1]-prices[i];
            if(t>0)
            {   profit= profit+t;   }
        }
        return profit;
    }
}

    