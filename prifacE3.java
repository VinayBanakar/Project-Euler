public class prifacE3
{
    public static void main(final String[] args)
    {
        final long val = 600851475143L;
        primefact(val);

    }

    public static void primefact(long val)
    {
        while (val % 2 == 0)
        {
            System.out.print(2 + " ");
            val /= 2;
        }
        for (int i = 3; i < Math.sqrt(val); i += 2)
        {
            while (val % i == 0)
            {
                System.out.print(i + " ");
                val /= i;
            }
        }
        if (val > 2)
        {
            System.out.print(val);
        }
    }
}

