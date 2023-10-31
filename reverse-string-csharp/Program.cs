using System;

namespace StringReversalApp
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Please provide a string as an argument.");
                return;
            }

            string originalString = args[0];
            string reversedString = ReverseString(originalString);

            Console.WriteLine($"Original String: {originalString}");
            Console.WriteLine($"Reversed String: {reversedString}");
        }

        static string ReverseString(string input)
        {
            char[] charArray = input.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
