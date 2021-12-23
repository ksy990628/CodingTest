# 아 정답은 맞는데.....런타임 에러....

import java.util.*;
class Solution {
    public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int people = stages.length;
        int clear = people;
        Arrays.sort(stages);
        Float [] failure = new Float[N];

        for (int i=1; i<=N; i++){
            int fail = 0;
            for (int j=0; j<people; j++){
                if (stages[j] == i) fail ++;
                else if (stages[j] > i) break;
            }
            float result = (float)fail/clear;
            failure[i-1] = result;
            clear -= fail;
        }

        Float [] failure2 = new Float[N];
        System.arraycopy(failure,0,failure2,0,N);
        Arrays.sort(failure2, Collections.reverseOrder());

        int [] path = new int[5];
        for (int x=0; x<N; x++){
            for (int y=0; y<N; y++){
                if (failure2[x] == failure[y]){
                    answer[x] = y+1;
                    path[x] = y;
                    break;
                }
            }
        }

        System.out.println(Arrays.toString(failure));
        System.out.println(Arrays.toString(failure2));
        System.out.println(Arrays.toString(answer));
        return answer;
    }
    public static void main(String [] args) {
        int [] arr = {2, 1, 2, 6, 2, 4, 3, 3};
        System.out.println(solution(5,arr));
        }
}

