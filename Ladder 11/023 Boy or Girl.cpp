#include <iostream>
#include <cstring>
using namespace std;
int main()
{
   int s,cnt=0;
   char a[100];
   cin>>a;
   s =strlen(a);
   for(int i=0;i<s-1;i++)
    {
        for(int j=i+1;j<s;j++)
        if(a[i]==a[j])
        {
            count++;
            break;
        }
    }
    int c=s-cnt;
    if(c%2==0)
    {
        cout<<"CHAT WITH HER!";
    }
    else
    {
        cout<<"IGNORE HIM!";
    }
    return 0;
}
