class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        String[] n1 = num1.split("\\+");
        n1[1]=n1[1].substring(0,n1[1].length()-1);
        String[] n2 = num2.split("\\+");
        n2[1]=n2[1].substring(0,n2[1].length()-1);
        StringBuilder str = new StringBuilder();
        int real = Integer.parseInt(n1[0])*Integer.parseInt(n2[0]);
        real+= -1*(Integer.parseInt(n1[1])*Integer.parseInt(n2[1]));
        int imaginary = Integer.parseInt(n1[1])*Integer.parseInt(n2[0]);
        imaginary+= Integer.parseInt(n1[0])*Integer.parseInt(n2[1]);
        str.append(Integer.toString(real));
        str.append("+");
        str.append(Integer.toString(imaginary));
        str.append("i");
        return str.toString();
    }
}