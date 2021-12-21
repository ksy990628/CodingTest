class Solution {
    public static int GCD (int a, int b){
        int r = a % b;
        if (r == 0)
            return b;
        else
            return GCD(b, r);
    }

    public int[] solution(int n, int m) {
        int gcd = GCD(n,m);
        int lcm = n*m/gcd;

        int[] answer = {gcd,lcm};
        return answer;
    }
}
