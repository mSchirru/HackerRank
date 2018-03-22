using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp11
{
    class Program
    {
        static void Main(string[] args)

        {
            string a = "", b = "";
            int t = Convert.ToInt32(Console.ReadLine());
            for(int i = 0; i < t; i++)
            {
                string x = Console.ReadLine();
                x.ToCharArray();
                for (int k = 0; k < x.Length; k ++)
                {
                    if(k % 2 == 0)
                    {
                        a = a + x[k].ToString();
                    }
                    else
                    {
                        b = b + x[k].ToString();
                    }
                }
                Console.WriteLine($"{a} {b}");
                a = "";
                b = "";
            }
            
        }
    }
}
