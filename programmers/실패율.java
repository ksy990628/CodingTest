# 정확도가 왜 70이지...

import java.util.*;
class Solution {
    public static int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int people = stages.length;
        int clear = people;
        Arrays.sort(stages);
        Double [][] failure = new Double[N][2];
        for (int i=1; i<=N; i++){
            int fail = 0;
            for (int j=0; j<people; j++){
                if (stages[j] == i) fail ++;
                else if (stages[j] > i) break;
            }
            failure[i-1][0] = (double)i;
            failure[i-1][1] = (double)fail/clear;
            clear -= fail;
        }

        //Arrays.sort(failure, Comparator.comparingDouble(o1 -> o1[1]));
        Arrays.sort(failure, (o1, o2) -> {
            if(o1[1] == o2[1]){
                return Double.compare(o2[0], o1[0]);
            }else{
                return Double.compare(o2[1], o1[1]);
            }
        });
        for (int i=0; i<failure.length; i++){
            //System.out.println(failure[i][0].intValue()+" " + failure[i][1]);
            answer[i] = failure[i][0].intValue();
        }
        //System.out.println(Arrays.toString(answer));
        return answer;
    }
    public static void main(String [] args) {
//        Scanner scanner = new Scanner(System.in);
//        String input = scanner.nextLine();
//        char ch = input.charAt(0);
//        System.out.println((int)ch);
        //int num = Integer.parseInt(input);
        int [] arr = {2, 1, 2, 6, 2, 4, 3, 3};
        System.out.println(solution(5,arr));
        }
}

