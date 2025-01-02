class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        int[] count = new int[words.length+1]; 
        int[] answer = new int[queries.length]; 
        count[0] = 0; 
        for(int i=0;i<words.length;i++){
            count[i+1] = count[i] + ((
                checkVowel(words[i].charAt(0)) && 
                checkVowel(words[i].charAt(words[i].length()-1))
            ) ? 1 : 0);
        }
        for(int i=0; i<queries.length;i++){
            answer[i] = count[queries[i][1]+1] - count[queries[i][0]];
        }
        return answer; 
    }

    public boolean checkVowel(char x){
        return (x=='a'||x == 'e'||x=='i'||x=='o'||x=='u');
    }
}
