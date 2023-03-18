import java.util.*;

public class NewPage {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        long sumx = 0, sumy = 0;
        long[] x = new long[n], y = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = in.nextLong();
            y[i] = in.nextLong();
            sumx += x[i];
            sumy += y[i];
        }
        Arrays.sort(x);
        Arrays.sort(y);
        long s_x = 0, s_y = 0;
        long ans = 0;
        for (int i = 0; i < n; i++) {
            s_x += x[i];
            ans += Math.abs(s_x - (x[i] * (i + 1)));
            s_y += y[i];
            ans += Math.abs(s_y - (y[i] * (i + 1)));
        }
        System.out.print(ans);
    }
}
