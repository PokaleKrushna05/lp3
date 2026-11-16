import java.util.Scanner;

public class P5 {

    static int n;
    static int[] q;  // q[row] = column of the queen in that row

    // Check whether placing a queen is safe
    static boolean isSafe(int row, int col) {
        for (int r = 0; r < row; r++) {
            if (q[r] == col || Math.abs(q[r] - col) == row - r) {
                return false;
            }
        }
        return true;
    }

    // Place queens row by row using backtracking
    static boolean solve(int row) {
        if (row == n) {
            return true;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                q[row] = col;

                if (solve(row + 1)) {
                    return true;
                }
            }
        }

        return false;  // Backtrack if no position works
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter value of N: ");
        n = sc.nextInt();

        if (n <= 0) {
            System.out.println("Invalid N");
            sc.close();
            return;
        }

        System.out.print("Enter first queen column (1 to " + n + "): ");
        int col = sc.nextInt();

        if (col < 1 || col > n) {
            System.out.println("Invalid column");
            sc.close();
            return;
        }

        q = new int[n];
        q[0] = col - 1;  // Place first queen in row 0

        if (solve(1)) {
            System.out.println("N-Queens Matrix:");

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print((q[i] == j ? 1 : 0) + " ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution exists");
        }

        sc.close();
    }
}

/*
SAMPLE INPUT:
4
3

SAMPLE OUTPUT:
N-Queens Matrix:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

NOTE:
1 represents a queen and 0 represents an empty position.
The first queen is placed in row 0 at the column entered.
Backtracking: if no column works in a row, return to the
previous row and try another column.

RUN:
javac P5.java
java P5
*/