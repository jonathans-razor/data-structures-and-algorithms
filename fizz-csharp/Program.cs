using System;

class Program
{
    static void Main()
    {
        for (int i = 1; i <= 100; i++)
        {
            string output = "";
            if (i % 3 == 0)
                output += "Fizz";
            if (i % 5 == 0)
                output += "Buzz";
            if (i % 7 == 0)
                output += "Bazz";

            Console.WriteLine(output != "" ? output : i.ToString());
        }
    }
}