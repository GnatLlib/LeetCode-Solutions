/***
	Leetcode question 151. Reverse Words in a String
	Given an input string, reverse the string word by word
	For example,
	Given s= "the sky is blue"
	return "blue is sky the"
	
	***/

class Solution {
public:
    void reverseWords(string &s) {
      
    
	string rs="";
	string cword = "";
	vector<string> words;
  
	for(int i = 0; i<s.length(); i++)
		{
			if(s[i] == ' ')
			{
				if (cword != "")
				{
					words.push_back(cword);
				}
				cword = "";
			}
			else
			{
				cword += s[i];
			}
			if(i == s.length()-1)
			{
				if (s[i]!= ' ')
				{
					words.push_back(cword);
				}
			}
      
      
		}		
    
    for(int i =0; i< words.size(); i++)
    {
        if(i ==0)
        {
			rs = words[i] +  rs;
        }
        else
        {
            rs = words[i] + " " + rs;
        }
    }
       
       
      s = rs;
	  return;
    
	} 
            
};