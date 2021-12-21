class Solution {
    public boolean solution(int x) {
        boolean answer = false;
        int q = 0;
        int a = x;
        int [] m = {1,10,100,1000,10000};
        for (int i=m.length-1; i>-1; i--){
            if (x/m[i] >= 1) q += (x/m[i]);
            x = x % m[i];
        }

        if (a % q == 0) answer = true;
        else answer = false;
        return answer;
    }
}
