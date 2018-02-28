public class PythogE9
{
    public static void pythSum(final int limit)
    {
        int m = 2, a, b, c = 0;
        while (c < limit)
        {
            for (int n = 1; n < m; ++n)
            {
                a = m * m - n * n;
                b = 2 * m * n;
                c = m * m + n * n;

                if (a + b + c == 1000)
                {
                    System.out.println("value: " + a * b * c);
                    break;
                }
                if (c > limit)
                {
                    break;
                }
                System.out.println("a " + a + " b " + b + " c " + c);
            }
            m++;
        }
    }

    public static void main(final String[] args)
    {
        pythSum(1000);
    }
}

