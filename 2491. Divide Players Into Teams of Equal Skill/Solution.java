class Solution {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill); 
        long answer = 0; 
        int skillSize = skill[0] + skill[skill.length-1];
        for(int i=0;i<skill.length/2;i++){
            int currSkill = skill[i] + skill[skill.length-1-i];
            if (currSkill != skillSize){
                return -1;
            }
            answer += (skill[i]*skill[skill.length-1-i]);
        }
        return answer; 
    }
}
