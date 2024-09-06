import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long long n = sc.nextLong();
        long long k = sc.nextLong();
        long long ans;

        if (n % 2 == 0) {
            if (k <= n / 2) {
                ans = k * 2 - 1;
            } else {
                ans = (k - (n / 2)) * 2;
            }
        } else {
            if (k <= ((n / 2) + 1)) {
                ans = k * 2 - 1;
            } else {
                ans = (k - (n / 2 + 1)) * 2;
            }
        }

        System.out.println(ans);
    }
}
