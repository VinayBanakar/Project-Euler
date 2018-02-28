public class fibE2
{
    public static void main(final String[] args)
    {
        int fob = 1;
        int fib = 2;
        int fab = 0;
        int eve = 0;
        while (fab < 4000000)
        {
            fab = fob + fib;
            if (fab % 2 == 0)
            {
                eve += fab;
            }
            fob = fib;
            fib = fab;
        }
        System.out.println(eve);
    }
}

