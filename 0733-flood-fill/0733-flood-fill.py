class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n= len(image[0])
        def dfs(image,i,j,ogcolor,color):
            if (i<0 or j<0 or i>=m or j>=n or image[i][j] != ogcolor or image[i][j] == color):
                return
            image[i][j]= color
            dfs(image,i+1,j,ogcolor,color)
            dfs(image,i-1,j,ogcolor,color)
            dfs(image,i,j+1,ogcolor,color)
            dfs(image,i,j-1,ogcolor,color)
        dfs(image,sr,sc,image[sr][sc],color)
        return image
