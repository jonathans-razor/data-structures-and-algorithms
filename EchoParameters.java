public class EchoParameters {
    public static void main(String[] args) {
      if (args.length == 0) {
            System.out.println("- Parameter(s) expected.");
            return;
      }
      for (String arg : args) {
          System.out.println(arg);
      }
    }
}