using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 問題H
{
    class Program
    {
        static void Main(string[] args)
        {
            int e = int.Parse(Console.ReadLine());
            int n = int.Parse(Console.ReadLine());
            int[,] st = new int[n,2];
            for(int i = 0; i < n; i++)
            {
                string[] cc = Console.ReadLine().Split(' ');
                st[i,0] = int.Parse(cc[0]);
                st[i,1] = int.Parse(cc[1]);
            }

            int[] table = new int[e + 1];
            for(int i = 0; i < n; i++)
            {
                table[st[i,0]] += 1;
                table[st[i, 1]] -= 1;
            }

            for(int i = 0; i < e; i++)
            {
                if(0 < i)
                {
                    table[i] += table[i - 1];
                }
            }

            int ans = 110000;
            for(int i= 0; i <  e; i++)
            {
                ans = Math.Min(ans, table[i]);
            }

            for(int i = 0; i < e; i++)
            {
                if(ans == table[i])
                {
                    Console.Write(i + " ");
                }
            }
            Console.Read();
        }
    }
}
