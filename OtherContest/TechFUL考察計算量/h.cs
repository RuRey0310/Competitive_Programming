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
            string[] abc = Console.ReadLine().Split(' ');
            double a = double.Parse(abc[0]);
            double b = double.Parse(abc[1]);
            double c = double.Parse(abc[2]);

            double ans = 1000;
            double nn = 10000;
            for(double x = 0.0001;x <= 100.0000;x += 0.0001)
            {
                double sub = a * Math.Pow(x, (2 + Math.Log(x))) + b * x + c;
                if(nn > sub)
                {
                    nn = sub;
                    ans = x;
                }
            }
            Console.WriteLine(Math.Round(ans,4,MidpointRounding.AwayFromZero));
            Console.Read();
        }
    }
}
