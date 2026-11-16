import java.util.Scanner;

public class P4 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid input");
            sc.close();
            return;
        }

        int[] weight = new int[n];
        int[] value = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter weight and value: ");
            weight[i] = sc.nextInt();
            value[i] = sc.nextInt();

            if (weight[i] <= 0 || value[i] < 0) {
                System.out.println("Invalid input");
                sc.close();
                return;
            }
        }

        System.out.print("Enter knapsack capacity: ");
        int W = sc.nextInt();

        if (W < 0) {
            System.out.println("Invalid capacity");
            sc.close();
            return;
        }

        // dp[i][j] = maximum value using first i items with capacity j
        int[][] dp = new int[n + 1][W + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= W; j++) {

                // Exclude the current item
                dp[i][j] = dp[i - 1][j];

                // Include the current item if its weight allows
                if (weight[i - 1] <= j) {
                    dp[i][j] = Math.max(
                        dp[i][j],
                        value[i - 1] + dp[i - 1][j - weight[i - 1]]
                    );
                }
            }
        }

        System.out.println("Maximum value: " + dp[n][W]);

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
Maximum value: 220

NOTE:
Time Complexity: O(n x W)
Space Complexity: O(n x W)

RUN:
javac P4.java
java P4
*/