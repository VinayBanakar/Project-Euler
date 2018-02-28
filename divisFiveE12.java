import java.util.Hashtable;

public class divisFiveE12
{
    public static void main(final String[] args)
    {
        final int i = 1;
        long tmp = 0, sum = 0;
        while (true)
        {
            sum += 1;
            tmp += sum;
            System.out.println("traingle num: " + tmp);
            if (checkDiv(tmp) > 500)
            {
                System.out.println(" final traingle num: " + tmp);
                break;
            }
        }
    }

    public static int checkDiv(long tmp)
    {
        final Hashtable<Integer, Integer> ht = new Hashtable<Integer, Integer>();
        ht.put(2, 0);
        ht.put(3, 0);
        ht.put(5, 0);
        ht.put(7, 0);
        ht.put(11, 0);
        ht.put(13, 0);
        ht.put(17, 0);
        while (tmp % 2 == 0)
        {
            ht.put(2, ht.get(2) + 1);
            tmp /= 2;
        }
        while (tmp % 3 == 0)
        {
            ht.put(3, ht.get(3) + 1);
            tmp /= 3;
        }
        while (tmp % 5 == 0)
        {
            ht.put(5, ht.get(5) + 1);
            tmp /= 5;
        }
        while (tmp % 7 == 0)
        {
            ht.put(7, ht.get(7) + 1);
            tmp /= 7;
        }
        while (tmp % 11 == 0)
        {
            ht.put(11, ht.get(11) + 1);
            tmp /= 11;
        }
        while (tmp % 13 == 0)
        {
            ht.put(13, ht.get(13) + 1);
            tmp /= 13;
        }
        while (tmp % 17 == 0)
        {
            ht.put(17, ht.get(17) + 1);
            tmp /= 17;
        }
        final int mul = (ht.get(2) + 1)
                * (ht.get(3) + 1)
                * (ht.get(5) + 1)
                * (ht.get(7) + 1)
                * (ht.get(11) + 1)
                * (ht.get(13) + 1)
                * (ht.get(17) + 1);
        System.out.println("multiplication val: " + mul);
        System.out.println(ht);
        return mul;
    }
}

