class Solution {
    public int solution(int num) {
        int answer = 0;
        long x = num;
        while (x != 1 | answer < 500){
            if (x==1) break;
            answer += 1;
            if (x%2==0)  x=x/2;
            else   x=x*3+1;
        }
        
        if (answer >= 500) answer = -1;
        return answer;
    }
}
