import java.util.*;

public class P3 {

    static class Item {
        int wt, val;
        double ratio;

        Item(int wt, int val) {
            this.wt = wt;
            this.val = val;
            ratio = (double) val / wt;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid input");
            sc.close();
            return;
        }

        Item[] items = new Item[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight and value: ");
            int wt = sc.nextInt();
            int val = sc.nextInt();

            if (wt <= 0 || val < 0) {
                System.out.println("Invalid input");
                sc.close();
                return;
            }

            items[i] = new Item(wt, val);
        }

        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        if (W < 0) {
            System.out.println("Invalid capacity");
            sc.close();
            return;
        }

        // Sort items by value/weight ratio
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));

        double total = 0;

        // Fill the knapsack
        for (Item item : items) {
            if (W == 0)
                break;

            if (item.wt <= W) {
                total += item.val;
                W -= item.wt;
            } else {
                total += item.ratio * W;
                W = 0;
            }
        }

        System.out.println("Maximum value: " + total);

        sc.close();
    }
}

/*
SAMPLE INPUT:
3
10 60
20 100
30 120
50

SAMPLE OUTPUT:
Maximum value: 240.0

NOTE:
Time Complexity: O(n log n)
Space Complexity: O(n)
*/