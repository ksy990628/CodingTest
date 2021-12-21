import java.util.Arrays;
import java.util.Collections;

class Solution {
    public static long solution(long n) {
        long answer = 0;
        String n_ = Long.toString(n);
        Long [] arr = new Long[n_.length()];
        for (int i=0; i<n_.length(); i++){
            arr[n_.length()-i-1] = Long.valueOf(n_.charAt(i)-'0');
        }
        Arrays.sort(arr, Collections.reverseOrder());
        String answer_ = "";
        for (int i=0; i<n_.length(); i++){
            answer_ += arr[i];
        }
        answer = Long.parseLong(answer_);
        return answer;
    }}
