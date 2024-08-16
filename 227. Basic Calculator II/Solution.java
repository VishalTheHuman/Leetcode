class Solution {
    public int calculate(String s) {
        s += "+";
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char prev = '+';
        for(char x : s.toCharArray()){
            if (x==' '){
                continue;
            }else if(Character.isDigit(x)){
                num = num*10 + Character.getNumericValue(x);
            }else{
                if (prev=='+'){
                    stack.push(num);
                }else if (prev=='-'){
                    stack.push(-num);
                }else if (prev=='*'){
                    stack.push(stack.pop()*num);
                }else{
                    stack.push(stack.pop()/num);
                }
                num = 0;
                prev = x;
            }
        }

        int sum = 0;
        while (stack.size()>0){
            sum += stack.pop();
        }
        return sum;
    }
}