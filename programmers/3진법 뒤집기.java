class Solution {
    public int solution(int n) {
        int answer = 0;
        int count = 0;
        int standard = 1;
        int a = n;
        while (a >= 3){
            a /= 3;
            count += 1;
            standard *= 3;
        }
        a = n;
        for (int i=0; i<count+1; i++){
            answer += (a % 3)*standard;
            a /= 3;
            standard /= 3;
        }
        return answer;
    }
}
