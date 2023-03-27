double average(int* salary, int salarySize){
    int min = salary[0];
        int max = salary[0];
        double sum =0;
        for(int i=0;i<salarySize;i++){
            sum+=salary[i];
            if(salary[i]<min){
                min = salary[i];
            }else if(salary[i]>max){
                max = salary[i];
            }
        } 
        sum=sum-min-max;
        return sum/(salarySize-2);
}