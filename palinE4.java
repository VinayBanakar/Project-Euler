public class palinE4
{
    public static void main(final String[] args)
    {
        //111 to 999
        int max = 0;
        int a = 0, b = 0;
        boolean check = false;
        for (int i = 111; i <= 999; i++)
        {
            for (int j = 111; j <= 999; j++)
            {
                final int val = i * j;
                check = palanCheck(val);
                if (check == true && val > max)
                {
                    a = i;
                    b = j;
                    max = val;
                }
            }
        }
        System.out.println(max + " " + a + " " + b);
    }

    public static boolean palanCheck(int val)
    {
        final int n = val;
        int rev = 0, dig = 0;
        while (val > 0)
        {
            dig = val % 10;
            rev = rev * 10 + dig;
            val = val / 10;
        }
        if (n == rev)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

