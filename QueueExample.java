import java.util.*;
class QueueExample{
    public static void main(String [] args){
        Queue<Integer> Q1 = new LinkedList<>();
        Q1.add(10);
        Q1.add(20);
        Q1.add(30);
        Q1.add(40);
      System.out.println(Q1);
      System.out.println(Q1.peek());
      System.out.println(Q1.offer(2));
      System.out.println(Q1.poll());
      System.out.println(Q1.remove());
      System.out.println(Q1.element());
    }

}