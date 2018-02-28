public class CollatzE14
{
    public static void main(final String[] args)
    {
        //final int[] arr = new int[1000000];
        long i = 3, max = 0, pos = 0;
        //arr[0] = 0;
        long val = 0;
        while (i < 1000000)
        {
            System.out.println(i);
            val = shreder(i);
            if (val > max)
            {
                max = val;
                pos = i;
            }
            i++;
        }
        System.out.println(" max " + max + " pos " + pos);
    }

    public static long shreder(long i)
    {
        long count = 0;
        while (i > 0)
        {
            if (i % 2 == 0)
            {
                i = i / 2;
                count++;
                System.out.print(i + " ");
            }
            else
            {
                i = 3 * i + 1;
                count++;
                System.out.print(i + " ");
            }
            if (i == 1)
            {
                System.out.println("I am 1");
                break;
            }
        }
        System.out.println(" i "+i+" count "+count);
        return count + 1;
    }
}

