import java.util.*;
public class FindMinFS {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int [] arr = {11,13,7,8,9,14};
        for(int i=0;i<arr.length;i++){
           pq.offer(arr[i]);
        }
        //pq.poll();
         System.out.println(pq);
        System.out.println("first min element : " + pq.poll());
      //  pq.poll();

       // System.out.println("first min element" + pq);
        System.out.println("second min element : "+ pq.peek());

    }
}
