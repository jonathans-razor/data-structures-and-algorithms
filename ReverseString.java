public class ReverseString {
    public static void main(String[] args) {
        // Check if the user has passed in a command-line argument.
        if (args.length == 0) {
            System.out.println("Usage: ReverseStringCommandLineArgs <string>");
            System.exit(1);
        }

        // The input string to be reversed.
        String inputString = args[0];

        // Reverse the input string.
        String reversedString = "";
        for (int i = inputString.length() - 1; i >= 0; i--) {
            reversedString += inputString.charAt(i);
        }

        // Print the reversed string to the console.
        System.out.println("The reversed string is: " + reversedString);
    }
}