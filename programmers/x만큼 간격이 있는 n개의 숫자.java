class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long temp = 1;
        for (int i=0; i<n; i++){
            answer[i] = x*temp;
            temp += 1;
        }
        return answer;
    }
}
