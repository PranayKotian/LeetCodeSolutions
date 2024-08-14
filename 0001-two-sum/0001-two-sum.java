class Solution {
    public int[] twoSum(int[] nums, int target) {
         
        //Convert array to hashtable
        //Iterate through array and see if matching value is in hashtable
        // If value in hashtable, return index pair
        
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            hash.put(nums[i], i); 
        }
        
        for (int i = 0; i < n; i++) {
            int val = target - nums[i];
            if (hash.containsKey(val) && hash.get(val) != i) {
                return new int[]{i, hash.get(val)};
            } 
        }
        
        return new int[]{};
    }
}