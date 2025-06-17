import java.io.IOException;
import java.util.Arrays;

public class Reverse {
    public static void main(String[] args) {
        try {
            MyScanner scanner = new MyScanner();
            int[][] mas = new int[10][10];
            int c = mas.length;
            int i = 0;
            while (scanner.hasNextLine()) {
                int j = 0;
                String line = scanner.nextLine();
                MyScanner sc = new MyScanner(line);
                if (i == mas.length) {
                    mas = Arrays.copyOf(mas, mas.length * 2);
                    for (int k = c; k < mas.length; k++) {
                        mas[k] = new int[10];
                    }
                    c = mas.length;
                }
                while (sc.hasNextInt()) {
                    if (j == mas[i].length) {
                        mas[i] = Arrays.copyOf(mas[i], mas[i].length * 2);
                    }
                    int n = sc.nextInt();
                    if (n == 0) {
                        mas[i][j] = Integer.MAX_VALUE;
                    } else {
                        mas[i][j] = n;
                    }
                    j++;
                }
                i++;
                sc.close();
            }
            scanner.close();
            for (int k = i - 1; k >= 0; k--) {
                for (int j = mas[k].length - 1; j >= 0; j--) {
                    if (mas[k][j] == 0) {
                        continue;
                    }
                    if (mas[k][j] == Integer.MAX_VALUE) {
                        System.out.print(0 + " ");
                    } else {
                        System.out.print(mas[k][j] + " ");
                    }
                }
                if (k != i) {
                    System.out.println();
                }
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}