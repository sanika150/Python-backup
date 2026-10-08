def Marvellous_Display(matrix, title): 
    plt.figure(figsize=(4, 4)) 
    plt.imshow(matrix, cmap='gray', interpolation='nearest') 
    plt.title(title) 
    plt.colorbar() 
    for i in range(matrix.shape[0]): 
        for j in range(matrix.shape[1]): 
            plt.text(j, i, f"{matrix[i][j]:.1f}", 
                     ha='center', va='center', 
                     color='red', fontsize=12) 
    plt.show() 

if __name__ == "__main__":
    Marvellous_CNN_Internal_Steps()