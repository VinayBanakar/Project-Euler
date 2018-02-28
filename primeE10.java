public class primeE10
{
    public static void main(final String[] args)
    {
        int i = 2;
        long sum = 0;
        while (i < 2000000)
        {
            if (checkIfPrime(i))
            {
                sum += i;
            }
            i++;
        }
        System.out.println(sum);
    }

    public static boolean checkIfPrime(final int i)
    {
        for (int j = 2; j <= Math.sqrt(i); ++j)
        {
            if (i % j == 0)
            {
                return false;
            }
        }
        return true;
    }
}

