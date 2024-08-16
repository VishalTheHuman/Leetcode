class Solution {
    public int vowelStrings(String[] words, int left, int right) {
        int count = 0;
        for(int i=left;i<=right;i++){
            if((vowel(words[i].charAt(0)) && (vowel(words[i].charAt(words[i].length()-1)))))
            {
                count+=1;
            } 
        }
        return count;
    }
    public boolean vowel(char ch){
        if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
            return true;
        }
        return false;
    }
}