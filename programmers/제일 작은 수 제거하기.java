import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        int [] answer;
        if (arr.length == 1){
            answer = new int[]{-1};
        }
        else{
            answer = new int[arr.length-1];
            int [] temp = new int[arr.length];
            System.arraycopy(arr,0,temp,0,arr.length);
            int j = 0;
            Arrays.sort(temp);
            for (int i=0; i<arr.length; i++){
                if (arr[i] == temp[0]){
                    continue;
                }
                answer[j] = arr[i];
                j++;
            }
            for (int i=0; i<arr.length-1; i++){
                System.out.println(answer[i]);
            }
        }
        return answer;
    }
}
