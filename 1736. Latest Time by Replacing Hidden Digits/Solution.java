class Solution {
    public String maximumTime(String time) {
        char[] arr = time.toCharArray();
        arr[0] = arr[0] !='?' ? arr[0] : (arr[1] < '4' || arr[1] == '?' ? '2' : '1');
        arr[1] = arr[1] !='?' ? arr[1] : (arr[0]=='2' ? '3' : '9');
        arr[3] = arr[3] !='?' ? arr[3] : '5';
        arr[4] = arr[4] !='?' ? arr[4] : '9';
        return String.valueOf(arr);
    }
}
