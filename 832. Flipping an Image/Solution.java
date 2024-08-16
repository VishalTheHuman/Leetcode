class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int k;
        for(int i=0;i<image.length;i++){
            k=0;
            for(int j=0;j<image.length;j++){
                if(k<image.length/2){
                    int temp = image[i][k];
                    image[i][k]=image[i][image.length-1-k];
                    image[i][image.length-1-k]=temp;
                }
                if(image[i][j]==1){
                    image[i][j]=0;
                }else{
                    image[i][j]=1;
                }
                k++;
            }
        }
        return image;
    }
}