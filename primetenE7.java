public class primetenE7
{
    public static void main(final String[] args)
    {
        int prime = 2;
        int pos = 1;
        while (true)
        {
            if (checkIfPrime(prime))
            {
                if (pos ==  10001)
                {
                    System.out.println(prime + " pos:" + pos);
                    break;
                }
                pos++;
            }
            prime++;
        }
    }

    public static boolean checkIfPrime(final int prime)
    {
        for (int i = 2; i <= Math.sqrt(prime); i++)
        {
            if (prime % i == 0)
            {
                return false;
            }
        }
        return true;

    }
}

