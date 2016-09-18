/**
	LeetCode Question 12.
	Integer to Roman
	
	Given an integer, convert it to a roman numeral.
	Input is guaranteed to be within the range from 1 to 3999.
	
	**/

class Solution {
public:
    string intToRoman(int num) {
        
        int thousands = 0;
        int fundreds = 0;
        int hundreds = 0;
        int fifty = 0;
        int tens = 0;
        int fives = 0;
        int ones = 0;
        string numeral;
        while(num-1000>=0)
        {
            thousands++;
            num = num-1000;
        }
        while(num-500>=0)
        {
            fundreds++;
            num = num-500;
        }
        
        while(num-100>=0)
        {
            hundreds++;
            num = num-100;
        }
        
        while(num-50>=0)
        {
            fifty++;
            num = num-50;
        }
        
        while(num-10>=0)
        {
            tens++;
            num = num-10;
        }
        if(num-5>=0)
        {
            fives++;
            num = num-5;
        }
        while(num-1>=0)
        {
            ones++;
            num = num-1;
        }
        for(int i = 0; i<thousands; i++)
        {
            numeral += "M";
        }
        
        if(fundreds == 1 &&  hundreds == 4)
        {
            numeral +="CM";
        }
        else{
            if(fundreds == 0 && hundreds == 4)
            {
                numeral+="CD";
            }
            else{
                if(fundreds ==1)
                {
                    numeral+="D";
                }
            
        for(int i = 0; i<hundreds; i++)
        {
            numeral +="C";
        }
            }
        }
        if(fifty == 1 && tens == 4)
        {
            numeral +="XC";
        }
        else{
            if(fifty == 0 && tens == 4)
            {
                numeral+="XL";
            }
            else{
                if(fifty ==1)
                {
                    numeral+="L";
                }
            
        for(int i = 0; i<tens; i++)
        {
            numeral +="X";
        }
            }
        }
        
        if(fives == 1 && ones == 4)
        {
            numeral+="IX";
            return numeral;
        }
        if(fives == 0 && ones == 4)
        {
            numeral+="IV";
            return numeral;
        }
        if(fives == 1)
        {
            numeral+="V";
            
        }
        for(int i = 0; i<ones; i++)
        {
            numeral+="I";
        }
        
        
        return numeral;
    }
};