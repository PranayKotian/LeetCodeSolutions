//https://leetcode.com/problems/roman-to-integer/
//Title: Roman to Integer
//Difficulty: Easy
//Language: Java
//Author: Pranay Kotian
//Notes: Return to problem, solution extremely inefficient

class Solution {
    public int romanToInt(String s) {
        
        //String s
        char c;
        char b;
        
        int num = 0; 
        
        for (int i = s.length() - 1; i >= 0; i--) {
            c = s.charAt(i);
            if (i != 0)
                b = s.charAt(i-1);
            else
                b = c; 
            
            //Covers I V and X
            if (c == 'I')
                num+=1;
            else if (c == 'V') {
                if (b == 'I') {
                    num+=4;
                    i--;
                }
                else
                    num+=5;
                    
            }
            else if (c == 'X') {
                if (b == 'I') {
                    num+=9;
                    i--;
                }
                else
                    num+=10;
                    
            }
            
            //Covers X L and C
            else if (c == 'X')
                num+=10;
            else if (c == 'L') {
                if (b == 'X') {
                    num+=40;
                    i--;
                }
                else
                    num+=50;
                    
            }
            else if (c == 'C') {
                if (b == 'X') {
                    num+=90;
                    i--;
                }
                else
                    num+=100;
                    
            }
            
            //Covers C D and M
            else if (c == 'C')
                num+=100;
            else if (c == 'D') {
                if (b == 'C') {
                    num+=400;
                    i--;
                }
                else
                    num+=500;
                    
            }
            else if (c == 'M') {
                if (b == 'C') {
                    num+=900;
                    i--;
                }
                else
                    num+=1000;
            }
        }
        
        return num; 
            
    }
}