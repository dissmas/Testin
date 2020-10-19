public class Numbers {
    public long factorial (int n){
        long res = 1;
        if (n == 0 || n == 1)
            return 1;

        for (int i = 1; i < n+1; i++){
            res *= i;
        }
        return res;
    }

    public int add (int a, int b){
        return a+b;
    }

    public int diff (int a, int b){
        return a-b;
    }

    public int mul (int a, int b){
        return a*b;
    }

   public int div (int a, int b){
        return a/b;
    }

}
