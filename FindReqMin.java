import java.util.*;

public class FindReqMin {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq= new PriorityQueue<>(Collections.reverseOrder());
        int [] arr= {29,11,17,8,25,16,3,9,20,30};
        for (int index = 0; index < arr.length; index++) {
            pq.offer(arr[index]);
        }
        System.out.println(pq);
        System.out.println("n-1 minimum : "+pq.poll());
    }
}
