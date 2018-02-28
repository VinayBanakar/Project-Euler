public class SumE1
{
    public static void main(final String[] args)
    {
        int sum = 0;
        for (int i = 1; i < 100000000; i++)
        {
            if ((i % 5 == 0) || (i % 3 == 0))
            {
                sum += i;
            }
        }
        System.out.println(sum);
    }
}

