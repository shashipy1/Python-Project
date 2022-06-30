#include<stdio.h>
//Traversal in Array
int display(int arr[], int n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    0
}
//Insertion in Array
int indInsertion(int arr[], int size, int element, int capacity, int index)
{
   if(size>=capacity){
       return -1;
   }
   for(int i=size-1; i>=index; i--)
   {
       arr[i+1]=arr[i];
   }
   arr[index]=element;
   return 1;
}

int main()
{
    int arr[7]={4,56,45,3,7,8,3};
    int size=7,element=34, index=4;
    display(arr,size);
    indInsertion(arr,size, element,20, index);
    size+=1;
    display(arr,size);
    
    return 0;
    
}

// Deletion in Array
#include<stdio.h>
int display(int arr[], int n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
    
}

int indDeletion(int arr[], int size, int index)
{
   for(int i=index; i<size-1; i++)
   {
       arr[i]=arr[i+1];
   }
}
int main()
{
    int arr[20]={4,56,45,3,7,8,3};
    int size=7,index=0;
    display(arr,size);
    indDeletion(arr,size, index);
    size-=1;
    display(arr,size);
    
    return 0;
}






//Linear Searching
#include<stdio.h>
int linearSearch(int arr[],int size, int element){
    for(int i=0; i<size; i++)
    {
        if(arr[i]==element)
        {
            return i;
        }
    }
        return -1;
     
}
int main()
{
    int arr[]={23,5,4,67,6,89};
    int size=sizeof(arr)/sizeof(int);
    //int searchIndex(arr, size, element);
    int element=67;
    int searchIndex=linearSearch(arr,size,element);
    printf("The element %d is found at index %d\n",element, searchIndex);
    return 0;
}








  //Searching Binary method
#include<stdio.h>
int linearSearch(int arr[],int size, int element){
    for(int i=0; i<size; i++)
    {
        if(arr[i]==element)
        {
            return i;
        }
    }
        return -1;
     
}

int binarySearch(int arr[], int size, int element){
    int low, mid, high;
    low=0;
    high=size-1;
    while(low<=high){
    mid=(low+high)/2;
    if(arr[mid]==element)
    {
        return mid;
    }
    if(arr[mid]<element)
    {
        low=(mid+1);
    }
    else{
        high=(mid-1);
    }
    }
    return -1;
}

int main()
{
    int arr[]={23,45,67,78,246,346};
    int size=sizeof(arr)/sizeof(int);
    //int searchIndex(arr, size, element);
    int element=246;
    int searchIndex=binarySearch(arr, size, element);
    printf("The element %d is found at index %d\n",element, searchIndex);
    return 0;
}