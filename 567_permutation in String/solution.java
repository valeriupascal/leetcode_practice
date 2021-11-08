class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int leng = s1.length();
        int[] map = new int[128];
        //put s1 in map array. +1 for each character adress
        for(char c: s1.toCharArray()) {
            map[c]++;
        }
        
        int counter = s1.length();
        int start = 0;
        int end = 0;
        while (end < s2.length()) {
            char c1 = s2.charAt(end);
            if(map[c1] > 0) {
                counter--;
            }
            map[c1]--;
            end++;
            while(counter == 0) {
                if(end - start == leng)
                    return true;
                char c2 = s2.charAt(start);
                map[c2]++;
                if(map[c2] > 0)
                    counter ++;
                
                start++;
            }
        }
        return false;
    }
}
