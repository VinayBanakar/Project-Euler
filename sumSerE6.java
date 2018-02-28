public class sumSerE6
{
    public static void main(final String[] args)
    {
        final int val = 100;
        final int serSum = serSuma(val);
        final int sumSer = sumSeri(val);
        System.out.println(serSum - sumSer);
    }

    public static int serSuma(final int num)
    {
        int sum = 0;
        sum = num * (num + 1) * (2 * num + 1) / 6;
        return sum;
    }

    public static int sumSeri(final int num)
    {
        final int sum = num * (num + 1) / 2;
        return (sum * sum);
    }
}

